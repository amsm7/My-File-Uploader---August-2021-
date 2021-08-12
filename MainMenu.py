import re

### All rights reserved to AMIR SILLAM - 2021
from colorama import Fore
from termcolor import colored


class MainMenu:

  def __init__(self):
        pass


  ## Print opening message.
  def welcome_print(self):
      print(Fore.LIGHTBLACK_EX + "\n\t\tHello and welcome to our 'File Uploader App'.\n")
      self.menu_print()


  ## Print menu displayed for the user.
  def menu_print(self):
      print("Dear user, please enter your choice from the options in the menu below.\n"
            "-------------------------------------------------------------\n"
            " 1: [PDF]\n 2: [JPG]\n 3: [PNG]\n \n"
            "-------------------------------------------------------------")

      print(colored(
            "---------------------------------------------------------\n"
            " \t\t* Size of PDF files - from 200 KB to 500 KB.\n"
            " \t\t* Size of JPEG/PNG files - from 1 MB to 2 MB.\n"
            "---------------------------------------------------------\n" ,
          'white' , 'on_blue'))

  ## Checking user menu input correctness.
  def menu_option(self, ):
    counter = 0
    user_input =(input("\t\t\t\t\t  "
                       "Your option is: "))

    ## Handling numbers and all types of characters
    ## that are different from 1, 2 and 3.
    while not re.match("^[1-3]*$", user_input)\
            or (len(user_input) > 1):
        exit("\nYour files are important to us so there is only one upload attempt,"
             " \nplease restart the app and try again.\n\n"
             "We appreciate your patience and understanding,\n"
             "thanks and have a good day!")

    return self.menu_option_convertor(file_type_num = user_input)


  ## Get menu option from the user and return the 'real type' of it.
  def menu_option_convertor(self, file_type_num):
    file_type = ''
    if file_type_num =="1":
        file_type = "PDF"
    elif file_type_num =="2":
        file_type = "JPG"
    else:
        file_type ="PNG"

    return file_type


### All rights reserved to AMIR SILLAM - 2021

































