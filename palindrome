index = -1
text=" "
while (text.isspace()):
    text = input("Please Enter your message, it shouldn't be only spaces or empty: ")
text = text.strip()
lenght = len(text)

palindrome=False
if lenght<=1:
    print("It's not a palindrome 1")
else:
    for char in text:
        if char.isspace():
            lenght-=1
            print("lenght: ",lenght)
            continue
        char = char.upper()
        print("Char: ",char)
        while( text[index].isspace()):
            index-=1
        if(-index<(lenght/2)):
            if(char==(text[index].upper())):
                print("char: ",char, "text[", index,"]: ", text[index])
                index-=1
                palindrome=True
                continue
            else:
                print("It's not a palindrome 2 ") 
                break
        else:
            break
    if (palindrome):
        print("It's a palindrome")
    elif(index!=-1):
        print("It's not a palindrome 3")
