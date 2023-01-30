import time
import random

def getTime():
    timeVar = time.localtime()
    currentTime = time.strftime("1%H", timeVar)
    return(currentTime)

def multiply(num,target):
    a = 0

    for i in target:
        target[a] = i*num
        a += 1
    
    return(target)

def encrypt(message,key):
    a = 0

    for i in message:
        message[a] = ord(i)
        a += 1

    multiply(key,message)
    message.append(key)
    return(list(message))

def decrypt(key,encriptedWord):
    
    a = 0
    b = 0

    for i in encriptedWord:
        a = float(i)/int(key)
        encriptedWord[b] = a
        b +=1
    
    a = 0
    b = 0

    for i in encriptedWord:
        a = chr(int(i))
        encriptedWord[b] = a
        b += 1

    return(encriptedWord)

def getBiggestAndSmallest(lst):
    return [min(lst), max(lst)]

def mixRandomNumbers(toBeMixed):
    returnVar = []
    for i in toBeMixed:
        if i > random.randint(getBiggestAndSmallest(toBeMixed)[0],getBiggestAndSmallest(toBeMixed)[1]):
            returnVar.append(random.randint(getBiggestAndSmallest(toBeMixed)[0],getBiggestAndSmallest(toBeMixed)[1]))
            returnVar.append(i)
            continue
        else:
            returnVar.append(i)
            continue
    return(returnVar)

key = int(getTime()) - 16
encrypted = encrypt(list("walper"),key)
encrypted = mixRandomNumbers(encrypted)
print(encrypted)
decrypted = decrypt(key,encrypted)
print(decrypted)