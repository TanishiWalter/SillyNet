import time
def getTime():
    timeVar = time.localtime()
    currentTime = time.strftime("1%S", timeVar)
    return(currentTime)

def multiply(num,target):
    a = 0

    for i in target:
        target[a] = i*num
        a += 1
    
    return(target)

def encrypt(message):
    a = 0

    for i in message:
        message[a] = ord(i)
        a += 1
    
    multiply(getTime(),message)
    return(message)

print(encrypt(list("walper")))

        
