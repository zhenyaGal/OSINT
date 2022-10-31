import pygeoip
from inspect import getsourcefile
from os.path import abspath
import socket


def geo_ip(domain):
    if not domain:
        ip = input('Enter ip: ')#109.233.56.78
    else:
        try:
            ip = socket.gethostbyname(domain)
            print(ip)
        except:
            print("Error in function socket.gethostbyname")
    p = abspath(getsourcefile(lambda: 0))
    try:
        gi = pygeoip.GeoIP(str(p)[:-16] + 'GeoIPCity.dat')
    except FileNotFoundError as e:
        print(e)
    else:
        try:
            city = gi.record_by_addr(ip)
            if city == None:
                return False
        except OSError as e:
            print(e)
        except:
            print("Error in function gi.record_by_addr")
        else:
            print(city)
            ans = []
            for key in city:
                if city[key] is None or city[key]:
                    if city[key] is None or city[key] == 0:
                        continue
                    else:
                        ans.append(f"{key}: {city[key]}")
            return ans
