import os
print(os.name)
print("dir(os): ",dir(os))

import platform
print("dir(platform): ",dir(platform))
print(platform.uname())

print("platform.platform(0,1): ", platform.platform(0,1))
print("platform.platform(1,0): ", platform.platform(1,0))
print("platform.platform(1,1): ", platform.platform(1,1))
print("platform.platform(): ", platform.platform())
print("platform.machine(): ", platform.machine())

#import processor
print("platform.processor(): ",platform.processor())
from platform import system
print("system(): ",system())
from platform import version
print("version(): ",version())
# this is a relative path which
#will create the my_first_directory directory in the current working directory;
os.mkdir("my_first_directoryRP")
print("listdir: ",os.listdir())

#this is a relative path that explicitly points to the current working directory.
#It has the same effect as the path above;
os.mkdir("./my_first_directoryRPEPTTCWD")

#this is a relative path that will create the my_first_directory directory
#in the parent directory of the current working directory;
os.mkdir("../my_first_directoryRPEPTTCWDP")

# this is the absolute path that will create the my_first_directory directory,
#which in turn is in the python directory in the root directory.
#root directory in my case was the c 
os.mkdir("/Python312/my_first_directoryAP")

#The code creates two directories. The first of them is created in the current working directory, while the second in the my_first_directory directory.
os.makedirs("my_first_directory/my_second_directory")
#To move between directories, you can use a function called chdir, which changes the current working directory to the specified path.
#As an argument, it takes any relative or absolute path. 
os.chdir("my_first_directory")
print(os.listdir())

#NOTE: The equivalent of the makedirs function on Unix systems is the mkdir command with the -p flag, while in Windows, simply the mkdir command with the path:

#Unix-like systems:

#mkdir -p my_first_directory/my_second_directory

#Windows:

#mkdir my_first_directory/my_second_directory

print(os.getcwd())
os.chdir("my_second_directory")
print(os.getcwd())
os.chdir("C:/Python312/my_first_directory")
os.rmdir("C:/Python312/my_first_directoryRPEPTTCWD")
os.rmdir("C:/my_first_directoryRPEPTTCWDP")
os.rmdir("C:/Python312/my_first_directoryAP")
os.rmdir("C:/Python312/my_first_directoryRP")
os.removedirs("C:/Python312/my_first_directory/my_second_directory")

os.chdir("C:/Python312/")
if "my_first_directory" in(os.listdir()):
    os.rmdir("C:/Python312/my_first_directory")

returned_value = os.system("mkdir my_first_directory")
print(returned_value)
print(os.listdir())
os.rmdir("C:/Python312/my_first_directory")
os.chdir("C:/Python312")

