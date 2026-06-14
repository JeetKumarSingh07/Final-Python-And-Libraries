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

num=int(input("Enter a number: "))
if num>0:
    print("Number is positive")
elif num==0:
    print("Number is zero")
elif num<0:
    print("Number is negative")
elif (num==10 and num<20):   
    print("Number is between 10 and 20")
elif (num==10 or num<20):
    print("Number is between 10 and 20")    
else:
    print("Chill kro yaar")