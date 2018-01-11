"""
Program to Print all Numbers in a Range Divisible by a Given Number
"""
n1=int(input("Enter the smallest number in range"))
n2=int(input("Enter the highest number in range "))
n=int(input("Enter the number to be divided by:"))
for i in range(n1,n2+1):
    if(i%n)==0:
        print(i)
    