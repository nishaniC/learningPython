class StudentsDataException(Exception):
    pass


class BadLine(StudentsDataException):
   def __init__(self, lineNumber):
        print("Test data at line ", lineNumber, "is inocrrect") 
        
class FileEmpty(StudentsDataException):
    def __init__(self, file):
        print("The file : ", file, "is empty")


srcname = input("Enter the source file name: ")
try:
    src = open(srcname, 'rt')
except IOError as e:
    print("Cannot open the source file: ", strerror(e.errno))
    exit(e.errno)	

try:
    readin = src.readline()
    fileEmpty = True
    content =[]
    studentRecords={}
    firstName=""
    lastName=""
    marks=0
    marksSet=False
    chno=0
    lineNum=1
    while readin:
        fileEmpty = False
        print(readin)
        for ch in readin:
            chno+=1
            print("ch: ", ch)
            if ((ch == ' ') or (ch == "\t")):
                readin=readin[chno:]
                if ((firstName=="")and (len(content)!=0)):
                    firstName=''.join(content)
                    print("firstName :", firstName)
                    content =[]
                elif((lastName=="") and (len(content)!=0)):
                    lastName=''.join(content)
                    content =[]
                elif((not marksSet) and (len(content)!=0)):
                    marks=float(''.join(content))
                    marksSet=True
                    content =[]
                continue
            if ((ch=="\n")and(lastName!="")and(not marksSet)):
                marks=float(''.join(content))
                marksSet=True
                content =[]
            elif ((ch=="\n")and(firstName=="")):
                raise BadLine(lineNum)
            content.append(ch)
            print("content:",content)
        readin = src.readline()
        if((not readin)and(lastName!="")and(not marksSet)):
            marks=float(''.join(content))
            content =[]
        name = firstName.capitalize()+" "+ lastName.capitalize()
        if name in studentRecords:
            studentRecords[name]= studentRecords.get(name)+marks
        else:
            studentRecords[name]=marks  
        
        content =[]
        firstName=""
        lastName=""
        marks=0
        marksSet=False
        lineNum+=1
    src.close()
    if fileEmpty:
        raise FileEmpty(srcname)
except (BadLine,FileEmpty) as e:
    src.close()
    exit()
except IOError as e:
    print("Cannot read the file: ", strerror(e.errno))
    src.close()
    exit(e.errno)

print("-------------------Results---------------------------")
for key in sorted(studentRecords.keys()):
    print(key," "*(15-len(key)),studentRecords[key])
       
