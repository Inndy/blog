import re
from glob import glob

for article in glob('content/**/*.md', recursive=True):
    with open(article) as fin:
        content = fin.read()
    content = re.sub(r'!\[(.*?)\]\(', r'![\1](/', content)
    with open(article, 'w') as fout:
        fout.write(content)
