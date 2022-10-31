import requests
from bs4 import BeautifulSoup


def get_pages_data(html):
    ans = []
    res = BeautifulSoup(html.text, 'lxml')
    line = res.find_all("loc")
    for i in line:
        ans.append(i.text)
    return ans


def main(url):
    if url:
        url = 'https://' + url
    else:
        url = input('Enter host [https://site.com]: ')# https://edu.hackeru.pro/
    try:
        if url[-1] == '/':
            page = requests.get(url + 'sitemap.xml')
        else:
            page = requests.get(url + '/sitemap.xml')
    except requests.exceptions.MissingSchema as e:
        print(e)
    except:
        print("Error")
    else:
        if page.status_code == 200:
            return get_pages_data(page)
        else:
            print('File "sitemap.xml" not found')


if __name__ == '__main__':
    main()
