# myname = input("Hello, Please Enter Your Name : ")   #Getting Name
# myage = input("Enter Your age : ")                   #Getting age
# myfaculty = input("Enter Your Faculty : ")
# f = open("file.txt","w")
# f.write("My Name is "+myname+"\n")
# f.write("My Age is "+myage+"\n")
# f.write("My Faculty : "+myfaculty+"\n")
# f = open("file.txt","w+")  # w+ معناها لو مش موجود اعمله create
f = open("file.txt","a") # append in file without overwrite
f.write("LOL")
f = open("file.txt","r")
print(f.read())
# print(f.read(100))    # read 100 characters in all file
# print(f.readline(20))   # read 50 characters in one line of file
# print(f.readlines(50))  # read 50 characters in all lines of file in List

f.close()
