import os
import re
import urllib.parse

from glob import glob

import requests

def fixer(ctx):
    def fix(m):
        ctx['used'] = True

        article = ctx['article']
        text = m.group('text')
        link = m.group('url')

        img_url_name = link.split('/')[-1]

        uniq_id = os.urandom(4).hex()

        img_out = 'images/%s--%s--%s' % (
            article, uniq_id, urllib.parse.unquote(img_url_name)
        )

        img_url = 'images/%s--%s--%s' % (
            article, uniq_id, img_url_name
        )

        print('[+] Download %s to %s' % (link, img_out))

        img = requests.get(link).content
        with open('content/' + img_out, 'wb') as fout: fout.write(img)

        return '![%s](%s)' % (text or img_url_name, img_url)
    return fix

for article in glob('**/*.md', recursive=True):
    with open(article) as fin:
        content = fin.read()
    ctx = {'used': False, 'article': article.split('/')[-1][:-3]}
    content = re.sub(r'!\[(?P<text>[^\]]*)\]\((?P<url>https?:[^\)]+)\)', fixer(ctx), content)
    if ctx['used']:
        print('[+] Fixed file: ' + article)
        with open(article, 'w') as fout:
            fout.write(content)
