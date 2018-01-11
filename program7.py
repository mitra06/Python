"""
Python Program to Find the Sum of Digits in a Number
"""
n=int(input("Enter the number"))
print("Number is " ,n)
sum=0

while(n!=0):
    dig=n%10
    sum=sum+dig
    n=n//10
print("sum =" , sum)