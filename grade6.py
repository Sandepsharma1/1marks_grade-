#  level 6 
# That is using a def advance function 
# mid level 

def grade_1():
    return("That grade is : A")

def grade_2():
    return("That grade is : B")

def grade_3():
    return("That grade is : C")

def grade_4():
    return("That grade is : D")

def grade_5():
    return("That grade is : F")


choice = float(input("Enter the grade marks number :"))

if choice >= 90:
    print(grade_1())
elif choice >= 70:
    print(grade_2())
elif choice >= 50:
    print(grade_3())
elif choice >= 35:
    print(grade_4())     
else:
    print(grade_5())    


def main():
    
    grade_1()
    grade_2()
    grade_3()
    grade_4()
    grade_5()
    

main()    