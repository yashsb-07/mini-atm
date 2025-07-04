################################## Question ##################################

# a = int(input("Enter first no: "))
# b = int(input("Enter second no: "))

# sum = a + b
# print(sum)

################################## Question ##################################

# side = float(input("Enter side of square"))
# print("Area: ", side*side)

# Question

# a = float(input("Enter 1st: "))
# b = float(input("Enter 2nd: "))

# print("Average: ", (a+b)/2)

# a = int(input("Enter 1st: "))
# b = int(input("Enter 2nd: "))

# print(a>=b)

################################## Question ##################################

# first_name = input("Enter your name: ")
# print(len(first_name))

# name = input("Enter your name: ")
# print(len(name))

# word = input("Enter a string: ")
# print(word.count("$"))

# count = 1
# while count <= 5:
#     print("Hello")
#     count += 1

# print(count)

# nums = [1,2,3,45,2,3,24,56,75,34,65,3,343,434,45,4,6565,6,54]

# idx = 0
# while idx < len(nums):
#     print(nums[idx])
#     idx += 1

# tup = (1,4,9,16,25,36,49,64,81,100)

# x = 0
# i = 0

# while i < len(tup):
#     if(tup[i] == x):
#         print("Found")
#     else:
#         print("Not found")
#     i += 1

# for i in range(2, 20, 2):
#     print(i)

# for i in range(2,21,2):
#     print(i)
#     i += 1

# word = "python"
# for i in word:
#     print(i)

# sum = 0

# for i in range(1,101):
#     sum += i
#     print(sum)

# users_pass = input("Enter your pasword: ")

# password = "Yashsb07" 

# while users_pass != password:
#     print("password is incorrect")
#     users_pass = input("Enter your pasword: ")
# print("password is correct.")
    
# str = input("Enter your stirng: ")

# vowels = "aeiouAEIOU"

# count = 0

# for ch in str:
#     if ch in vowels:
#         count += 1
        
# print("Vowels of count is: ", count)

# num = int(input("Enter a nuber: "))

# for i in range(1, 11):
#     print(num*i)
 
# list = [1,2,3,4,4,5,56,67,7]

# for num in list:
#     if(num % 2 == 0):
#         print(num)

# cities = ["pune", "delhi", "banglore", "chennai"]

# def print_len(cities):
#     print(len(cities))
    
# print_len(cities)

# def cal_fact(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     print(fact)
    
# cal_fact(6)

# def converter(USD):
#     INR = USD * 83
#     print("USD =", USD, "INR =", INR)
    
# converter(900)

# num = int(input("Enter your number: "))

# def define_num(num):
#     if(num % 2 == 0):
#         print("Number is even.")
#     else:
#         print("Number is odd.")

# define_num(num)

# def calc_sum(n):
#     if(n == 0):
#         return 0
#     return calc_sum(n-1) + n

# sum = calc_sum(5)
# print(sum)
    
# cities = ["Pune", "Delhi", "Banglore", "Hydrabad", "Chennai"]

# def print_list(list, idx=0):
#     if(idx == len(list)):
#         return
#     print(list[idx])
#     print_list(list, idx+1)

# print_list(cities)
    
# for line in range(5, 0, -1):
#     print("*" * line)
 

################################## Question ##################################

# str = "Hi i am $ and you ?"
# print(str.count("$"))

################################## Question ##################################

# num = int(input("Enter a number: "))

# if(num % 2 == 0):
#     print("Number is even")
# else:
#     print("number is odd")

################################## Question ##################################

# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter a number: "))
# num3 = int(input("Enter a number: "))

# if(num1 >= num2):
#     print("Num1 is great.")
# elif(num2 >= num3):
#     print("Num2 is great.")
# else:
#    print("Num3 is great.")

################################## Question ##################################

# movies = []

# mov1 = input("Fav Movies: ")
# mov2 = input("Fav Movies: ")
# mov3 = input("Fav Movies: ")

# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)

# print(movies)

################################## Question ##################################

# list = ["r","a","c","e","c","a","r"]

# copy_list = list.copy()
# copy_list.reverse()

# if(copy_list == list):
#     print("palindrome")
# else:
#     print("not a palindrome")

################################## Question ##################################

