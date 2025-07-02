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
 