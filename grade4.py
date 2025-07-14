# level 4
while True:

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

   # you see and observe teriminal has change a output  only changing in Break function
     Exit = input("Exit program (y/n) :").lower()  
     if Exit == "n":
        print ("bye bye ")
        break   
    