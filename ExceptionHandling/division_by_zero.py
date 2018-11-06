num=1.5
try:
  print(num/0)
except ZeroDivisionError:
   print ("Error: can\'t division by zero")
