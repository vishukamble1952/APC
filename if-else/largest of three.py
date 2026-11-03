n1=int(input("first number:"))
n2=int(input("Second number:"))
n3=int(input("Third number:"))
if n1>n2 and n1>n3:
    print("Largest number:",n1)
elif n2>n3:
    print("Largest number:",n2)
else:
    print("Largest number:",n3)
