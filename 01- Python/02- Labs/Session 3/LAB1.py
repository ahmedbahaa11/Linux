from tkinter import *

def ButtomPressedTraker():
    ButtomPressedTraker.counter += 1
    print("The Buttom Pressed ",ButtomPressedTraker.counter)
    label = Label(window,text = ButtomPressedTraker.counter )
    label.pack(side = TOP)

def Fun():
    label = Label(window,text = "Ahmed Bahaa Nasr")
    label.pack(side = TOP)
    print("Ahmed Bahaa Nasr")  
    
ButtomPressedTraker.counter = 0

window = Tk()

window.title("GUI")
window.geometry('500x500')
# label = Label(window,text = "Ahmed Bahaa Nasr")
# label.pack(side = TOP)
b1 = Button(window , text = "Your Name" , bd = '15', command = Fun)
b1.pack(side = LEFT)

# b3 = Button(window , text = "Nasr")
# b3.pack(side = BOTTOM)
# b4 = Button(window , text = "Hello GUI")
# b4.pack(side = TOP)
b5 = Button(window , text = "Exit Program", bd = '10' , command = window.destroy)
b5.pack(side = BOTTOM)

photo1 = PhotoImage(file='iti.png')
photo1 = photo1.subsample(2,2)
b2 = Button(window , text = "Photo" , background="green", bd = '10' , image = photo1 , command = ButtomPressedTraker , fg="red" , font = ('Verdana', 15))
b2.pack(side = RIGHT)
b2.place(x= 150 , y = 250)
window.mainloop()
