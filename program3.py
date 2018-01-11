"""
Reverse a Given Number

"""

num=int(input("Enter the number"))
print("The given number is " , num)

rev=0
while(num!=0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
print("Reverse of the number is", rev)