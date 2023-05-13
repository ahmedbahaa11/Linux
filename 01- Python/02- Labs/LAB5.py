
while True :
    print("To Explain Function center() Press (1)")
    print("To Explain Function rfind()  Press (2)")
    print("To Explain Function find()   Press (3)")
    x = int (input("Entre you choice : "))
    if x == 1 :
        print("txt = banana ")
        print("x = txt.center(20) ")
        y = int(input("Press (1) to show the output of x "))
        txt = "banana"
        x = txt.center(20)
        if y == 1 :
            print("output is : ",x)
            print("Print the word banana , taking up the space of 20 characters, with banana in the middle:")
            print("====================================")   
    elif x == 2 :
        print("txt = Mi casa, su casa.")
        print("x = txt.rfind(casa)")
        y = int(input("Press (1) to show the output of x "))
        txt = "Mi casa, su casa."
        x = txt.rfind("casa")
        if y == 1 :
            print("output is : ",x)  
            print("====================================")        
    elif x == 3 :
        print('''txt = Hello, welcome to my world. ")
x = txt.find(welcome)''')
        y = int(input("Press (1) to show the output  of x "))
        txt = "Hello, welcome to my world."
        x = txt.find("welcome")
        if y == 1 :
            print("output is : ",x)
            print("====================================")  
    elif x == 27  :
        break














# ############ Set ############
# #  غير مرتبة وغير مكررة وغير قابلة للتعديل
# #  تستخدم عادة لاختبار وجود العناصر والتخلص من المدخلات المكرره
# # Set is Unorderd
# # Constant per its elements
# # immutable
# my_set = {90,5,80,1,1,1,50,70}                 
# print(my_set)              # {80, 1, 50, 5, 70, 90}
# my_set = {2,1,1,1,50,70}                 
# print(my_set)              # {1, 2, 50, 70}
# # my_set = {90,5,60,20,80,1,2,1,1,3,[50,70]}    
# # print(my_set)     # Error TypeError: unhashable type: 'list'
