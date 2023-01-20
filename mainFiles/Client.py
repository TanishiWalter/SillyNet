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
        print(color1 + i + color2 + "[" + str(numVar+1) + "]")
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
        print(configs)
        return(configs[request])

def config(path,newConfigs):
    with open(path,"r+") as file:
        file.truncate()
        file.writelines(newConfigs)
                          
#main
#This is where all the code starts
