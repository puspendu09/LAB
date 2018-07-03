import re


html = '''<html><a href = 'puspemdi.com'></a></html>'''
pattern = re.compile(r'<.*?>')
html_match = pattern.finditer(html)

for html in html_match:
    print(html.group())
