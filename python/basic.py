# NAME="John Doe"
# friends = ["Alice", "Bob", "Charlie"]
# address = {
#     "street": "123 Main St",
#     "city": "Anytown",
#     "state": "CA",
#     "zip": "12345"
# }
# a="""hii 
# this is a multi line string
# and it can span multiple lines
# and it can contain special characters like \n and \t"""
# print("Hello, my name is", NAME),
# print("My friends are:", ", ".join(friends)),
# print("My address is:", address["street"], address["city"], address["state"], address["zip"])
# print(a)

# for char in a:
#     print(char)


# fruit="avacado"
# print(fruit)
# print(fruit[0])  # prints 'a'
# print(fruit[1 :len(fruit)-3])  # prints 'v'



# a="harry"
# print(a[-4:-2])
# print(a.lower())
# print(a.upper())
# print(a.replace("h","H"))
# print(a.rstrip("y"))
# print(a.capitalize())
# b=" hii this is a multi line string for the find function"
# print(b.find("multi"))


# <----Conditional Statements---->

# num=int(input("Enter a number: "))
# if num>0:
#     print("Number is positive")
# elif num==0:
#     print("Number is zero")
# elif num<0:
#     print("Number is negative")
# elif (num==10 and num<20):   
#     print("Number is between 10 and 20")
# elif (num==10 or num<20):
#     print("Number is between 10 and 20")    
# else:
#     print("Chill kro yaar")




# import time
# time=time.strftime("%H:%M:%S")
# if time>="00:00:00" and time<="11:59:59":
#     print("Good Morning")
# elif time>="12:00:00" and time<="15:59:59":
#     print("Good Afternoon")
# else:
#     print("Good Evening")



# <----Loops---->

# name ="Jeet Kumar Singh"
# for i in name:
# #     print(i)   
# list=["Jeet", "Kumar", "Singh"]
# for list in list:
#   print(list)


# for i in range(1, 11):
#     print(i)



# i=int (input("Enter a number: "))
# while (i)<=38:
#     i=int(input("Enter a number: "))
#     print("You entered:", i)
i=1
# while i==1:
#     i in range(1,)
#     print("You entered:", i)

# <--break statement-->
# for i in range(1, 15):
#      if i==10:
#         break
#      print(5, "x", i, "=", 5*i)
   

# <----continue statement-->
for i in range (1, 15):
    if i==10:
        continue
    print(5, "x", i, "=", 5*i)