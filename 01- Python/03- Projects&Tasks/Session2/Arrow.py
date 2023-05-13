######################################
# Project : Aroww Animation          #
# Auther : Ahmed Bahaa Nasr          # 
# Date : 12/5/2023                   # 
######################################
import os
# import sleep to show output for some time period
from time import sleep
# ====================================================
# ==================   Arrow_1   =====================
def Up_Arrow() :
    for n in range(0,3,1):
        print("\t\t\t\t")
    for Row in range(0,7,1):
        print("\t\t\t\t",end="")
        for x in range(Row,7,1):
            print(" ",end="")
        for y in range(0,(2*Row)-1,1):
            print("*", end="")
        print("")
    for i in range(0,7,1) :
        print("\t\t\t\t      *") 
# ====================================================
# ==================   Arrow_2   =====================
def Right_Arrow ():
    for n in range(0,10,1):
        print("\t\t\t\t")
    for Row in range(0,6,1):
        print("\t\t\t\t\t\t        ",end="")
        for x in range (0,Row,1):
            print("*",end="")
        print("")
    # -----------------------------------------------
    print("\t\t\t\t      * * * * * * * * * Bahaa")
    # -----------------------------------------------
    for Row in range(0,6,1):
        print("\t\t\t\t\t\t        ",end="")
        for x in range (Row,5,1):
            print("*",end="")
        print("")
# ====================================================
# ==================   Arrow_3   =====================
def Down_Arrow ():
    for n in range(0,16,1):
        print("\t\t\t\t")     
    for i in range(0,7,1) :
        print("\t\t\t\t      *")     
    for Row in range(1,7,1):
        print("\t\t\t\t ",end="")
        for x in range(1,Row,1):
            print(" ",end="")
        for y in range(0,(14-(2*Row)-1),1):
            print("*", end="")
        print("")
# ====================================================
# ==================   Arrow_4   =====================
def Left_Arrow():
    for n in range(0,11,1):
        print("\t")
        
    for Row in range(1,6,1):
        print("\t       ",end="")
        for y in range(Row,6,1):
            print(" ",end="")
        for x in range (0,Row,1):
            print("*",end="")
        print("")
    # -----------------------------------------------
    print("\t        Ahmed * * * * * * * * *")
    # # -----------------------------------------------
    for Row in range(1,6,1):
        print("\t        ",end="")
        for y in range (1,Row,1):
            print(" ",end="")
        for x in range (Row,6,1):
            print("*",end="")
        print("")
# ====================================================                   
while True:  
    Up_Arrow()
    sleep(0.5)
    os.system('cls')
    Right_Arrow()
    sleep(0.5)
    os.system('cls')
    Down_Arrow()    
    sleep(0.5)
    os.system('cls')
    Left_Arrow()
    sleep(0.5)
    os.system('cls')
# ==================================================== 

