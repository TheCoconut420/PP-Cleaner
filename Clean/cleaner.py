from cmath import log
import imp
import os
import logging
import random


logging.basicConfig(filename='cleaner.log', 
                    level=logging.DEBUG, 
                    format='%(asctime)s %(message)s', 
                    filemode='w')


class Cleaner:
    def __init__(self, file):                                   # Constructor
        self.file = file                            
        self.png = "89504E470D0A"                               # Magic number for PNG
        self.gif = "474946383961"                               # Magic number for GIF
        self.jpg = "FFD8FFE00010"                               # Magic number for JPG
        self.extension = ""                     

    def get_hex(self, file):                                    # Get hexadecimal value of file
        with open(file, "rb") as file:
            f = file.read(6)
            self.hex = f.hex().upper()

    def check_extension(self):                                  # Check file extension
        if self.hex == self.png:
            if not self.file.endswith(".png"):
                self.extension = ".png"
                self.change_extension()
        elif self.hex == self.gif:
            if not self.file.endswith(".gif"):
                self.extension = ".gif"
                self.change_extension()
        elif self.hex == self.jpg:
            if not self.file.endswith(".jpg"):
                self.extension = ".jpg"
                self.change_extension()

    def change_extension(self):                                 # Change file extension
        if self.extension == ".png":
            logging.info(f"{self.file} restored to a .png file")
            base = os.path.splitext(self.file)[0]
            os.rename(self.file, base + ".png")
        elif self.extension == ".gif":
            logging.info(f"{self.file} restored to a .gif file")
            base = os.path.splitext(self.file)[0]
            os.rename(self.file, base + ".gif")
        elif self.extension == ".jpg":
            logging.info(f"{self.file} restored to a .jpg file")
            base = os.path.splitext(self.file)[0]
            os.rename(self.file, base + ".jpg")
    
    def set_up(self):                                           # Set up
        self.file_list_location = []
        self.file_list = []
        for root, dirs, files in os.walk(self.file):
            for file in files:
                self.file_list_location.append(os.path.join(root, file))
                self.file_list.append(file)

    def run(self):
        self.set_up()
        for i in range(len(self.file_list_location)):
            self.file = self.file_list_location[i]
            self.get_hex(self.file)
            self.check_extension()


class Corupter:
    def __init__(self, file):                                   # Constructor
        self.file = file

    def set_up(self):                                           # Set up
        self.file_list_location = []
        self.file_list = []
        for root, dirs, files in os.walk(self.file):
            for file in files:
                self.file_list_location.append(os.path.join(root, file))
                self.file_list.append(file)
                
    def corupt_extensions(self):
        n = 0
        for i in range(len(self.file_list_location)):
            if self.file_list[i].endswith(".png") or self.file_list[i].endswith(".gif") or self.file_list[i].endswith(".jpg"):
                base = os.path.splitext(self.file)[0]
                logging.info(f"{self.file_list[i]} has been corrupted")
                os.rename(self.file_list_location[i], base + ".corrupt" + str(n))
                n += 1
            else:
                logging.info(f"{self.file_list[i]} has not been corrupted")

    def run(self):
        self.set_up()
        self.corupt_extensions()

if __name__ == "__main__":
    logging.info("Started")
    choose = input("Do you want to restore or corrupt files? (r/c) ")
    path = r"C:\Users\stefa\OneDrive\Dokumente\GitHub\PP-Cleaner\Clean"
    if choose == "r":
        clean = Cleaner(path)
        clean.run()
    elif choose == "c":
        corupter = Corupter(path)
        corupter.run()
    else:
        print("Invalid input")
        logging.info("Invalid input by the user")
        logging.info(f"'{choose}' was entered")
    logging.info("Finished")