# tuple = ("c","d","a","a","b","b","a")
# print(tuple.count("b"))

################################## Question ##################################

# list = ["c","d","a","a","b","b","a"]
# list.sort(reverse=True)
# print(list)

################################## Question ##################################

# dict = {
#     "table" : "a piece of furniture", 
#     "cat" : [" a small animal", "list of facts and figures"]  
# }
# print(dict)

################################## Question ##################################

# subject = {"python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"}
# print(len(subject))

################################## Question ##################################

# marks = {}

# x = int(input("Enter phy: "))
# marks.update({"phy: ": x})

# x = int(input("Enter chem: "))
# marks.update({"cehm: ": x})

# x = int(input("Enter math: "))
# marks.update({"math: ": x})

# print(marks)

################################## Question ##################################

# i = 1

# while i <= 100:
#     print(i)
#     i += 1

################################## Question ##################################

# i = 100

# while i >= 1:
#     print(i)
#     i -= 1

################################## Question ##################################
# n = 10
# i = 1

# while i <= 10:
#     print(n*i)
#     i += 1

################################## Question ##################################

# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    
# idx = 0
# while idx < len(nums):
#     print(nums[idx])
#     idx += 1

################################## Question ##################################

# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100,36, 78, 887, 36, 887, 88, 36)

# x = 36
# i = 0

# while i < len(nums):
#     if(nums[i] == x):
#         print("Found at index ", i)
#     else:
#         print("Finding..")
#     i += 1

################################## Question ##################################

# i = 1

# while i <= 5:
#     print(i)
#     if(i == 3):
#         break
#     i += 1

################################## Question ##################################

# nums = (1,2,3,4,5,6,7,8,9)

# for el in nums:
#     print(el)

################################## Question ##################################

# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100,36, 78, 887, 36, 887, 88, 36)

# x = 49

# for el in nums:
#     if(el == x):
#         print(x)

################################## Question ##################################

# for i in range(1, 101):
#     print(i)
    
# for i in range(100, 0, -1):
#     print(i)

# n = 6
    
# for i in range(1, 11):
#     print(n*i)

################################## Question ##################################

# n = 5
# sum = 0

# for i in range(1, n+1):
#     sum += i
#     print(sum)
    
# n = 5
# sum = 0
# i = 1
# while i <= n:
#     sum += i
#     i += 1
# print(sum)

# n = 5
# fact = 1

# for i in range(1, n+1):
#     fact *= i
# print(fact)

# n = 9
# fact = 1
# i = 1

# while i <= n:
#     fact *= i
#     i += 1
# print(fact)

# Average of 3 numbers

# def avg(a,b,c):
#     return (a+b+c)/3

# avg = avg(98,97,95)
# print(avg)

# nums = [2,4,5,6,7,8,9]
# cities = ["pune", "nashik", "mumbai", "delhi", "chennai"]

# def len_list(list):
#     print(len(list))

# len_list(nums)
# len_list(cities)

# cities = ["pune", "nashik", "mumbai", "delhi", "chennai"]
# nums = [2,4,5,6,7,8,9]

# def print_list(list):
#     for item in list:
#         print(item, end= " ")
        
# print_list(cities)
# print_list(nums)
        
# def calc_fact(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     print(fact)

# calc_fact(9)

# def converter(usd_value):
#     inr_value = usd_value * 83
#     print(usd_value, "USD = ", inr_value, "INR")

# converter(5)

# def num(a):
#     if(a % 2 != 0):
#         print("Odd")
#     else:
#         print("Even")

# num(100)

### Recursion ###

# def show(n):
#     if(n == 0):
#         return
#     print(n)
#     show(n-1)

# show(3)

# with open("practice.txt", "w") as f:
#     f.write("Hi everyone..\nwe are learning file I/O\nusing java.. ")
#     f.write("I like programming in java.")

# with open("practice.txt", "r") as f:
#     data = f.read()
    
# new_data = data.replace("java", "python")
# print(new_data)

# with open("practice.txt", "w") as f:
#     f.write(new_data)

# def FIO():
#     with open("practice.txt", "r") as f:
#         data = f.read()
    
#     new_data = data.replace("python", "Yash")
#     print(new_data)

#     with open("practice.txt", "w") as f:
#         f.write(new_data)
        
