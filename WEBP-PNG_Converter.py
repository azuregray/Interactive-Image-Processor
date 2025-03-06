'''
=================================================================================================================== DOCUMENTATION STARTS HERE
:: AUTHOR :::::: D A R S H A N   S (GitHub/azuregray)
You can find this script origin here :: https://github.com/azuregray
===================================================================================================================
REPOSITORY :: https://github.com/azuregray/WEBP-to-PNG-Converter

LIBRARIES USED: os, PIL.Image, time.sleep, tkinter.filedialog

CALLABLE FUNCTIONS: askForUserChoice() -> userChoice:int; webpToPngConverter(userChoice:int) -> processedFiles:List;

LINES OF CODE = 14(Documentation) + 1 + 82(Code) + 1
=================================================================================================================== DOCUMENTATION ENDS HERE
'''

import os
from time import sleep
import tkinter.filedialog as fd
from PIL import Image

def askForUserChoice():
    os.system('cls')
    sleep(1)
    print('\nSo, in what way are the WEBP Images stored?')
    print('1. Stored in a Single directory.') #askopenfilenames
    print('2. Stored in Multiple Directories') # askdirectory, multiple
    print('3. Search recursively from a root directory.') # askdirectory + os.walk()
    print('Otherwise, Press [Ctrl + C] to Exit! Thanks for trying the code❤️')
    userChoice = input('\n =============== Please Enter your choice :: ')
    return userChoice

def webpToPngConverter(userChoice):
    processedFiles = []
    
    if userChoice == 1: #askopenfilenames
        os.system('cls')
        print('============= Please select input files in the popup that appears! =============')
        sleep(0.8)
        response = fd.askopenfilenames(title='Choose WEBP Files', filetypes=[('WEBP Images', '*.webp'), ('All Files', '*.*')]) # Need specific types.
        processedFiles = list(response)
        for item in processedFiles:
            im = Image.open(item).convert("RGB")
            savableName = item[:-4] + '.png'
            im.save(savableName, "png")
            print('\nSaved ', savableName)
    elif userChoice == 2: # askdirectory, multiple
        os.system('cls')
        print('============= Please select input files in the popup that appears! =============')
        sleep(0.8)
        directories = fd.askdirectory(title='Please select all the directories that contain your WEBP files.', multiple=True)
        for directory in directories:
            for filename in directory:
                if filename[-3:].lower() == 'webp':
                    file_path = os.path.join(root_dir, filename)
                    processedFiles.append(file_path)
                    im = Image.open(file_path).convert("RGB")
                    im.save(file_path[:-4] + '.png', "png")
                    print('\nSaved ', savableName)
    elif userChoice == 3: # askdirectory + os.walk()
        os.system('cls')
        print('============= Please select input files in the popup that appears! =============')
        sleep(0.8)
        response = fd.askdirectory(title='Please select the root directory to start.')
        for root_dir, _, files in os.walk(response):
                for filename in files:
                    if filename[-3:].lower() == 'webp':
                        file_path = os.path.join(root_dir, filename)
                        processedFiles.append(file_path)
                        im = Image.open(file_path).convert("RGB")
                        im.save(file_path[:-4] + '.png', "png")
                        print('\nSaved ', savableName)
    else:
        print('\n\nInvalid Choice! :: Sorry! Try running the script again with a valid choice.')
        exit()
    
    return processedFiles



if __name__ == '__main__':
    userChoice = askForUserChoice()
    filesProcessed = webpToPngConverter(userChoice)
    
    cleanOrNot = input("\n\n [CLEAN SOURCE?] Please type YES to DELETE ALL Processed Input Files, otherwise NO (Default NO) :: ")
    
    if cleanOrNot.lower() == 'yes':
        print('\n[CLEANUP] Deleting all Source files now.')
        for item in filesProcessed:
            os.remove(item)
        print(f'\n {len(filesProcessed)} files have been converted and deleted.\n')
        print('\n\n Thanks for trying out the code. See you!\n')
    elif cleanOrNot == '' or cleanOrNot.lower() == 'no':
        print('\n Source WEBP files are not removed.')
        print('\n\n Thanks for trying out the code. See you!\n')
    else:
        print('\n Invalid Input!')
        print('\n However, Source WEBP files are not removed.')
        print('\n\n Thanks for trying out the code. See you!\n')
