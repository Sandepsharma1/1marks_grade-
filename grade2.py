# that is a level = 2 marks grade program code
#this used loop formula 

while True :
    user_choice = int(input ("Enter the gade marks number :"))

    if user_choice >=  90 :
        print("That grade is : A")
    elif user_choice >= 70:
        print("that grade is : B")    
    elif user_choice >= 50:
        print("Taht grade is : C")   
    elif user_choice >= 35:
        print("That grade is : D")

    else :
        print("That grade is :F")