# FIO()        
    
# word = "learning"
# with open("practice.txt", "r")as f:
#     data = f.read()
#     if(data.find(word) != -1):
#         print("Found")
#     else:
#         print("Not found")

# def checking_word():
#     word = "lfjearning"
#     with open("practice.txt", "r")as f:
#         data = f.read()
#         if(data.find(word) != -1):
#             print("Found")
#         else:
#             print("Not found")
            
# checking_word()


# class Student:
#     name = "Yash"

# s1 = Student()
# print(s1.name)

# class Car:
#     color = "Black"
#     brand = "BMW"

# car = Car()
# print(car.color)
# print(car.brand)

# class Student:
#     def __init__(self, fullname):
#         self.name = fullname
        
# s1 = Student("Yash Sharad Bansode")
# print(s1.name)

# class Student: 
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
         
#     def welcome(self):
#         print("welcome", self.name)
        
#     def get_marks(self):
#         return self.marks
      
      
# s1 = Student("Yash", 97)
# s1.welcome()
# print(s1.get_marks())

# class Account:
#     def __init__(self, bal, acc):
#         self.balance = bal
#         self.acc_no = acc

#     def debit(self, amount):
#         self.balance -= amount
#         print("Rs.", amount, "Was Debited.")
#         print("Total balance is: ", self.get_bal())
    

#     def credit(self, amount):
#         self.balance += amount
#         print("Rs.", amount, "Was Credited.")
#         print("Total balance is: ", self.get_bal())
    
#     def get_bal(self):
#         return self.balance 

# acc = Account(10000, 12345)
# acc.debit(1000)
# acc.credit(200)
# acc.debit(4000)
# acc.credit(50000)


# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass
        
#     def reset_pass(self):
#         print(self.__acc_pass)
        
# acc1 = Account(12345, "Yashsb07")
# print(acc1.acc_no)
# print(acc1.reset_pass())
        
"""Multilevel Inheritance"""

# class Car:
#     @staticmethod
#     def start():
#         print("car started..")        
    
#     @staticmethod
#     def stop():
#         print("Car stopped.")
    
# class Fortuner(Car):
#     def __init__ (self, brand):
#         self.brand = brand
    
# class Toyota(Fortuner):
#     def __init__(self, type):
#         self.type = type

# car1 = Toyota("disel")
# print(car1.type)
# car1.start()
        
"""Multiple Inheritance"""

# class A:
#     varA = "Welcome to class A:"

# class B:
#     varB = "welcome to class B:"

# class C(A, B):
#     varC = "Welcome to class C:"

# c1 = C()

# print(c1.varA)
# print(c1.varB)
# print(c1.varC)

"""Super keyword"""

# class Car:
#     def __init__(self, type):
#         self.type = type

#     @staticmethod
#     def start():
#         print("Car Started..")

#     @staticmethod
#     def stop():
#         print("Car Stoped.")
        
# class Toyota(Car):
#     def __init__(self, name, type):
#         super().__init__(type)
#         self.name = name
#         super().start()

# car1 = Toyota("Prius", "Petrol")
# print(car1.type)

"""@classmethod"""

# class Person:
#     name = "anonymous"

#     @classmethod
#     def changeName(cls, name):
#         cls.name = name
        
# p1 = Person()
# p1.changeName("Yash Bansode")
# print(p1.name)
# print(Person.name)
        
"""@Propertymethod"""

# class Student:
#     def __init__(self, phy, chem, math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math
        
#     @property
#     def percentage(self):
#         return str((self.phy + self.chem + self.math) / 3) + "%"

# stu1 = Student(98, 97, 99)
# print(stu1.percentage)

# stu1.phy = 86 
# print(stu1.percentage)

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

# name = input("Enter your name: ")
# print(len(name))

# word = input("Enter a string: ")
# print(word.count("$"))

# count = 1
# while count <= 5:
#     print("Hello")
#     count += 1

# print(count)

# nums = [1,2,3,45,2,3,24,56,75,34,65,3,343,434,45,4,6565,6,54]

# idx = 0
# while idx < len(nums):
#     print(nums[idx])
#     idx += 1

# tup = (1,4,9,16,25,36,49,64,81,100)

# x = 0
# i = 0

