import os
from colorama import Fore, Back, Style, init
from .rcodes import *

init(autoreset=True)

# EDIT THESE COLORS
clr = { "<- download" : Fore.GREEN,
        "-> send"     : Fore.BLUE, 
        "src_Fore"    : Fore.BLUE,
        "src_Back"    : Back.WHITE,
        "dst_Fore"    : Fore.WHITE,
        "dst_Back"    : Back.BLUE,
        "positive"    : Fore.GREEN,
        "negative"    : Fore.RED,}

def clear(name):
    if name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

def endlog(endlog):
    downloads, sends = 0, 0
    for x in endlog:
        if x['operation'] == '<- download' and x['result'] == ReturnCode.SUCCESS: downloads += 1
        if x['operation'] == '-> send'and x['result'] == ReturnCode.SUCCESS: sends += 1
    print ("Successful send operations ", sends)
    print ("Successful download operations ", downloads, "\n")

def out(op_file, operation, result):
    print (f"{clr[operation]}{operation} {op_file} {result}")


def question_override(src, dst):
    print (f"\n{Fore.RED}OVERRIDE?")
    print (f"file is not in logs or it was not modified by us")
    print (f"proceed copying {clr['src_Fore']}{clr['src_Back']}SRC{Style.RESET_ALL} to {clr['dst_Fore']}{clr['dst_Back']}DST{Style.RESET_ALL}?")
    
    print (f"SRC:	{clr['src_Fore']}{clr['src_Back']}{src}{Style.RESET_ALL}")
    print (f"DST:	{clr['dst_Fore']}{clr['dst_Back']}{dst}{Style.RESET_ALL}")
    
    while (True):
        print (f"{clr['positive']}1. Yes, override")
        print (f"{clr['negative']}2. No, do nothing")
        x = input(">")
        if x == "1":
            return True
        elif x == "2":
            return False
        