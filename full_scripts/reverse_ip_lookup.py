import socket
import requests
from bs4 import BeautifulSoup


def get_ip(host):
    if '://' in host:
        host = host.split('://')[1]
    host = host.replace('/', '')
    try:
        ip = socket.gethostbyname(host)
    except (TypeError, KeyboardInterrupt) as e:
        print(e)
        return False
    except:
        print("Error")
        return False
    else:
        return ip


def find_domains(host):
    if not host:
        host = input('Enter IP or Domain: ')# luxdevices.com
    if ip := get_ip(host):
        print(f"{'Found domain hosted on the same web server as '}{host}{ip}")
        API_KEY = '3c09f6900f0d774ceed5e9d06ec8c5aef2679bf5'
        params = dict(apikey=API_KEY, host=ip, output='xml', verify=False)
        try:
            res = requests.get('https://api.viewdns.info/reverseip/', params=params)
            soup = BeautifulSoup(res.text, 'lxml')
            line = soup.findAll('name')
        except:
            print("Error")
        else:
            ans = []
            for i in line:
                ans.append(i.text)
            return ans



