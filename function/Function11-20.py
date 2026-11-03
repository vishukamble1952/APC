def reverse(S):
    rev=" "
    for i in S:
        rev=i+rev
    return rev
print(reverse("Abhi"))

def palindrome(S):
    if S==S[::-1]:
      print("Palindrome")
    else:
      print("Non-Palindrome")
palindrome("Madam")

def average(a):
     sum=0    
     for i in a:
         sum+=i
     avg=sum//len(a)
     return avg
a=[1,3,5,7,9,11]
print(average(a))

def occurence(list,element):
   count=0
   for i in list:
      if element==i:
         count+=1
   return count
a=[2, 3, 5, 4, 6, 3, 6, 2, 4, 2, 3, 5, 7, 4, 5, 3]
print(occurence(a,3))

def unique_list(list):
   new_list=[]
   for i in list:
     if i not in new_list:
         new_list.append(i)
   return new_list;
a=[2, 3, 5, 4, 6, 3, 6, 2, 4, 2, 3, 5, 7, 4, 5, 3]
print(unique_list(a))

def second_largest(lst):
   unique=list(set(lst))
   unique.sort()
   return unique[-2]
a=[11,34,6,95,67,78,36]
print(second_largest(a))

def fibonacci(n):
   a=0
   b=1
   for i in range(n):
      a,b=b,a+b
   return a
print(fibonacci(5))

def result(m1,m2,m3,m4,m5):
   total=m1+m2+m3+m4+m5
   percent=(total/500)*100
   print("Student percentage:",percent,"%")
   
   if percent>80:
       print("Grade A")
   elif 60<percent or percent<=80:
       print("Grade B")
   elif 40<percent or percent<=60:
       print("Grade C")
   else:
       print("Grade D")
result(56,78,97,96,56)