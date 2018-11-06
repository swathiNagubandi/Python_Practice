def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("can't division by zero!")
    else:
        print("result is", result)
    finally:
        print("Always this statement executes")
#giving the result
divide(2, 1)
#throwing exception
divide(2, 0)