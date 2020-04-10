from enum import Enum
import colorama

class ReturnCode(Enum):
	SUCCESS     = f"{colorama.Fore.GREEN}File was copied successfully!"
	FAIL 	    = "eh"
	NO_SOURCE   = 3
	NOT_OLDER   = f"{colorama.Fore.YELLOW}No action because destination is newer"
	USER_CANCEL = "Action was canceled by the user"
	def get_val(self):
		return self.value