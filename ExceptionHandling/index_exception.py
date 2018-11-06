
# IndexError exception

abc=[10,20,20]
try:
 print(abc[3])
except IndexError:
    print("Index out of range")
else:
    print ('No exception')

#TypeError Exception

print('***********************************')
try:
    a=int(5)
    b=str
    c=a+b
except TypeError:
    print ('Caught TypeError Exception')
else:
    print ('No exception')

print('***********************************')
# ValueError Exception

try:
    print(int('a'))
except ValueError:
    print ('Caught ValueError Exception')
else:
    print ('No exception')