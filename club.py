import tkinter




while True:

    gender = "male"
    age= input("enter age")
    gender= input("enter gender")

    if int(age) <= 17 and int(age) > 0:

      print("too young")
    elif int(age) >=18 and gender=="male":
      print("can go in! But does not receive a free drink")
    elif int(age) >=18 and gender=="female":
      print("can go in! receives a free drink, its ladies night")
    else:
        print("invalid input")