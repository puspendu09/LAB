import re

with open('raw_url.txt', 'r+') as f:
    text = f.read()
    f.close()


# split_pattern = re.compile(r'[/]', re.IGNORECASE)
matching_pattern = re.compile(r'https?://[a-zA-Z_0-9.-]+\.[a-zA-Z]+')
web_URL = matching_pattern.finditer(text)
for url in web_URL:
    with open('websites.csv', 'a+') as f:
        f.write(str(url.group()))
        f.write('\n')
