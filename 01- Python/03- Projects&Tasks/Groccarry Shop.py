######################################
# Project : Groccary Shop            #
# Auther : Ahmed Bahaa Nasr          # 
# Date : 7/5/2023                    # 
######################################

Shop_Tuple = ("Name","Amount","Price of 1Kg")
Shop_List = [("Apple     ",100,30),("Banana    ",130,20),("Strawberry",111,15),("tomatoes  ",150,10),("potatoes  ",200,18)]
Buyer_Cart = []

print("***************************************")
print("***************************************")
print("**    Welcome to My Groccarry Shop   **")
print("**     Auther : Ahmed Bahaa Nasr     **")
print("**      Embedded Linux Software      **")
print("***************************************")
print("***************************************")

while True :
    print("===========================")
    print("[1] Admin Mode");
    print("[2] Buyer Mode");
    print("[0] Exit Program");
    print("===========================")
    print("Enter the mode you need: ");
    Mode = int(input("Select Mode: "))
    print("===========================")
    if Mode == 1 :
        print( "Please Enter Admin Password: " )
        Range = range(0,3,1)
        Admin_Feature = 1
        for i in Range :
            if Admin_Feature == 0 :
                break
            Password = int(input())  
            if Password == 1234 :
                print( "==========================" )
                print( "==========================" )
                print( "===   Welcome Admin   ====" )
                print( "==========================" )
                print( "==========================" )
                while True :
                    print( "==========================" )
                    print( "(1) Adding New Items" )
                    print( "(2) View All Items" )
                    print( "(3) Modifiy Item Details" )
                    print( "(0) Back to Main Window" )
                    print( "==========================" )
                    Admin_Feature = int(input("Select Feature: "))
                    print( "==========================" )
                    if Admin_Feature == 1 :
                        # Adding New Items
                        ItemName = input("Entre Name of Item : ")
                        ItemAmount = int(input("Entre Amount of Kgs from Item : "))
                        ItemPrice  = int(input("Entre Price of 1 Kg from Item : "))
                        Shop_Tuple = (ItemName,ItemAmount,ItemPrice)
                        Shop_List.append(Shop_Tuple)
                        print( "======================================================================" )
                        print( "=======================  Insertion Successfully  =====================" )
                        print( "======================================================================" )
                    elif Admin_Feature == 2 :
                        # View All Items 
                        List_Range = range(0,len(Shop_List),1)
                        print( "======================================================================" )
                        for List_iter in List_Range :
                            Shop_Tuple = Shop_List[List_iter]
                            print( " Item(",List_iter,"): " ,Shop_Tuple[0],"   |  Amount:",Shop_Tuple[1],"Kg     |  Price of 1Kg:",Shop_Tuple[2],"$" )
                        print( "======================================================================" )

                    elif Admin_Feature == 3 :
                        # Edit in Item Details
                        List_Range = range(0,len(Shop_List),1)
                        for List_iter in List_Range :
                            Shop_Tuple = Shop_List[List_iter]
                            print( " Item(",List_iter,"): " ,Shop_Tuple[0])
                        print( "==========================" )
                        Select_Item = int(input("Select Item Number to Edit on it : "))
                        ItemName = input(" Entre New Name of Item :           ")
                        ItemAmount = int(input(" Entre Amount of Kg from Item :     "))
                        ItemPrice  = int(input(" Entre New Price of 1 Kg from Item :"))
                        Shop_Tuple = (ItemName,ItemAmount,ItemPrice)
                        Shop_List[Select_Item] = Shop_Tuple
                        print( "======================================================================" )
                        print( "=======================  Modified Successfully  ======================" )
                        print( "======================================================================" )
                    else :
                        break
            else :	
                if i == 2 :
                    print("********************************************************")
                    print("***  Incorrect Password for 3 times, No more tries   ***")
                    print("********************************************************")
                    break
                else :
                    print("xxxxxxxxxxxxx")
                    print(" Try again : ")
    elif Mode == 2 :
        print( "==========================" )
        print( "==========================" )
        print( "===   Welcome Buyer   ====" )
        print( "==========================" )
        print( "==========================" )
        while True :
            print( "==========================" )
            print( "(1) Make Order" )
            print( "(2) View Receipt & Checkout" )
            print( "(0) Back to Main Window" )
            print( "==========================" )
            Buyer_Feature = int(input("Select Feature: "))
            print( "==========================" )
            if Buyer_Feature == 1 :
                while True :
                    List_Range = range(0,len(Shop_List),1)
                    print( "======================================================================" )
                    for List_iter in List_Range :
                        Shop_Tuple = Shop_List[List_iter]
                        print( " Item(",List_iter,"): " ,Shop_Tuple[0],"  /// Price of 1Kg:",Shop_Tuple[2],"$" )
                    print( "======================================================================" )
                    Temp = int(input("Select Item: "))
                    AddAmount_Item = int(input("Entre the Weight: "))
                    Buyer_Tuple = (Shop_List[Temp][0] ,AddAmount_Item , Shop_List[Temp][2] , AddAmount_Item*Shop_List[Temp][2] )
                    Shop_Tuple = (Shop_List[Temp][0], Shop_List[Temp][1]-AddAmount_Item ,Shop_List[Temp][2])
                    Shop_List[Temp] = Shop_Tuple
                    Buyer_Cart.append(Buyer_Tuple)
                    print( "==========================" )
                    print( "(1) Continue Shopping" )
                    print( "(0) Exit Shopping" )
                    print( "==========================" )
                    Exit_Shopping = int(input("Select Feature: "))
                    print( "==========================" )
                    if Exit_Shopping == 0 :
                        break

            elif Buyer_Feature == 2 :
                # View Receipt & Checkout
                Total_Recript = 0
                Buyer_Cart_Range = range(0,len(Buyer_Cart),1)
                print( "======================================================================" )
                print( "      Item       |    Amount     |   Price of 1Kg   |      Total      " )
                print( "======================================================================" )
                for Buyer_Cart_iter in Buyer_Cart_Range :
                    Buyer_Tuple = Buyer_Cart[Buyer_Cart_iter]
                    Total_Recript += Buyer_Tuple[3]
                    print( " ",Buyer_Tuple[0] , "    |     " , Buyer_Tuple[1] , "      |       " , Buyer_Tuple[2] , "       |      " ,  Buyer_Tuple[1] * Buyer_Tuple[2]  )
                print( "======================================================================" )
                print( "                         Total   =  " , Total_Recript )
                print( "======================================================================" )
                Buyer_Feature = 0
            else :
                break
    else :
        print( "==========================" )
        print( "==========================" )
        print( "=====    Good Bey    =====" )
        print( "==========================" )
        print( "==========================" )
        break
