stack = []


def push(val):
    stack.append(val)


def pop():
    if (stack):
        val = stack[-1]
        del stack[-1]
        return val


push(3)
push(2)
push(1)

print(pop())
print(pop())
print(pop())
print(pop())

class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val


class CountingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__count = 0

    def get_counter(self):
        return self.__count

    def pop(self):
        self.__count+=1
        Stack.pop((self))

stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())

