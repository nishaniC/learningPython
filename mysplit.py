def mysplit(strng):
    mylist = []
    mylistitem = ""
    ch=None
    for ch in strng:
        if ((ch == ' ')and (mylistitem!="")):
            mylist.append(mylistitem)
            mylistitem = ""
        elif ((ch != ' ')and (ch!=None)):
            mylistitem+=ch
        
    if ((ch != ' ')and (mylistitem!="")):
        mylist.append(mylistitem)
        return mylist
    else:
        return mylist


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
