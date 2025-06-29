text1=" "
while (text1.isspace()):
    text1 = input("Please Enter your burthdate in the format  YYYYMMDD: ")
text1 = text1.strip()
text1=text1.replace(" ","")
text1=text1.lower()
lenght1 = len(text1)
print("text1= ", text1, ", lenght1= ", lenght1)
numbers=list(text1)
digit=0
twoDigit=" "
for n in numbers:
    digit+=int(n)
if digit>10:
    twodigit=str(digit)
    numbers=list(twodigit)
    digit=0
    for n in numbers:
        digit+=int(n)
    print("Digit of Life: ", digit)
elif digit==10:
    print("Digit of Life: 1")
else:
    print("Digit of Life: ", digit)
    
