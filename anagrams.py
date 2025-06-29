# anagrams 

text1=" "
while (text1.isspace()):
    text1 = input("Please Enter text1, it shouldn't be only spaces or empty: ")
text1 = text1.strip()
text1=text1.replace(" ","")
text1=text1.lower()
lenght1 = len(text1)
print("text1= ", text1, ", lenght1= ", lenght1)
text2=" "
while (text2.isspace()):
    text2 = input("Please Enter text2, it shouldn't be only spaces or empty: ")
text2 = text2.strip()
text2=text2.replace(" ","")
text2=text2.lower()
lenght2 = len(text2)
print("text2= ", text2, ", lenght2= ", lenght2)


anagrams=False
letterCount=0
checkedChars=[]
alreadyPrinted=False
if (lenght2!=lenght1):
    print("They vary in lenght and do not include spaces so they are not anagrams")
else:
    for char in text1:
        if char not in checkedChars:
            checkedChars.append(char)
            letterCount+=text2.count(char)
        if (text2.count(char)==0):
            print("They are not anagrams 1")
            alreadyPrinted=True
            break
        if ((char==text1[-1])and(letterCount==lenght2)):
            anagrams=True
if(anagrams):
    print("They are anagrams 1")
elif(not(alreadyPrinted)):
    print("They are not anagrams 2")
