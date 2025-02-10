import os
class DirSearch:
    def find(self,path, dir):
        #path.replace('\','/')
        os.chdir(path)
        path = os.getcwd()
        #print("path: ", path)
        if dir in path:
            return path
        else:
            list = os.listdir()
            #print("list: ", list)
            if dir in list:
                print( path , '\\' , dir)
            else:
                for i in list:
                    #print("i:",i)
                    if "." not in i:
                        self.find(path+ "\\" + i, dir)

ds=DirSearch()
ds.find("./tree","python")
#os.chdir("./tree/cpp")
#print(os.getcwd())
#path="./tree", dir="python"
#dir2 = "python"
#list1=['python']
#if dir2 in list1:
#    print("yes")
