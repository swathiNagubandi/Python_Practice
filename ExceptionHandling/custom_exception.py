from ExceptionHandling.myexception import *
def enterage(age):

 if age < 0:
   raise AgeException("Only positive integers are allowed")
 if age%2==0:
     print("age is even")
 else:
  print("age is odd")




try:
  num = int(input("Enter your age: "))
  enterage(num)

except AgeException as ex:
  print(ex )
else:
  print("something is ok")