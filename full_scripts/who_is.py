import whois


def who_is(add):
    if not add:
        add = input('Enter domain: ')# ctftime.org
    try:
        domain = whois.query(add)
        res = domain.__dict__
    except:
        print("Error!")
    else:
        ans=[]
        for i in res:
            ans.append(f"{i}: {res[i]}")
        return ans
