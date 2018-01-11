"""
Python Program to Exchange the Values of Two Numbers Without Using a Temporary Variable

"""

a= int(input("Enter number one"))
b= int(input("Enter number two"))

print("After swapping")
c=a+b
a=c-a
print("a =", a)
b=c-a
print("b =", b)
