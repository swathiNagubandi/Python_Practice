def divide(x, y):
    try:
        result = x / y
    except ArithmeticError:
        print("Arithmetic exception raised.")

    else:
        print("result is", result)
    finally:
        print("Always this statement executes")
#giving the result
divide(2, 1)
#throwing exception
divide(2, 0)