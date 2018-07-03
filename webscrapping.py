import urllib.request
import random
import string
from bs4 import BeautifulSoup as bs
from multiprocessing import Pool

'''
AUTHOR : PUSPENDU

PURPOSE:  This script uses random module to generate
            random links and using those links it's
            trying extract the content of the webpage and
            save the webpage content in the form of a file.
            if the randomly generated link does not exist
            exception handling is there.

NOTE: I have used multiprocessing module to run the code in less time

'''


def random_url():
    url = [random.choice(string.ascii_lowercase) for _ in range(4)]
    url = ''.join(url)
    url = 'http://' + url + '.com'
    return url


def get_webpage(url):
    try:
        webpage = urllib.request.urlopen(url)
        webpage = bs(webpage, 'html')
        print(webpage)
        with open('D:\\PYTHON_LAB\\raw_url.html', 'a') as f:
            f.write(str(webpage))

    except Exception as e:
        pass


def main():
    how_many = 50
    p = Pool(processes=how_many)
    url_list = [random_url() for _ in range(50)]
    p.map(get_webpage, [link for link in url_list])
    p.close()


if __name__ == '__main__':
    main()
