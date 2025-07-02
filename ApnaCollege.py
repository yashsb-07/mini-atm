#####################################################################################
                            # Lecture First
#####################################################################################
# Question

# a = int(input("Enter first no: "))
# b = int(input("Enter second no: "))

# sum = a + b
# print(sum)

# Question

# side = float(input("Enter side of square"))
# print("Area: ", side*side)

# Question

# a = float(input("Enter 1st: "))
# b = float(input("Enter 2nd: "))

# print("Average: ", (a+b)/2)

# a = int(input("Enter 1st: "))
# b = int(input("Enter 2nd: "))

# print(a>=b)

#####################################################################################
                            # Lecture Second
#####################################################################################
# Question

# first_name = input("Enter your name: ")
# print(len(first_name))

# Question

# str = "Hi i am $ and you ?"
# print(str.count("$"))

# Question

# num = int(input("Enter a number: "))

# if(num % 2 == 0):
#     print("Number is even")
# else:
#     print("number is odd")

# Question

# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter a number: "))
# num3 = int(input("Enter a number: "))

# if(num1 >= num2):
#     print("Num1 is great.")
# elif(num2 >= num3):
#     print("Num2 is great.")
# else:
#    print("Num3 is great.")

#####################################################################################
                            # Lecture Third
#####################################################################################
# Question

# movies = []

# mov1 = input("Fav Movies: ")
# mov2 = input("Fav Movies: ")
# mov3 = input("Fav Movies: ")

# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)

# print(movies)

# Question

# list = ["r","a","c","e","c","a","r"]

# copy_list = list.copy()
# copy_list.reverse()

# if(copy_list == list):
#     print("palindrome")
# else:
#     print("not a palindrome")

# Question

# tuple = ("c","d","a","a","b","b","a")
# print(tuple.count("b"))

# Question

# list = ["c","d","a","a","b","b","a"]
# list.sort(reverse=True)
# print(list)

#####################################################################################
                            # Lecture Four
#####################################################################################
# Question

# dict = {
#     "table" : "a piece of furniture", 
#     "cat" : [" a small animal", "list of facts and figures"]  
# }
# print(dict)

# Question

# subject = {"python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"}
# print(len(subject))

# Question

# marks = {}

# x = int(input("Enter phy: "))
# marks.update({"phy: ": x})

# x = int(input("Enter chem: "))
# marks.update({"cehm: ": x})

# x = int(input("Enter math: "))
# marks.update({"math: ": x})

# print(marks)

#####################################################################################
                            # Lecture Five
#####################################################################################
# Question

# i = 1

# while i <= 100:
#     print(i)
#     i += 1

# Question

# i = 100

# while i >= 1:
#     print(i)
#     i -= 1

# Question
# n = 10
# i = 1

# while i <= 10:
#     print(n*i)
#     i += 1

# Question

# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    
# idx = 0
# while idx < len(nums):
#     print(nums[idx])
#     idx += 1

# Question

# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100,36, 78, 887, 36, 887, 88, 36)

# x = 36
# i = 0

# while i < len(nums):
#     if(nums[i] == x):
#         print("Found at index ", i)
#     else:
#         print("Finding..")
#     i += 1

# Question

# i = 1

# while i <= 5:
#     print(i)
#     if(i == 3):
#         break
#     i += 1

# Question

# nums = (1,2,3,4,5,6,7,8,9)

# for el in nums:
#     print(el)

# Question

# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100,36, 78, 887, 36, 887, 88, 36)

# x = 49

# for el in nums:
#     if(el == x):
#         print(x)

# Question

# for i in range(1, 101):
#     print(i)
    
# for i in range(100, 0, -1):
#     print(i)

# n = 6
    
# for i in range(1, 11):
#     print(n*i)

# Question

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

#####################################################################################
                            # Lecture Six
#####################################################################################

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

#####################################################################################
                            # Lecture Seven
#####################################################################################

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

#####################################################################################
                            # Lecture Eight
#####################################################################################

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