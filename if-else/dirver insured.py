marriage=input("You are married? Y/N")
gender=input("Enter your gender:M/F")
age=int(input("Enter your age:"))

if marriage=="Y":
    print("The driver is insured")
elif marriage=="N" and gender=="M" and age>30:
    print("The driver is insured")
elif marriage=="N" and gender=="F" and age>25:
    print("The driver is insured")
else:                                               
    print("The driver is not insured")