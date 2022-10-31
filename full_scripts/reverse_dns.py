from dns import reversename, resolver
import socket


def pointer(domain):
    if domain:
        try:
            ip = socket.gethostbyname(domain)
        except:
            print("Error")
    else:
        ip = input('Enter ip: ')# 77.88.55.55
    try:
        rev_name = reversename.from_address(ip)
    except:
        print("Error")
    try:
        ans = (str(resolver.query(rev_name, "PTR")[0]), )
        return ans
    except Exception as e:
        print(e)
