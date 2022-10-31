import dns.resolver


def find_server(address):
    if not address:
        address = input('Enter host: ')# ctftime.org
    my_resolver = dns.resolver.Resolver(configure=False)
    my_resolver.nameservers = ['8.8.8.8', '1.1.1.1']
    try:
        answers = my_resolver.query(address, "MX")
    except dns.resolver.NXDOMAIN as e:
        print(e)
    except:
        print("Error!")
    else:
        ans = []
        for rdata in answers:
            ans.append(f"MX Record: {rdata.exchange}")
        return ans
