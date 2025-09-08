try:
    print("5"/0)
except ArithmeticError:
    print("ArithmeticError")
except(ZeroDivisionError):
    print("ZeroDivisionError")
except TypeError:
    print("Default")    