# while i < len(tup):
#     if(tup[i] == x):
#         print("Found")
#     else:
#         print("Not found")
#     i += 1

# for i in range(2, 20, 2):
#     print(i)

# for i in range(2,21,2):
#     print(i)
#     i += 1

# word = "python"
# for i in word:
#     print(i)

# sum = 0

# for i in range(1,101):
#     sum += i
#     print(sum)

# users_pass = input("Enter your pasword: ")

# password = "Yashsb07" 

# while users_pass != password:
#     print("password is incorrect")
#     users_pass = input("Enter your pasword: ")
# print("password is correct.")
    
# str = input("Enter your stirng: ")

# vowels = "aeiouAEIOU"

# count = 0

# for ch in str:
#     if ch in vowels:
#         count += 1
        
# print("Vowels of count is: ", count)

# num = int(input("Enter a nuber: "))

# for i in range(1, 11):
#     print(num*i)
 
# list = [1,2,3,4,4,5,56,67,7]

# for num in list:
#     if(num % 2 == 0):
#         print(num)

# cities = ["pune", "delhi", "banglore", "chennai"]

# def print_len(cities):
#     print(len(cities))
    
# print_len(cities)

# def cal_fact(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     print(fact)
    
# cal_fact(6)

# def converter(USD):
#     INR = USD * 83
#     print("USD =", USD, "INR =", INR)
    
# converter(900)

# num = int(input("Enter your number: "))

# def define_num(num):
#     if(num % 2 == 0):
#         print("Number is even.")
#     else:
#         print("Number is odd.")

# define_num(num)

# def calc_sum(n):
#     if(n == 0):
#         return 0
#     return calc_sum(n-1) + n

# sum = calc_sum(5)
# print(sum)
    
# cities = ["Pune", "Delhi", "Banglore", "Hydrabad", "Chennai"]

# def print_list(list, idx=0):
#     if(idx == len(list)):
#         return
#     print(list[idx])
#     print_list(list, idx+1)

# print_list(cities)
    
# for line in range(5, 0, -1):
#     print("*" * line)
 
# """ Classes and objects """

# class Student:
#     name = "Yash"

# s1 = Student()
# print(s1.name)

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
    
# s1 = Student("Yash Bansode", 97)
# print(s1.name, s1.marks)

# s2 = Student("Sakshi", 100)
# print(s2.name, s2.marks)

"""Methods"""

# class Student():
#     def __init__(self, name , marks):
#         self.name = name
#         self.marks = marks
        
#     def welcome(self):
#         print("Welcome", self.name)
        
#     def get_marks(self):
#         return self.marks

# s1 = Student("Yash", 99)
# s1.welcome()
# print(s1.get_marks())

""" Question """

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
      
#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("Hi", self.name, "your avg score is: ", sum/3)
       
# s1 = Student("Yash", [79, 87, 69])
# s1.get_avg()

""" Abstraction """

# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False
        
#     def start(self):
#         self.acc = True
#         self.clutch = True
#         print("Car started..")

# car1 = Car()
# car1.start()
        
# class Account:
#     def __init__(self, bal, acc):
#         self.bal = bal
#         self.acc = acc
        
#     def debit(self, amt):
#         self.bal -= amt
#         print("Debit amount is: ", amt)
#         print("Total balance is: ", self.get_bal())
        
#     def credit(self, amt):
#         self.bal += amt
#         print("Credit amount is: ", amt)
#         print("Total balance is: ", self.get_bal())
        
#     def get_bal(self):
#         return self.bal     
        
# acc1 = Account(1000, 123456789)
# acc1.debit(130)
# acc1.credit(762)
# acc1.debit(256)
# acc1.credit(6576)

# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def bark(self):
#         print(f"{self.name} says woof!")
        
#     def get_age(self):
#         print(self.age)

# # Create an object
# my_dog = Dog("Buddy", 3)
# my_dog.bark() 

# dog1 = Dog("Tommy", 5)
# dog1.get_age()
           
           
""" Private"""

# class Person:
#     __name = "Yash Bansode"
    
#     def __hello(self):
#         print("Hello yash")
        
#     def yash(self):
#         self.__hello()

# p1 = Person()
# print(p1.yash())

""" Inheritance """

# class Car:
#     @staticmethod
#     def start():
#         print("Car Started..")

