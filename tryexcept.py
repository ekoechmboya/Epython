#try except, else, finally
#try block

try:
    print(x)
except:
    print("an error occured, check if email is defined")
else:
    print(str(x)+"from else")
finally:
    print("finally block")


# raise keyword: works with a condition if condition is met

x=9
if x<0:
    raise TypeError("sorry x shouldn't be less than zero")