import os
import fnmatch
import time
from datetime import datetime
from os import path

def Menu(): #main menu
    print(user_name + """,  what do you want to do?
                            press 1 to work with file
                            press 2 to work with directory
                            press 3 to change your current directory
                            press 0 to go back/exit""")

def FileMenu(): #menu for files options
    print("""
                            press 1 to delete file
                            press 2 to rename file
                            press 3 to add content to this file
                            press 4 to rewrite content of this file
                            press 5 to return to the parent directory
                            press 0 to go back""")

def DirMenu(): #menu for directories options
        print("""
                            press 1 to rename directory
                            press 2 to print number of files in it
                            press 3 to print number of directories in it
                            press 4 to list content of the directory
                            press 5 to add file to this directory
                            press 6 to add new directory to this directory""")


print("                     Welcome to File Manager!")
print("                     What is your name?")
user_name = str(input())
while True:
    Menu()
    location = int(input())
    curpath = os.getcwd() # current location 
    print(curpath)
    
    if location == 1: #for files
        FileMenu()
        n = int(input()) #choose the option for file
        if n == 0:
            continue

        if n == 1: #option_1 = 1 - delete file
            file_del = input('Enter the name of the file you want to delete: ')
            if os.path.exists(file_del + '.txt'):
                os.remove(curpath + '/' + file_del + '.txt')
                print("Okay. File removed!")
                continue
            else:
                print("The file does not exist in this directory")
                continue

        elif n == 2: #option_2 = '2 - rename file'
            file_rename = input('Enter the name of file you want to rename: ')
            if os.path.exists(file_rename + '.txt'):
                print('How do you want to rename it?')
                new_name = input()
                os.rename(file_rename + '.txt', new_name + '.txt')
                print("Okay. File renamed!")   
                continue
            else:
                print("The file does not exist in this directory.")
                continue

        elif n == 3: #option_3 = '3 - add content to this file
            file_addcon = input('Enter the name of file to add content: ')
            if os.path.exists(file_addcon + '.txt'):
                curFile = open(file_addcon + '.txt', 'a')
                new_content = str(input("What content do you want to add? "))
                curFile.write(new_content)
                curFile.close()
                print("Okay. New contect added to file!")
                continue
            else:
                print("The file does not exist in thid directory.")
                continue

        elif n == 4: #option_4 = '4 - rewrite content of this file'
            file_rewrite = input('Enter the name of file to rewrite content: ')
            if os.path.exists(file_rewrite + '.txt'):
                curFile = open(file_rewrite + '.txt', 'w')
                rewrite_content = input("What do you want to rewrite?")
                curFile.write(rewrite_content)
                curFile.close()
                print("Okay. Content rewritten.")
                continue
            else:
                print("The file does not exist in this directory.")
                continue

        elif n == 5: #option_5 = '5 - return to the parent directory'
            parentDir = os.path.dirname(os.getcwd())
            os.chdir(parentDir)
            print('Your parent directory is ' + parentDir)
            continue


    elif location == 2:  #for directory
        DirMenu()
        curDir = os.getcwd()
        print('Yout current directory is ' + curDir)
        c = int(input())

        if c == 1: #'1 - rename directory'
            dir_rename =  input('Enter the name of directory you want to rename: ')
            if os.path.exists(dir_rename):
                new_dir_name = input('Enter a new name for your directory: ')
                os.rename(dir_rename, new_dir_name)
                print('Done. Directory successfully renamed.')
                continue
            else:
                print('Directory does not exist')
                continue

        elif c == 2: #'2 - print number of files in it'
            dir_files = input('Enter the name of directory to print number of files: ')
            if os.path.exists(dir_files):
                dir_list = os.listdir(dir_files)
                num_files = len([1 for x in list(os.scandir(dir_files)) if x.is_file()])
                print('There are ' + str(num_files) + ' files in your directory!')
                continue
            else:
                print('Directory does not exist')
                continue
            
        elif c == 3: #3 - print number of directories in it
            dir_dir = input ('Enter the name of directory to print number of directories: ')
            if os.path.exists(dir_dir):
                num_dir = len([1 for x in list(os.scandir(dir_dir)) if x.is_dir()])
                print('There are ' + str(num_dir) + ' directories in your directory!')
                continue
            else:
                print('Directory does not exist')
                continue

        elif c == 4: #4 - list content of the directory
            dir_content = input('Enter the name of directory to list content: ')
            if os.path.exists(dir_content):
                all_dir = os.listdir(dir_content)
                print(all_dir)
                continue
            else:
                print('Directory does not exist')
                continue

        elif c == 5: #5 - add file to this directory
            file_name = input("Enter the name for new file: ")
            curFile = open(file_name + '.txt', 'w')
            print('File was added to this directory.')
            continue

        elif c == 6: #6 - add new directory to this directory
            dir_name = input('Enter the name for new directory: ')
            os.mkdir(dir_name)

    elif location == 0:
        print("Thanks. Bye!")
        time.sleep(1)
        break

    elif location == 3:
        curpath = os.getcwd()
        os.chdir("..")
        print(os.getcwd())