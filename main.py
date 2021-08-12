
### All rights reserved to AMIR SILLAM - 2021

from Uploader import Uploader
from MainMenu import MainMenu

   ## File uploader app --> All rights reserved to AMIR SILLAM ! ##

## User is choosing his menu option of the program.

menu_run = MainMenu()

menu_run.welcome_print()
user_input = menu_run.menu_option()

some_file = Uploader(user_input, str, int)
File1 = Uploader\
    (some_file.random_file_name(user_input),
     user_input,
     some_file.random_file_size(user_input))

print(File1)
print("\n\n### All rights reserved to AMIR SILLAM - 2021")


### All rights reserved to AMIR SILLAM - 2021