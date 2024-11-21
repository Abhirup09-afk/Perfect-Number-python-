#program to find Perfect Number
#Defination: A number that is equal to the sum of its proper divisors, 
# excluding itself. For example, 
# 28 is a perfect number because its divisors (1, 2, 4, 7, 14) sum to 28.

num = int(input("Enter a number: "))

a = 0 

for i in range(1, num):
    if num % i == 0:
        a += i

if a == num:
    print(f"{num} is a Perfect Number.")
else:
    print(f"{num} is not a Perfect Number")