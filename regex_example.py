import re

'''
AUTHOR : PUSPENDU
PURPOSE: This script takes a text file as an input
         (in this code the 'raw_url.txt')
         and extract all the  links which matches
         certain pattern.

NOTE: Please refer webscrapping.py to generate raw_url.txt

'''

with open('raw_url.html', 'r+') as f:
    text = f.read()
    f.close()


# split_pattern = re.compile(r'[/]', re.IGNORECASE)
matching_pattern = re.compile(r'https?://[a-zA-Z_0-9.-]+\.[a-zA-Z]+')
web_URL = matching_pattern.finditer(text)
for url in web_URL:
    with open('websites.txt', 'a+') as f:
        f.write(str(url.group()))
        f.write('\n')
        print(str(url.group()))
