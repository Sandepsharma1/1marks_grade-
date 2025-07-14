#This is level = 3 program grade 
#That is used loop and break function 


while True:

    Exit = input("Exit program (y/n) :").lower()  
    if Exit == "n":
        print ("bye bye ")
        break
    user_choice = int(input("Enter the grade marks :"))

    if user_choice  >=  90:
        print("That grade is : A")
    elif user_choice >= 70:    
        print("That grade is : B")
    elif user_choice >= 50:
        print("That grade is : C")    
    elif user_choice >= 35:
        print("That grade is : D")
    else :
        print("That grade is : F")        
   
    
