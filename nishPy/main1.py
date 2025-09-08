import sys
print("before append")
for p in sys.path:
    print(p)
sys.path.append('C:\\Users\\adeet\\py\\modules')
print("after append")
for p in sys.path:
    print(p)

from module import suml, prodl, __counter

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(zeroes)
print(ones)
print(suml(zeroes))
print(prodl(ones))
print("__counter:",__counter)
