import socket

import full_scripts.ip_address as add
import full_scripts.site_location as geo
import full_scripts.who_is as who
import full_scripts.ns_lookup as ns
import full_scripts.dns_mxrecord as dns
import full_scripts.reverse_dns as rdns
import full_scripts.robots as robots
import full_scripts.sitemap as sitemap
import full_scripts.reverse_ip_lookup as reverse_ip_lookup


logo = "\033[32m" + r'''
  ___  ____ ___ _   _ _____   ____   _____  __
 / _ \/ ___|_ _| \ | |_   _| | __ ) / _ \ \/ /
| | | \___ \| ||  \| | | |   |  _ \| | | \  / 
| |_| |___) | || |\  | | |   | |_) | |_| /  \ 
 \___/|____/___|_| \_| |_|   |____/ \___/_/\_\
'''


def num_input():
    try:
        num = int(input('\nEnter the option number: '))
    except (ValueError, TypeError):
        print('Error input!')
        exit(1)
    except (EOFError, KeyboardInterrupt):
        print('Cancel operation')
        exit(1)
    else:
        return num


def exit_prog(_):
    print("The program is complete!")
    exit(0)


def all_items(_):
    try:
        domain = input("Enter domain: ")
    except KeyboardInterrupt as e:
        print(e)
    else:
        for i in range(1,10):
            print('-'*35, dict[i-1][0], '-'*35, sep='\n')
            if ans := dict[i-1][1](domain):
                print('\n'.join(ans))


if __name__ == '__main__':
    print(logo)
    dict = {-1: ("0. Exit the program", exit_prog),
            0: ("1. Host Ip ", add.address),
            1: ("2. Site location ", geo.geo_ip),
            2: ("3. Whois ", who.who_is),
            3: ("4. Nslookup", ns.lookup),
            4: ("5. DNS MX-Record ", dns.find_server),
            5: ("6. Reverse DNS ", rdns.pointer),
            6: ("7. robots.txt ", robots.main),
            7: ("8. sitemap.xml ", sitemap.main),
            8: ("9. Reverse ip lookup ", reverse_ip_lookup.find_domains),
            9: ("10. All items " + "\033[0m", all_items)}

    for value in dict.values():
        print(value[0])

    while True:
        if 0 <= (num := num_input()) <= 9:
            print('-'*35, dict[num-1][0], '-'*35, sep='\n')
            if ans := dict[num-1][1](None):
                print('\n'.join(ans))
        elif num == 10:
            all_items(num)
        else:
            print("Enter 0-10!")


