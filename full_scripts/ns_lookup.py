from nslookup import Nslookup


def lookup(domain):
    if not domain:
        domain = input('Enter host: ')
    try:
        dns_query = Nslookup(dns_servers=["1.1.1.1"])# ctftime.org
    except:
        print("Error!")
    else:
        try:
            ips_record = dns_query.dns_lookup(domain)
        except:
            print("Error!")
        else:
            ans=[]
            for i in ips_record.response_full:
                ans.append(i)
            soa_record = dns_query.soa_lookup(domain)
            for i in soa_record.response_full:
                ans.append('\n'.join(i.split('. ')))
            return ans
