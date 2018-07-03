import urllib.request
import random
import string
from bs4 import BeautifulSoup as bs
from multiprocessing import Pool


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
        with open('D:\\PYTHON_LAB\\raw_url.csv', 'a') as f:
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
