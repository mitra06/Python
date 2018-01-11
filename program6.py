"""
Python Program to Print Odd Numbers Within a Given Range

"""
lower=int(input("Enter the number"))
higher=int(input("Enter the number"))

for i in range(lower,higher+1):
    if(i%2!=0):
        print(i)