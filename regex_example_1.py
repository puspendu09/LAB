import re


def raw_text():
    with open('C:\\Python\\Python36\\LAB\\url.txt', 'r+') as f:
        text = f.read()
        # print(text)
        f.close()
        return text


def filtered_url(raw_text):
    ''' this method take text input and write in the
     files which url matches the pattern'''
    pattern = re.compile(r'https?://[a-zA-Z0-9._]+\.[a-zA-Z-]+')
    links = pattern.finditer(raw_text)
    for matching_link in links:
        # print(matching_link.group())
        with open('D:\\PYTHON_LAB\\filtered_url.txt', 'a') as f1:
            f1.write(str(matching_link.group()))
            f1.write('\n')
            print('.')


def remove_duplicate():
    with open('D:\\PYTHON_LAB\\filtered_url.txt', 'r') as f2:
        all_url = f2.read().split('\n')
        temp_distinct_url = set(all_url)
        for url in temp_distinct_url:
            with open('D:\\PYTHON_LAB\\distinct_url.txt', 'a') as f3:
                f3.write(url)
                f3.write('\n')


def main():
    # text_raw = raw_text()
    # filtered_url(text_raw)
    # remove_duplicate()
    print(filtered_url.__doc__)


if __name__ == '__main__':
    main()
