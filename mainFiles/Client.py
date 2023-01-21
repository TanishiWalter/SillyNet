#This is Client file for project SillyNet.
#This botnet is for Windows targets only, client file cab be used on Linux too, but Server client will not.
#For eduction purposes only.
#Var means variable in this code.
#There will be version with and without explanation of this code. This one is with the explenation.
#Made by Walper.

#Importing
#In this sections, needed packages will be imported.s
import time 
import random 
from colorama import Fore as FORE #This package allows us to write colorful text
import socket #This package is for networking
import os #This package is for interacting with OS (listing files, running commands, etc.)

#definitions
#In This sections, definitions that will be later used in code will be writen.
def printLogo(color1,color2,color3):
    print(color1 + "##########")
    print(color1 + "#" + color2 + "Silly" + color3 + "Net" + color1 + "#")
    print(color1 + "##########")
    print(color1 + "#" + color2 + "by" + color1 + "#" + color2 + "Walper")

def menu(itemList, numVar, color1, color2):
    for i in itemList:
        print(color1 + i + color2 + " [" + str(numVar+1) + "]")
        numVar += 1

def menuSelect(itemList,question):
    itemList[int(input(question))]

def log(logInfo,path):
    with open(path,"a") as file:
        timeVar = time.localtime()
        currentTime = time.strftime("%D %H:%M:%S", timeVar)
        timeStamp = "[" + currentTime + "]"
        file.write("\n" + timeStamp+logInfo)

def readConfig(path,request): #request is variable to store wich information do you want from config, read info.txt for more info
    with open(path,"r") as file:
        configs = file.readlines()
        return(configs[request])

def config(path,newConfigs):
    with open(path,"r+") as file:
        file.truncate()
        file.writelines(newConfigs)

def getTime():
    timeVar = time.localtime()
    currentTime = time.strftime("%D %H:%M:%S", timeVar)
    return(currentTime)

def printHelp():
    print(FORE.GREEN + "This is help page, if you see this and u didn't select Help option anywhere, it's bug. Report it please.")
    print("If you alredy have botnet made with this tool, select Connect option.")
    print("If you don't have botnet yet, select Setup option.")
    print("If you want to config this tool, select Config.")
    print("If yo uwant to exit tool, select stop.")
    print(FORE.RESET)

def exitTool():
    print("Process killed, exit code: 00")
    quit()

def notDoneYet():
    print(FORE.RED + "Not done yet")
                          
#main
#This is where all the code starts, it's made in definitions to prevent from executing the code while being imported
def Client():
    connectedStatus = [False,0]
    exitCode1 = 1 #Explanation of exit codes can be found in info.txt or on github page
    exitCode = 1

    printLogo(FORE.YELLOW,FORE.RED,FORE.GREEN)
    for i in range(5):
        print("\n")
    
    if readConfig("systemFiles/configs.txt",0) == "logs_path=systemFiles/logs.txt\n":
        print(FORE.GREEN + "[" + getTime() + "]" + FORE.CYAN + " [INFO] " +FORE.RESET + " Log path is set on default.")
    else:
        print(FORE.GREEN + "[" + getTime() + "]" + FORE.YELLOW + " [WARNING] " + " Log path is set to custom, this might not work!")
    if readConfig("systemFiles/configs.txt",1) == "systemFile_path=systemFiles/systemFile.json":
        print(FORE.GREEN + "[" + getTime() + "]" + FORE.CYAN + " [INFO] " + FORE.RESET + " System file path is set on default")
    else:
        print(FORE.GREEN + "[" + getTime() + "]" + FORE.YELLOW + " [WARNING] " + " System file path is set to custom, this might not work!")
    
    def mainMenu():
        menu(["Help","Connect","Setup","Config","Stop"],0,FORE.GREEN,FORE.CYAN)
        selectionVar = input("[" + getTime() + "] " + str(connectedStatus) + "> ")
        [printHelp,notDoneYet,notDoneYet,notDoneYet,notDoneYet,exitTool][int(selectionVar)]()
        mainMenu()
    mainMenu()

    

if __name__ == "__main__": #This line checks if the code is executed alone or it's imported in somewhere else
    Client()
