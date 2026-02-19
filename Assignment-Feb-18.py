# square pattern

# n=int(input("Enter n value:"))
# for j in range(n):
#     for i in range(n):
#         print("*",end=" ")
#     print()

#OUTPUT:
# Enter n value:5
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 

# Rectangle pattern

# n=int(input("Enter n value:"))
# for j in range(n):
#     for i in range(n*2):
#         print("*",end=" ")
#     print()

# OUTPUT:
# Enter n value:5
# * * * * * * * * * * 
# * * * * * * * * * * 
# * * * * * * * * * * 
# * * * * * * * * * * 
# * * * * * * * * * * 

#Hollow square

n=int(input("Enter n value:"))

for j in range(1,n+1):
    for i in range(1,n+1):
        if i==1 or j==1 or i==n or j==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


#Nearest prime number

# def Check_prime(n):
#     if n<2:
#         return False
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     return True

# n=int(input("Enter a number:"))

# if Check_prime(n):
#     print(n)
# else:
#     left=n-1
#     right=n+1
#     while True:
#         if Check_prime(left):
#             print(left)
#             break
#         if Check_prime(right):
#             print(right)
#             break
#         left-=1
#         right+=1

# OUTPUT:
# Enter a number:13
# 13
# Enter a number:14
# 13
# Enter a number:16
# 17