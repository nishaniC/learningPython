from os import strerror

data = bytearray(10)
#replace 10 with something like ord('a')
#- this will produce bytes containing values corresponding to the
#alphabetical part of the ASCII code (don't think it will make the file a text file - it's still binary, as it was created with a wb flag)
for i in range(len(data)):
    data[i] =  ord('a') + i

try:
    bf = open('file.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
print("")
print("--------------------------------------------------")
# Your code that reads bytes from the stream should go here.
data2 = bytearray(15)

try:
    bf = open('file.bin', 'rb')
    bf.readinto(data2)
    bf.close()

    for b in data2:
        print(hex(b), end=' ')
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
print("")
print("--------------------------------------------------")
try:
    bf = open('file.bin', 'rb')
    data3 = bytearray(bf.read())
    bf.close()

    for b in data3:
        print(hex(b), end=' ')

except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
print("")
print("--------------------------------------------------")

try:
    bf = open('file.bin', 'rb')
    data = bytearray(bf.read(5))
#    data = bytearray(bf.read(5))
#    data = bytearray(bf.read(5))
    bf.close()

    for b in data:
        print(hex(b), end=' ')

except IOError as e:
    print("I/O error occurred:", strerror(e.errno))


print("--------------------------------------------------")

srcname = input("Enter the source file name: ")
try:
    src = open(srcname, 'rb')
except IOError as e:
    print("Cannot open the source file: ", strerror(e.errno))
    exit(e.errno)	

dstname = input("Enter the destination file name: ")
try:
    dst = open(dstname, 'wb')
except Exception as e:
    print("Cannot create the destination file: ", strerror(e.errno))
    src.close()
    exit(e.errno)	

buffer = bytearray(65536)
total  = 0
try:
    readin = src.readinto(buffer)
    while readin > 0:
        written = dst.write(buffer[:readin])
        total += written
        readin = src.readinto(buffer)
except IOError as e:
    print("Cannot create the destination file: ", strerror(e.errno))
    exit(e.errno)	
    
print(total,'byte(s) succesfully written')
src.close()
dst.close()

