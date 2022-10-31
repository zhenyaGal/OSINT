import socket


def address(host):
    if not host:
        host = input('Enter host: ')# ctftime.org
    if '://' in host:
        host = host.split('://')[1]
    host = host.replace('/', '')
    try:
        remote_ip = socket.gethostbyname(host)
    except (TypeError, KeyboardInterrupt) as e:
        print(e)
    except:
        print("Error")
    else:
        ans=[]
        ans.append(f"{'IP Address of '}{host}{' is '}{remote_ip}")
        return ans
