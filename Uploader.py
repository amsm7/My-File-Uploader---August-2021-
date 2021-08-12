### All rights reserved to AMIR SILLAM - 2021

import colorama
import random

from colorama import Fore


class Uploader:
    def __init__(self, file_name, file_type, file_size):
        self.file_name = file_name
        self.file_type = file_type
        self.file_size = file_size

    ## Create random file names for the documents / images.
    def random_file_name(self, file_type):
        Pic_list = ["Cyber Security Certificate", "Python Certificate",
                    "Candidate cover letter", "Additional Certificate",
                    "REST API with Python Certificate", ]

        Pdf_list = ["CV - Java Developer", "CV - Python Developer",
                    "CV - IT Specialist", "CV - Security Analyst",
                    "Linux Specialist"]

        if file_type == "PDF":
            return (random.choice(Pdf_list + Pic_list))

        return (random.choice(Pic_list))

    ## Create random file sizes for the documents / images.
    def random_file_size(self, file_type):
        if file_type == "PDF":
            self.file_size = random.randint(250, 900)

        else:
            self.file_size = random.randint(1000, 3000)

        return self.check_size(file_type, self.file_size)

    ## Checks the file size uploaded by the user
    ## and continues or stops the operation accordingly.
    def check_size(self, file_type, file_size):
        if file_type == "PDF":
            if (self.file_size > 500) or (self.file_size < 200):
                print(f"\nSize of the file is {file_size} KB.")
                exit("PDF files size should be between 200 and 500 KB.\n"
                     "The program is quiting automatically, try uploading again.")

        else:
            if (self.file_size > 2000) or (self.file_size < 1000):
                print(f"\nSize of the file is {file_size} KB.")
                exit("JPG/PNG files size should be between 1000 and 2000 KB.\n"
                     "The program is quiting automatically, try uploading again.")

        return file_size

    ## Print user's file properties.
    def __str__(self):
        return (Fore.LIGHTBLUE_EX + f"\nDetails of the file you chose to upload: "
                           f"\n--------------------------------\n"

                           f"File name is: {self.file_name}. \n"
                           f"File type is: {self.file_type}. \n"
                           f"File size is: {self.file_size} Kb.\n"

                           f"--------------------------------\n"
                           f"0 --- 23% ---- 51% --- 67% --- 83% --- 100% \n\n"
                           f"The file was uploaded successfully !\n"
                           f"Thanks for using our app, we appreciate it!")

### All rights reserved to AMIR SILLAM - 2021
