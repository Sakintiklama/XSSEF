# XSSEF
 Cross Site Scripting Vulnerability Exploitation Freamwork
 Authenticated & Unauthenticated POST,GET,HTTPHEADER xss exploitation & session stealing freamwork.
 In order to use it, you must be registered to the Freamwork System.
 
 It is for educational purposes only. In case of abuse, the user is responsible.
 
 
 # USAGE BOOK 
 
 ### POST VALUE EXPLOITATION
   
  Unauthenticated POST Value Exploitation :
  
  `python xssef.py -t [TARGET URL] -u [FREAMWORK USERNAME] -p [VULNERABLE POST PARAMETHER]`
  
  Authenticated POST Value Exploitation :
  
  `python xssef.py -t [TARGET URL] -u [FREAMWORK USERNAME] -p [VULNERABLE POST PARAMETHER] -c [PHPSESSION ID FOR AUTHENTICATION]`
  
  
  
  ### GET VALUE EXPLOITATION
   
  Unauthenticated GET Value Exploitation :
  
  `python xssef.py -t [TARGET URL] -u [FREAMWORK USERNAME] -g [VULNERABLE GET PARAMETHER]`
  
  Authenticated GET Value Exploitation :
  
  `python xssef.py -t [TARGET URL] -u [FREAMWORK USERNAME] -g [VULNERABLE GET PARAMETHER] -c [PHPSESSION ID FOR AUTHENTICATION]`
  
  
  
  
  
  ### HTTP HEADER VALUE EXPLOITATION
   
  Unauthenticated HTTP HEADER Value Exploitation :
  
  `python xssef.py -t [TARGET URL] -u [FREAMWORK USERNAME]`
  
  Authenticated HTTP HEADER Value Exploitation :
  
  '''python xssef.py -t [TARGET URL] -u [FREAMWORK USERNAME] -c [PHPSESSION ID FOR AUTHENTICATION]'''
  
  
  
