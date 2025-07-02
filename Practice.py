############################# Simple calculater #############################

# n1 = input("Enter a string: ")
# n2 = input("Enter a string: ")

# a = int(n1)
# b = int(n2)

# ch = int(input("Enter your choice: "))

# if(ch == 1):
#     print(a+b)
    
# elif(ch == 2):
#     print(a-b)

# elif(ch == 3):
#     print(a*b)

# elif(ch == 4):
#     if(b !=0 ):
#         print(a/b)
#     else:
#         print("Error.. Cannot devide by zero.")
    
# else:
#     ("Wront input..")
 
############################# Age in months #############################

# name = input("Enter your name: ")
# age =  int(input("Enter your age: "))

# print(name, "your are", age * 12, "months old.")
    
############################# Student's Grade #############################

# phy = int(input("Enter your phy marks: "))
# chem = int(input("Enter your chem marks: "))
# bio = int(input("Enter your bio marks: "))

# marks = (phy+chem+bio)/3

# if(marks >= 90):
#     grade = "A"

# elif(marks <= 89 and marks >= 70):
#     grade = "B"
    
# elif(marks <= 69 and marks >= 50):
#     grade = "C"
    
# elif(marks <= 49 and marks >= 40):
#     grade = "D"
    
# elif(marks <= 39 and marks >= 35):
#     grade = "Pass"
 
# else:
#     grade = "Better luck next time.."

# print("Your marks is", marks, "and grade is", grade)

############################# Login Authentication check #############################

# username = "yashsb"
# password = 123

# user = input("Enter your username: ")
# passs = int(input("Enter your password: "))

# if(user == username and passs == password):
#     print("Access Granted..")
# else:
#     print("Access Denied..")

############################# List #############################

# student_scores = [1,2,4,5,7,3,2,6,8,2,7,2]

# student_scores.append(90)
# student_scores.sort()
# print(student_scores[3:len(student_scores)])
# student_scores[4:len(student_scores)] = [1,1,1,1,1,1,1]
# print(student_scores)


# num = []

# n1 = int(input("Enter n1: "))
# n2 = int(input("Enter n2: "))
# n3 = int(input("Enter n3: "))
# n4 = int(input("Enter n4: "))
# n5 = int(input("Enter n5: "))

# num.append(n1)
# num.append(n2)
# num.append(n3)
# num.append(n4)
# num.append(n5)

# num.sort()
# print(num)
                            
############################# Set & Dict #############################

# student_roll_no = {1, 2, 3, 4, 5, 6, 7}

# print(type(student_roll_no))

# student_marks = {
    
#     "Yash" : 95,
#     "Sakshi" : 99,
#     "Ritika" : 100
# }

############################# String & Slicing #############################

# str = "hi yash how are you"
# x = str.endswith("u")
# print(x)


""" Simple Calculator App """

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# op = input("Enter an operator (+, -, *, /): ")

# if op == "+":
#     value = num1 + num2

# elif op == "-":
#     value = num1 - num2    

# elif op == "*":
#     value = num1 * num2

# elif op == "/":
#     if num2 != 0:
#         value = num1 / num2
#     else:
#         print("Error: Division by zero is not allowed.")
#         value = None
# else:
#     print("Error: Invalid operator.")
#     value = None

# if value is not None:
#     print(value)

""" Student Grading System """

# marks = {}

# phy = int(input("Enter phy marks: "))
# chem = int(input("Enter chem marks: "))
# math = int(input("Enter math marks: "))

# marks = (phy + chem + math) / 3

# if(marks >= 90):
#     grade = "A"

# elif(marks >= 80 and marks < 90):
#     grade = "B"

# elif(marks >= 60 and marks < 80):
#     grade = "C"

# elif(marks >= 40 and marks < 60):
#     grade = "D"

# elif(marks >= 35 and marks < 40):
#     grade = "Pass"

# else:
#     grade = "Fail."

    
# marks["phy"] = grade

# print(marks)


    


