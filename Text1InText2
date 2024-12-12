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

alreadyPrinted=False
start=0
end=lenght2-lenght1+1
if (lenght2<lenght1):
    print("Text2 is shorter so Text1 is not in Text2")
else:
    for char in text1:
        start=text2.find(char,start,end)
        if(start==-1):
           print("Text1 is not in Text2,,1")
           alreadyPrinted=True
           break
        else:
            end+=1
    if(not(alreadyPrinted)):
        print("Text1 is in Text2")
        
