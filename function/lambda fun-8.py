#square of num
square= lambda n:n**2
num=int(input("Enter a number:"))
print("Square=",square(num))

#Cube of num
cube= lambda n:n**3
n=int(input("Enter a number:"))
print("Cube=",cube(n))

#is num even
even= lambda n:n%2==0
num=int(input("Enter a number:"))
print(even(num))

#max of 2
maximum=lambda a,b:a if a > b else b
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))

print("Maximum of ",a,"&",b,":",maximum(a,b))

#Simple interest
SI=lambda p,r,t:p*r*t/100
p=int(input("Enter a principal:"))
r=int(input("Enter a rate:"))
t=int(input("Enter a time(year):"))
print("Simple Interest is", SI(p,r,t))

#make square using map function
num=[1,2,3,4,5,6,7,8]
squares=list(map(lambda x:x*x ,num))
print("Squareof list:",squares)

# cube using map()
nums=[1,2,3,4,5,6,7,8]
cubes=list(map(lambda x:x*x*x, nums))
print("Cube of list:",cubes)

#addition of 2 list using map
list1=[1,2,3,4,5]
list2=[5,4,3,2,1]
sum=list(map(lambda x,y:x+y,list1,list2))
print("Sum of 2 list:", sum)
