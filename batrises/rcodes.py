from enum import Enum
from colorama import Fore, Back, Style

class ReturnCode(Enum):
	#TODO: rework these
	SUCCESS     = f"{Fore.GREEN}File was copied successfully!"
	#what error is this lol
	FAIL 	    = "fail"
	NO_SOURCE   = "source file doesnt exist"
	NOT_OLDER   = f"{Fore.YELLOW}No action because destination is newer"
	USER_CANCEL = f"{Fore.RED}Action was canceled by the user"
	FILE_IN_USE = f"{Fore.RED}File is in use!"
	def get_val(self):
		return self.value