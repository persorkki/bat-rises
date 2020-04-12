from enum import Enum
from colorama import Fore, Back, Style

class ReturnCode(Enum):
	SUCCESS     = f"{Fore.GREEN}File was copied successfully!"
	FAIL 	    = "eh"
	NO_SOURCE   = 3
	NOT_OLDER   = f"{Fore.YELLOW}No action because destination is newer"
	USER_CANCEL = f"{Fore.RED} Action was canceled by the user"
	FILE_IN_USE = f"{Fore.RED} File is in use!"
	def get_val(self):
		return self.value