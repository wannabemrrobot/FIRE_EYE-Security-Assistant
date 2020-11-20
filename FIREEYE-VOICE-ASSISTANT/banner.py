from colorama import Back, Fore, Style
import time

def display():

    print(Fore.BLUE + '''
           . "  \  \   /  /  " .
         ,  \                 /  .
       . \   _,.--~=~"~=~--.._   / .
      ;  _.-"  / \ !   ! / \  "-._  .
     / ,"     / ,` .---. `, \     ". 
    /.'   `~  |   /:::::\   |  ~`   '.
    \`.  `~   |   \:::::/   | ~`  ~ .'/
     \ `.  `~ \ `, `~~~' ,` /   ~`.' /
      .  "-._  \ / !   ! \ /  _.-"  .
       ./    "=~~.._  _..~~=`"    \.
         ,/         ""          \,
           . _/             \_ .
              " - ./. .\. - "
    ''')

    print(Fore.RED + '''
     (     (    (                  )       
     )\ )  )\ ) )\ )            ( /(       
    (()/( (()/((()/( (    (     )\()) (    
     /(_)) /(_))/(_)))\   )\   ((_)\  )\   
    (_))_|(_)) (_)) ((_) ((_) __ ((_)((_)  
    | |_  |_ _|| _ \| __|| __|\ \ / /| __| 
    | __|  | | |   /| _| | _|  \ V / | _|  
    |_|   |___||_|_\|___||___|  |_|  |___| 

    ''')
    print(Fore.RED + "    ======================================")
    print(Fore.CYAN + "     A VIRTUAL SECURITY ASSISTANT FOR WEB \n"
          "      APP VULNERABILITY DETECTION & LINUX \n"
          "          SYSTEM SECURITY AUDITING")
    print(Fore.WHITE + "              Design and Code By")
    print(Fore.GREEN + "             PAVITHRA  SRINIVASAN")
    print(Fore.RED + "    ======================================\n")
    print("[+]" + Style.RESET_ALL + " FireEye is Ready!...")
    print("")
    time.sleep(2)
#display()