#     @staticmethod
#     def stop():
#         print("Cat Stopped.")

# class ToyotaCar(Car):
#     def __init__(self, name):
#         self.name = name

# car1 = ToyotaCar("Fortuner")
# print(car1.name)
# print(car1.start())
        
        
# class Car():
#     @staticmethod
#     def start():
#         print("Car started..")

#     @staticmethod
#     def stop():
#         print("Car stopped.")

# class Toyota(Car):
#     def __init__(self, brand):
#         self.brand = brand

# class Fortuner(Toyota):
#     def __init__(self, type):
#         self.type = type
        
# car1 = Fortuner("Petrol")
# car1.start()
# car2 = Toyota("BMW")
# print(car2.brand)

# class A:
#     varA = "Welcome to class A"

# class B:
#     varB = "Welcome to class B"

# class C(A, B):
#     varC = "Welcome to class C"

# c1 = C()
# print(c1.varA)
# print(c1.varB)
# print(c1.varC)

""" *args and **kwargs """

# def funargs(normal, *agrsyash, **kwargs):
#     print(normal)
#     for item in agrsyash:
#         print(item)
        
#     print("\nNow i want to introduce you some of our main persons in this company: ")
#     for key, value in kwargs.items():
#         print(f"{key} is a {value}")
        

# name = ["Yash", "Sakshi", "Bansode","How are you both of you ?"]
# normal= ("I am a normal argument in this function and the students are: ")
# kw = {"Yash":"S/W Engineer", "Sakshi":"CA"}
# funargs(normal, *name, **kw)

""" Super() """

# class Car():
#     def __init__(self, type):
#         self.type = type
        
#     @staticmethod
#     def start():
#         print("Car started..")

#     @staticmethod
#     def stop():
#         print("Car stopped.")

# class Fortuner(Car):
#     def __init__(self, brand, type):
#         super().__init__(type)
#         self.brand = brand
#         super().start()

# car1 = Fortuner("Toyota", "Petrol")
# print(car1.type)
# print(car1.brand)

""" @Classmethod """

# class Person():
#     name = "Yash"

#     @classmethod
#     def changeName(cls, name):
#         cls.name = name

# p1 = Person()
# p1.changeName("Sakshi")
# print(p1.name)
# print(Person.name)

""" @Property """

# class Student:
#     def __init__(self, phy, chem, math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math
        
#     @property
#     def percentage(self):
#         return str((self.phy + self.chem + self.math) / 3) + "%"

# std1 = Student(98, 97, 99)
# print(std1.percentage)

# std1.phy = 86
# print(std1.percentage)

""" Dunder Function """

# class Complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img
        
#     def showNumber(self):
#         print(self.real, "i +", self.img,"j")
        
#     def __add__(self, num2):
#         newReal = self.real + num2.real
#         newImg = self.img + num2.img
#         return Complex(newReal, newImg)
    
    # def __add__(self, num2):
    #     newReal = self.real - num2.real
    #     newImg = self.img - num2.img
    #     return Complex(newReal, newImg)


# num1 = Complex(3, 4)
# num1.showNumber()

# num2 = Complex(3, 4)
# num2.showNumber()

# num3 = num1 + num2
# num3.showNumber()

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
    
#     def Area(self):
#         return (22/7) * self.radius * self.radius
        
#     def Perimeter(self):
#         return 2 * (22/7)  * self.radius
        
# cir1 = Circle(21)
# print(cir1.Area())
# print(cir1.Perimeter())

# class Employee:
#     def __init__(self, role, dept, salary):
#         self.role = role
#         self.dept = dept
#         self.salary = salary
        
#     def showDetails(self):
#         print("Role =",self.role)
#         print("Dept =",self.dept)
#         print("Salary =",self.salary)
        
# class Engineer(Employee):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         super().__init__("CA", "Finance", "1,00,000")
        
        
# emp1 = Engineer()
# print(emp1.showDetails())

# class Order():
#     def __init__(self, items, price):
#         self.items = items
#         self.price = price
        
#     def __gt__(self, ord2):
#         return self.price > ord2.price
        
# ord1 = Order("Chips", 20)
# ord2 = Order("Kurkure", 3)

# print(ord1 > ord2)
