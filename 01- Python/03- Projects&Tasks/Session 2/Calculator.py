################################################
# Project : Calcultor (Standard & Programmer)  #
# Auther : Ahmed Bahaa Nasr                    # 
# Date : 15/5/2023                             # 
################################################
import os
from time import sleep
# ===========================================================================
# Convert From DIC to BIN
def Binary(x):
    Binary_List = []
    if x < 256 :
        y = 8
        List = [7,6,5,4,3,2,1,0]
    else:
        y = 16
        List = [15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0]    
        
    for i in range(0,y,1):
        if ( ( x >= 2**List[i] ) ):
            Binary_List.insert(i,1)
            x = x - (2**List[i])
        else :
            Binary_List.insert(i,0)
    return Binary_List
# ===========================================================================
# Convert From BIN to DEC
def Decimal(B_List):    
    z = 0 
    if len(B_List) <= 8 :
        List = [7,6,5,4,3,2,1,0]
    else:
        List = [15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0] 
    for i in range(0,len(B_List),1):                       
        if B_List[i] == 1 :
            z = z + 2**List[i]
    return z
# ===========================================================================
# Convert From BIN to HEX
def Hexcadicemal(New_List):
    H1,H2,H3,H4 = 0,0,0,0
    List_4Bit = [3,2,1,0] 
    if len(New_List) > 8 :
        M_MSB = [ New_List[0],New_List[1],New_List[2],New_List[3] ]
        M_LSB = [ New_List[4],New_List[5],New_List[6],New_List[7] ]
        L_MSB = [ New_List[8],New_List[9],New_List[10],New_List[11] ]
        L_LSB = [ New_List[12],New_List[13],New_List[14],New_List[15] ]
        for i in range(0,len(M_MSB),1):                       
            if M_MSB[i] == 1 :
                H1 = H1 + 2**List_4Bit[i]
        for i in range(0,len(M_LSB),1):                       
            if M_LSB[i] == 1 :
                H2 = H2 + 2**List_4Bit[i]
        for i in range(0,len(L_MSB),1):                       
            if L_MSB[i] == 1 :
                H3 = H3 + 2**List_4Bit[i]
        for i in range(0,len(L_LSB),1):                       
            if L_LSB[i] == 1 :
                H4 = H4 + 2**List_4Bit[i]
    else :
        M_MSB = [ New_List[0],New_List[1],New_List[2],New_List[3] ]
        M_LSB = [ New_List[4],New_List[5],New_List[6],New_List[7] ]
        for i in range(0,len(M_MSB),1):                       
            if M_MSB[i] == 1 :
                H1 = H1 + 2**List_4Bit[i]
        for i in range(0,len(M_LSB),1):                       
            if M_LSB[i] == 1 :
                H2 = H2 + 2**List_4Bit[i]
    if H1 == 10 :
        H1 = "A"
    elif H1 == 11 :
        H1 = "B"
    elif H1 == 12 :
        H1 = "C"
    elif H1 == 13 :
        H1 = "D"
    elif H1 == 14 :
        H1 = "E"
    elif H1 == 15 :
        H1 = "F"
    if H2 == 10 :
        H2 = "A"
    elif H2 == 11 :
        H2 = "B"
    elif H2 == 12 :
        H2 = "C"
    elif H2 == 13 :
        H2 = "D"
    elif H2 == 14 :
        H2 = "E"
    elif H2 == 15 :
        H2 = "F"
    if H3 == 10 :
        H3 = "A"
    elif H3 == 11 :
        H3 = "B"
    elif H3 == 12 :
        H3 = "C"
    elif H3 == 13 :
        H3 = "D"
    elif H3 == 14 :
        H3 = "E"
    elif H3 == 15 :
        H3 = "F"
    if H4 == 10 :
        H4 = "A"
    elif H4 == 11 :
        H4 = "B"
    elif H4 == 12 :
        H4 = "C"
    elif H4 == 13 :
        H4 = "D"
    elif H4 == 14 :
        H4 = "E"
    elif H4 == 15 :
        H4 = "F"
    HEX = [H1,H2,H3,H4]
    return HEX 
# ===========================================================================
# Power Function
def Power(x,y):
    z = 1
    for i in range(0,y,1):
        z = z*x
    return z

print("***************************************")
print("***************************************")
print("**      Welcome to My Calculator     **")
print("**     Auther : Ahmed Bahaa Nasr     **")
print("**      Embedded Linux Software      **")
print("***************************************")
print("***************************************")
sleep(2.5)
while True :
    os.system('cls')
    print("====================")
    print("(1) Standard ")
    print("(2) Programmer")
    print("(0) Exit Program")
    print("====================")
    Mode = int(input("Select Mode: "))
    if Mode == 1 :
        Exit = 1
        while Exit != 0 :
            os.system('cls')
            print("===========================")
            equation = input("Enter the Equation: ")
            List = equation.split()
            os.system('cls')
            print("================")
            if List[1] == '+':
                print(List[0],List[1],List[2],"=",int(List[0])+int(List[2]))
            elif List[1] == '-':
                print(List[0],List[1],List[2],"=",int(List[0])-int(List[2]))
            elif List[1] == '*':
                print(List[0],List[1],List[2],"=",int(List[0])*int(List[2]))
            elif List[1] == '/':
                print(List[0],List[1],List[2],"=",int(List[0])/int(List[2]))
            elif List[1] == '^':
                print(List[0],List[1],List[2],"=",Power(int(List[0]),int(List[2])))
            print("================")
            print("(1) to Continuo")
            Exit = int(input("(0) to Exit   "))  
        
    elif Mode == 2 :
        os.system('cls')
        while True :
            print("===========================")
            x = int(input("Entre Decimal Number: "))
            if x == 0 :
                break
            New_List = Binary(x)
            os.system('cls')
            print("===========================")
            # ===================================================== 
            # Print List of Binary
            print("Binary  : ",end="")
            for i in range(0,len(New_List),1):
                if (len(New_List)-i) == 1 :
                    print(New_List[i])  
                else:
                    print(New_List[i],end="") 
            # =====================================================    
            # Print Decimal
            print("Decimal : ",end="")
            DEC = Decimal(New_List)
            print(DEC)
            # ===================================================== 
            #  Print HEX
            HEX = Hexcadicemal(New_List)
            print("HEXA    : ",end="")
            if HEX[2] != 0 or HEX[3] != 0 :
                print("0x",end="") 
                print(HEX[0],end="")
                print(HEX[1],end="")
                print(HEX[2],end="")
                print(HEX[3])
            else :
                print("0x",end="") 
                print(HEX[0],end="") 
                print(HEX[1])
    elif Mode == 0 :
        break


        
           

