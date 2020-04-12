from colorama import Fore, Back, Style, init

init(autoreset=True)

def out(l, f, v):
    print (f"{Fore.BLUE}-> send {l} {v}")
    print (f"{Fore.GREEN}<- download {f} {v}\n")

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
        