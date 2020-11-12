#! /usr/bin/python3

def hundredToText(num,numberCollection,arr,kotiTakarBepar):
    returnString = ''
    if len(str(abs(num))) == 3: # hundred sequence
        returnString = ''
        st = str(num)
        st2 = int (st[1] + st[2])
        print("value: ",st[0])
        for x in numberCollection:
            if int(st[0]) == x:
                returnString = arr[x - 1]+' '+kotiTakarBepar[0]
            if int (st2) == x:
                returnString += ' ' + arr[x-1]
        
    return returnString

def numToText(num):
    numberCollection = []
    numToText = ''
    kotiTakarBepar = ['hundred','thousand','lakh','cror']
    fp = open("text.txt","r")
    numToText = fp.read()
    arr = numToText.split('\n') # So got the number text

    for x in range(1,101):
        numberCollection.append(x)
    
    # Now let's create the algorithm

    if len(str(abs(num))) < 3:
        for x in numberCollection:
            if x == num:
                print(arr[x - 1])
                break
    elif len(str(abs(num))) == 3: # hundred sequence
        returnString = ''
        st = str(num)
        st2 = int (st[1] + st[2])
        print("value: ",st[0])
        for x in numberCollection:
            if int(st[0]) == x:
                returnString = arr[x - 1]+' '+kotiTakarBepar[0]
            if int (st2) == x:
                returnString += ' ' + arr[x-1]
        print (returnString.upper())
    elif len(str(abs(num))) == 4:
        returnString = ''
        st = str(num)
        st1 = st[0]
        st2 = st[1]
        st3 = st[2]
        st4 = st[3]
        st5 = int(st2 + st3 + st4)
        for x in numberCollection:
            if x == int(st1):
                returnString += arr[x - 1]+ ' ' + kotiTakarBepar[1]
        ret = hundredToText(st5,numberCollection,arr,kotiTakarBepar)
        returnString += ' ' + ret
        print(returnString)
    elif len(str(abs(num))) == 5:
        returnString = ''
        
        st = str(num)
        st1 = st[0] + st[1]
        st2 = st[2]
        st3 = st[3]
        st4 = st[4]
        st5 = int(st2 + st3 + st4)

        for x in numberCollection:
            if x == int(st1):
                returnString += arr[x - 1] + ' ' + kotiTakarBepar[1]
        ret = hundredToText(st5,numberCollection,arr,kotiTakarBepar)
        returnString += ' ' + ret
        print(returnString)
    elif len(str(abs(num))) == 6:
        returnString = ''

        st = str(num)
        st1 = st[0]
        st2 = st[1] + st[2]
        st3 = int(st[3] + st[4] + st[5])

        for x in numberCollection:
            if x == int(st1):
                returnString += arr[x - 1] + ' ' + kotiTakarBepar[2]
            if x == int(st2):
                returnString += ' ' + arr[x - 1] + ' ' + kotiTakarBepar[1]

        ret = hundredToText(st3,numberCollection,arr,kotiTakarBepar)
        returnString += ' ' + ret
        print(returnString)

'''
    elif len(str(abs(num))) == 4 or len(str(abs(sum))) == 5: # handling the thousand section
        returnString = ''
        st = str(num)
        # we have to split the value in 3 part in case of thousand 
        if (len(str(abs(num))) == 4:
                # thousand not more than 9999
                st0 = st[0] # first digit
                st1 = st[1]
                st2 = st1 + st[2] + st[3]
                for x in numberCollection:
                    if x == int(st0):
                        returnString += arr[x-]
'''
if __name__ == "__main__":
    inpu = input ("Enter the number that you want to use : ")

    print(numToText(int(inpu))) # problem is it's work until it's reach it range 100 then the entire part will be undefined !
