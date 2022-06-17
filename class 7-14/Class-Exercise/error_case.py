def division(x, y):
    try:
        result = x / y
    except Exception:
        print("Sorry Somethings went wrong!")
    else:
        print("Result is ", result)



division(1, 2)
division(10, 0)
