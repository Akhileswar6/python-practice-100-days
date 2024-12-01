"""1.program to find max number without using in-built function"""
# list=[3,7,9,8,87,32,12]
# max=0
# for i in list:
#     if i>max:
#         max=i
# print(max)

"""2.find intersection/common elements between two lists"""
# nums1=[1,2,2,5]
# nums2=[2,2]
# intersection=[]
# for i in nums1:
#     if i in nums2:
#         intersection.append(i)
# print(intersection)

"""3.find unique elements without using in-built function"""
# nums1=[78,73,89,8,6,12,44]
# nums2=[73,78,89,6,8]
# intersection=[]
# for i in nums1:
#     if i not in nums2:
#         intersection.append(i)
# print(intersection)

"""4.program to convert the below string 
s='11101011110' to CAD"""
# S="11101011110"
# count=0
# for i in S:
#     if i=="1":
#         count=count+1
#     else:
#         print(chr(64+count),end="")
#         count=0

"""5.write a program to convert the below string
n=43 value:7 --> 4+3 output:prime"""
# n=43
# num=0
# while n>0:
#     last = n%10
#     num=num+last
#     n=n//10
# print(num)
# for i in range(2,num):
#     if num%i==0:
#         print("Not a prime")
# else:
#     print("Prime")

"""6.write a program to convert string in format"""
# str = "I AM STRONG"
# reverse = str[::-1]
# words=reverse.split()
# for word in words:
#     print(len(word),word)

"""7.write a program to reverse a number"""
# n=765493
# reverse=0
# while n>0:
#     last=n%10
#     reverse=reverse*10+last
#     n=n//10
# print(reverse)

"""8.write a program to check given number is palindrome or not"""
# str="MALAYALAM"
# reverse=str[::-1]
# if str==reverse:
#     print("Palindrome")
# else:
#     print("Not palindrome")

"""9.write a program to find factorial"""
# n = 6
# fact = 1
# if n >= 0:
#     if n == 0:
#         print(fact)
#     else:
#         for i in range(1, n+1):
#             fact = fact * i
# print(fact)

"""10.write a program to find perfect number"""
# n=int(input("Enter a number:"))
# perfect=0
# for i in range(1,n):
#     if n%i==0:
#         perfect=perfect+i
# if(perfect==n):
#     print("perfect number")
# else:
#     print("not number")

"""11.write a program to find the frequency of character in string"""
# n="programming"
# char="m"
# count=0
# for i in n:
#     if i==char:
#         count+=1
# print(count)


