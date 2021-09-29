# XSSEF
 Cross Site Scripting Vulnerability Exploitation Freamwork
 Authenticated & Unauthenticated POST,GET,HTTPHEADER xss exploitation & session stealing freamwork.
 In order to use it, you must be registered to the Freamwork System.
 
 It is for educational purposes only. In case of abuse, the user is responsible.
 
 
 1)- [USAGE BOOK](https://github.com/ringzerofy/XSSEF#usage-book)
 
 2)- [REQUIREMENTS](https://github.com/ringzerofy/XSSEF#requirements)
 
 3)- [DOWNLOAD AND INSTALLATION](https://github.com/ringzerofy/XSSEF#download--installation)
 
 4)- [PARAMETHERS AND WORKS](https://github.com/ringzerofy/XSSEF#paramethers--works)
 
 
 
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

 ### DOWNLOAD & INSTALLATION
 
  ```
  $ git clone https://github.com/ringzerofy/XSSEF.git
  $ cd XSSEF-master
  $ chmod 777 * (Linux)
  $ python xssef.py --help
  
  ```
 
 
### PARAMETHERS & WORKS
 
 ```
 --user [-u] -> Freamwork Usrname
 --target [-t]  -> (VULNERABLE) TARGET URL
 
 --post [-p] -> VULNERABLE POST PARAMETHER
 --get [-g] -> VULNERABLE GET PARAMETHER
 --cookie [-c] -> COOKI FOR AUTHENTICATIONS (FOR AUTHENTICATED VULNERABILITIES)
 
 ``` 
 
 
 
 ### REQUIREMENTS
 ```
 Python Version >= 3.0
 
 $pip install -m requests
 $pip install -m argparse
 
 XXEF Freamwork Account
 
 ```
 
 
 # USAGE BOOK 
 
 ### [POST] PARAMETHER EXPLOITATION
   
  ``` 
  Unauthenticated POST Value Exploitation :
  
  $ python xssef.py -t [TARGET URL] -u [FREAMWORK USERNAME] -p [VULNERABLE POST PARAMETHER]
  
  Authenticated POST Value Exploitation :
  
  $ python xssef.py -t [TARGET URL] -u [FREAMWORK USERNAME] -p [VULNERABLE POST PARAMETHER] -c [PHPSESSION ID FOR AUTHENTICATION]
  
  ```
  
  
  ### [GET] PARAMETHER EXPLOITATION
  
  ```
  Unauthenticated GET Value Exploitation :
  
  $ python xssef.py -t [TARGET URL] -u [FREAMWORK USERNAME] -g [VULNERABLE GET PARAMETHER]
  
  Authenticated GET Value Exploitation :
  
  $ python xssef.py -t [TARGET URL] -u [FREAMWORK USERNAME] -g [VULNERABLE GET PARAMETHER] -c [PHPSESSION ID FOR AUTHENTICATION]
  
  ```
  
  
  
  
  ### [HTTP HEADER] PARAMETHER EXPLOITATION
  
  ```
  Unauthenticated HTTP HEADER Value Exploitation :
  
  $ python xssef.py -t [TARGET URL] -u [FREAMWORK USERNAME]
  
  Authenticated HTTP HEADER Value Exploitation :
 
  $ python xssef.py -t [TARGET URL] -u [FREAMWORK USERNAME] -c [PHPSESSION ID FOR AUTHENTICATION]
  
  ```
  

