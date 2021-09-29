import os

def Clear():
    if os.name == "nt":
	    os.system("cls")
    else:
	    os.system("clear")


def Banner():
    Clear()
    print("""

          _______  _______  _______  _______ 
|\     /|(  ____ \(  ____ \(  ____ \(  ____ |
( \   / )| (    \/| (    \/| (    \/| (    \/
 \ (_) / | (_____ | (_____ | (__    | (__    
  ) _ (  (_____  )(_____  )|  __)   |  __)   
 / ( ) \       ) |      ) || (      | (      
( /   \ )/\____) |/\____) || (____/\| )      
|/     \|\_______)\_______)(_______/|/       


[ Cross Site Scripting Exploit Freamwork ]



""")