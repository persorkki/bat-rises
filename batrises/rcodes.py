from enum import Enum
from colorama import Fore, Back, Style

class ReturnCode(Enum):
	#TODO: rework these
	SUCCESS     = f"{Fore.CYAN}SUCCESS"
	#what error is this lol
	FAIL 	    = f"{Fore.RED}FAIL"
	NO_SOURCE   = f"{Fore.RED}NO SOURCE"
	NOT_OLDER   = f"{Fore.YELLOW}NO ACTION"
	USER_CANCEL = f"{Fore.RED}CANCEL"
	FILE_IN_USE = f"{Fore.RED}IN USE"
	def get_val(self):
		return self.value