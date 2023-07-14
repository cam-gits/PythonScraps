'''Quick tasklist app run from command line

Commands are (R)ead List, (A)dd item, (D)elete Item, (D)elete (L)ist, (S)ettings and (E)xit'''

import os
import sys


command = 'O'
taskList = 'tasklist.txt'
print("Cam's Tasklist\n")
print("Current list location: {} Update in (S)ettings".format(taskList))


while command:

    # input command, no validation, validation through if/else in body
    command = input("Select an option to begin: ").upper()
    items = 0

    
    # loop for reading line items on the list and printing to console, with counter to verify completion
    if command == 'R':
        print("Fetching list...")
        if os.path.isfile(taskList):
            readFile = open(taskList,'r')
            for line in readFile:
                if type(line.strip()) == str:
                    print(line,end='')
                    items = items +1
            print()
            print('{} Items on Tasklist'.format(items))
            readFile.close()
        else:
            print("You have no tasklist at {}".format(taskList))
            
    # the below deals with writing an item to the list as a new line, if no file exists one will be created
    elif command == 'A' or command == 'W':
        try:
            if os.path.isfile(taskList):
                writeFile = open(taskList,'a')
            else:
                writeFile = open(taskList,'w')

            toLog = input('What would you like to add: ').title()
            writeFile.write(toLog+'\n')
            writeFile.close()
        except:
            print('The filepath {} is not valid, please update it in settings (S)'.format(taskList))

    # deletes tasks containing user inputted string 
    elif command == 'D':
        print('All tasks containing the specified text will be deleted')
        dropLine = input('Specify text: ')
        with open(taskList,'r') as readFile:
            lines = readFile.readlines()
        with open(taskList,'w') as writeFile:
            for line in lines:
                if dropLine.upper() not in line.strip('\n').upper():
                    writeFile.write(line)
                    items = items + 1
        print('Items containing "{}" have been removed, if any ever existed...\n{} list items remaining'.format(dropLine, items))

    # decision path to deleting the whole file
    elif command == 'DL':
        print("You have chosen to DELETE THE ENTIRE LIST, are you sure? (Y/N)")
        print("This cannot be undone")
        delList = input().upper()
        try:
            if delList == 'Y' and os.path.isfile(taskList):
                os.remove(taskList)
                print('The task list has been deleted')
            elif delList == 'N':
                print('File retained, returning to main')
            elif os.path.isfile(taskList) != True:
                print('There is no current tasklist to remove')
            else:
                print("I don't recognise this command.")
                print('File retained, returning to main')
        except:
            print('The filepath {} is not valid, please update it in settings (S)'.format(taskList))

    # option to change file location
    elif command == 'S':
        changePath = input('Would you like to change the location of your tasklist? (Y/N): ').upper()
        if changePath == 'Y':
            taskList = input('Enter location in the format C:\dir\\filename.txt:\n')
            print('Tasklist located at {} for duration of session'.format(taskList))
        elif changePath == 'N':
            print('No change made to tasklist location {}'.format(taskList))
        else:
            print('Invalid Option. Returning to Main')

    # exit programme
    elif command == 'E':
        print("Goodbye")
        break

    # unrecognised command
    else:
        print("\nThis is not a valid option.\n")
        print("Commands for this programme are: \nRead List (R)\nAdd Item (A or W)\nDelete Item (D)\nDelete List (DL)\nSettings (S)\nExit App (E)\n")
        command = 'O'

sys.exit()
