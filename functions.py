def greetings():
    message = print("hello from the other side")
    return message
greetings()

message = "hello from user"
mes= "hello from user two"

def greeting(greet):
    print(greet)
    return
greeting(message)
greeting(mes)

def simple_add(num1, num2):
    print(int(num1)+int(num2))

    return
simple_add(1,1)

def default_arguments(num1, num2 = 1):
    division = (int(num1)/int(num2))
    print(int(division))
    return
default_arguments(20,4)
