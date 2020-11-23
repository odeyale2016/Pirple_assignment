keyword = "Hello"

try:
    raise NameError("Error")
except  ValueError:
    print("got Value Error")
except Exception as e:
    print("Other type of exception")
    print(str(e))
else:
    print("No Error")
finally:
    print("Finally")