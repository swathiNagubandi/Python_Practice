try:
   fh = open("C:/Users/swathi.nagubandi/PycharmProjects/Python_Practice/ExceptionHandling/testfile.txt", mode="rb")
   fh.write("some text file")
except IOError:
   print("Error: can not find file")
else:
   print("Written content in the file successfully")