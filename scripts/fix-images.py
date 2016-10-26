import os
import re

from glob import glob

import requests

def fixer(refs):
    def fix(m):
        refs['used'] = True
        article = refs['article']
        text = m.group('text')
        ref = m.group('ref')
        link = refs[ref]

        img_url_name = link.split('/')[-1]

        img_out = 'images/%s--%s--%s' % (
            article, os.urandom(4).hex(), img_url_name
        )

        print('[+] Download %s to %s' % (link, img_out))

        img = requests.get(link).content
        with open('content/' + img_out, 'wb') as fout: fout.write(img)

        return '![%s](%s)' % (text or img_url_name, img_out)
    return fix

for article in glob('**/*.md', recursive=True):
    with open(article) as fin:
        content = fin.read()
    refs = {'used': False, 'article': article.split('/')[-1][:-3]}
    for idx, url in re.findall(r'^\[(\d+)\]:\s*(.*)', content, re.M):
        refs[idx] = url
    content = re.sub(r'!\[(?P<text>[^\]]*)\]\[(?P<ref>\d+)\]', fixer(refs), content)
    if refs['used']:
        print('[+] Fixed file: ' + article)
        with open(article, 'w') as fout:
            fout.write(content)
