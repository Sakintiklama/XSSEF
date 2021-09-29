# XSSEF
 Cross Site Scripting Vulnerability Exploitation Freamwork
 Authenticated & Unauthenticated POST,GET,HTTPHEADER xss exploitation & session stealing freamwork.
 In order to use it, you must be registered to the Freamwork System.
 
 It is for educational purposes only. In case of abuse, the user is responsible.
 
 
 # USAGE BOOK 
 
### POST VALUE EXPLOITATION
   
  Unauthenticated POST Value Exploitation :
  
  `python xssef.py -t [TARGET URL] -u [FREAMWORK USERNAME] -p [VULNERABLE POST VALUE]`
  
  Authenticated POST Value Exploitation :
  
  `python xssef.py -t [TARGET URL] -u [FREAMWORK USERNAME] -p [VULNERABLE POST VALUE] -c [PHPSESSION ID FOR AUTHENTICATION]`
