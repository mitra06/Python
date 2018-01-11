"""
Python Program to Find the Smallest Divisor of an Integer

"""
n=int(input("Enter the numbers"))
d=[]
for i in range(2,n+1):
    if(n%i==0):
        d.append(i)
        
d.sort()
print(d)
print("The smallest divisor=",d[0] )