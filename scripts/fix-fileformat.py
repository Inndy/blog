import re
import glob

article_pattern = '**/*.md'

for article in glob.glob(article_pattern, recursive=True):
    with open(article, 'r') as fin:
        content = fin.read()
    content = re.sub(r'[\r\s]+\n', '\n', content, flags=re.M)
    with open(article, 'w') as fout:
        fout.write(content)
        if content[-1] != '\n':
            fout.write('\n')
