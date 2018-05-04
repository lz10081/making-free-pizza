import requests
import datetime
import time
import names
import os
import random

def header():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
header()
month = datetime.datetime.now().month+1
email = raw_input('Enter your Gmail or catchall domain: ')
emaildomain = email
catchall = 1
if '@' in email:
    emailname = email.split('@')[0]
    emaildomain = '@' + email.split('@')[1]
    catchall = 0
header()
acode = raw_input('Enter the first three digits of your phone number: ')
header()
headers = {
    'origin': 'https://www.papajohns.com',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'accept': '*/*',
    'referer': 'https://www.papajohns.com/order/create-account',
    'authority': 'www.papajohns.com',
    'x-requested-with': 'XMLHttpRequest',
    'request-source': 'freight',
}
registered = 0
s = requests.Session()
while True:
    s.cookies.clear()
    firstname = names.get_first_name()
    lastname = names.get_last_name()
    if catchall == 0:
        email = emailname + "+" + str(random.randint(1,999999)) + emaildomain
    else:
        email = firstname + lastname + "@" + emaildomain
    phone = "(" + acode + ") " + str(random.randint(111, 999)) + "-" + str(random.randint(1111, 9999))
    data = [
      ('firstName', firstname),
      ('lastName', lastname),
      ('emailAddress', email),
      ('password_autofill_off', ''),
      ('createPassword', 'P1zzapie'),
      ('phoneNumber', phone),
      ('birthMonth', month),
      ('birthDayOfMonth', '1'),
      ('papaRewardsRedeemPoints', 'on'),
      ('createAccountCountry', 'usa'),
      ('locationType', 'HOME'),
      ('usCampusTerritoryCode', 'CA'),
      ('usCampus', ''),
      ('caCampusTerritoryCode', ''),
      ('caCampus', ''),
      ('campusBuildingId', ''),
      ('campusRoomNumber', ''),
      ('usBaseTerritoryCode', 'CA'),
      ('usBase', ''),
      ('caBaseTerritoryCode', ''),
      ('caBase', ''),
      ('baseBuildingId', ''),
      ('baseRoomNumber', ''),
      ('streetAddress', 'One Infinite Loop'),
      ('aptCode', 'NON'),
      ('usCity', 'Cupertino'),
      ('usResidentialTerritoryCode', 'CA'),
      ('usPostalCode', '95014'),
      ('caCity', 'Cupertino'),
      ('caResidentialTerritoryCode', ''),
      ('caPostalCode', '95014'),
      ('locationName', ''),
      ('ageConsentTermsOfUse', 'on'),
    ]
    a = s.get('https://www.papajohns.com/', headers=headers)
    if a.status_code == 403:
        print("IP banned, use a VPN/proxy.")
        input("")
        sys.exit()
    a = s.get('https://www.papajohns.com/order/create-account', headers=headers)
    a = s.post('https://www.papajohns.com/order/create-account-page', headers=headers, data=data)
    registered += 1
    header()
    print("Registered account #" + str(registered))
    time.sleep(0.1)
    with open("emails.txt", "a+") as f:
        f.write(email + "\n")