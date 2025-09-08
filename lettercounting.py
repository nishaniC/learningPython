srcname = input("Enter the source file name: ")
try:
    src = open(srcname, 'rt')
except IOError as e:
    print("Cannot open the source file: ", strerror(e.errno))
    exit(e.errno)	

indexList= {}
try:
    readin = src.readline()
    while readin:
        for ch in readin:
            ch = ch.lower()
            if ch in indexList:
               indexList[ch]= indexList.get(ch)+1
            else:
                indexList[ch]=1    
        readin = src.readline()
    src.close()   
except IOError as e:
    print("Cannot read the file: ", strerror(e.errno))
    src.close()
    exit(e.errno)
#The sorted() function in Python returns a new list containing all items from the iterable in ascending order by default.
#It does not modify the original iterable. Here’s a quick overview:    
#Basic sorting: sorted(iterable)
#Reverse sorting: sorted(iterable, reverse=True)
#Custom key sorting: sorted(iterable, key=function)
sorted_dict = dict(sorted(indexList.items(), key=lambda item: item[1], reverse=True))

destname = srcname.replace(".txt", ".hist", 1)

try:
    dest = open(destname, 'wt')
    
except IOError as e:
    print("Cannot open the destination file: ", strerror(e.errno))
    exit(e.errno)
try:
        
    for key in sorted_dict.keys():
        #text=str(key)+" -> "+str(indexList[key])+"\n"
        dest.write(str(key)+" -> "+str(indexList[key])+"\n")
        print(str(key)+" -> "+str(indexList[key])+"\n")

    dest.close()
except IOError as e:
    print("Cannot write to the file: ", strerror(e.errno))
    dest.close()
    exit(e.errno)        
