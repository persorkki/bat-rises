from colorama import Fore, Back, Style, init
from .rcodes import *

init(autoreset=True)

clr = { "<- download" : Fore.GREEN,
        "-> send"     : Fore.BLUE, }
def endlog(endlog):
    downloads, sends = 0, 0
    for x in endlog:
        if x['operation'] == '<- download' and x['result'] == ReturnCode.SUCCESS: downloads += 1
        if x['operation'] == '-> send'and x['result'] == ReturnCode.SUCCESS: sends += 1
    print ("Successful send operations ", sends)
    print ("Successful download operations ", downloads, "\n")

def out(op_file, operation, result):
    
    print (f"{clr[operation]}{operation} {op_file} {result}")
    #print (f"{Fore.GREEN}<- download {f} {v}\n")

def question_override(src, dst):
    print (f"\n{Fore.RED}OVERRIDE QUESTION ")
    print (f"file is not in logs or it was not modified by us")
    print (f"proceed copying {Fore.BLUE}{Back.WHITE}SRC{Style.RESET_ALL} to {Fore.WHITE}{Back.BLUE}DST{Style.RESET_ALL}?")
    
    print (f"SRC:	{Fore.BLUE}{Back.WHITE}{src}{Style.RESET_ALL}")
    print (f"DST:	{Fore.WHITE}{Back.BLUE}{dst}{Style.RESET_ALL}")
    
    while (True):
        print ("1. Yes, override")
        print ("2. No, do nothing")
        x = input(">")
        if x == "1":
            return True
        elif x == "2":
            return False
        