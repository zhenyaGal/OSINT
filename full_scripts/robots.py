import requests


def main(url):
    if url:
        url = 'https://' + url
    else:
        url = input('Enter host [https://site.com]: ')# https://ctftime.org
    head = {"User-Agent": "Mozilla/5.0 (X11; Linux x84_64) AppleWebKit/537.36 "
            "KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
    try:
        if url[-1] == '/':
            page = requests.get(url + 'robots.txt', headers=head)
        else:
            page = requests.get(url + '/robots.txt', headers=head)
    except requests.exceptions.MissingSchema as e:
        print(e)
    except:
        print("Error")
    else:
        if page.status_code != 404:
            return page.text.split('\n')
        else:
            print('File "robots.txt" not found')


if __name__ == '__main__':
    main()


