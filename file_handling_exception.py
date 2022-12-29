try:
   fh = open("testfile1.txt", "r")
   fh.write("This is my test file for exception handling!!")
except FileNotFoundError:
   print("Error: can't find file or read data")
else:
   print("Content written successfully")