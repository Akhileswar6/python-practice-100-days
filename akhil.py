"""1.program to find max number without using in-built function"""
list=[3,7,9,8,87,32,12]
max=0
for i in list:
    if i>max:
        max=i
print(max)

"""2.find intersection/common elements between two lists"""
nums1=[1,2,2,5]
nums2=[2,2]
intersection=[]
for i in nums1:
    if i in nums2:
        intersection.append(i)
print(intersection)

"""3.find unique elements without using in-built function"""
nums1=[78,73,89,8,6,12,44]
nums2=[73,78,89,6,8]
intersection=[]
for i in nums1:
    if i not in nums2:
        intersection.append(i)
print(intersection)

"""4.program to convert the below string 
s='11101011110' to CAD"""
S="11101011110"
count=0
for i in S:
    if i=="1":
        count=count+1
    else:
        print(chr(64+count),end="")
        count=0

"""5.write a program to convert the below string
n=43 value:7 --> 4+3 output:prime"""
n=43
num=0
while n>0:
    last = n%10
    num=num+last
    n=n//10
print(num)
for i in range(2,num):
    if num%i==0:
        print("Not a prime")
else:
    print("Prime")

"""6.write a program to convert string in format"""
str = "I AM STRONG"
reverse = str[::-1]
words=reverse.split()
for word in words:
    print(len(word),word)

"""7.write a program to reverse a number"""
n=765493
reverse=0
while n>0:
    last=n%10
    reverse=reverse*10+last
    n=n//10
print(reverse)

"""8.write a program to check given number is palindrome or not"""
str="MALAYALAM"
reverse=str[::-1]
if str==reverse:
    print("Palindrome")
else:
    print("Not palindrome")

"""9.write a program to find factorial"""
n = 6
fact = 1
if n >= 0:
    if n == 0:
        print(fact)
    else:
        for i in range(1, n+1):
            fact = fact * i
print(fact)

"""10.write a program to find perfect number"""
n=int(input("Enter a number:"))
perfect=0
for i in range(1,n):
    if n%i==0:
        perfect=perfect+i
if(perfect==n):
    print("perfect number")
else:
    print("not number")

"""11.write a program to find the frequency of character in string"""
n="programming"
char="m"
count=0
for i in n:
    if i==char:
        count+=1
print(count)

"""12.guess the output"""
n=123
sum=0
while n>0:
    last=n%10
    sum=sum+last
    n=n//10
print(sum)

"""13.guess the output"""
text1="learning python"
text2="python"
if text2 in text1:
    print("Exists")
else:
    print("Not Exists")

"""14.write a program to find fibonacci series"""
n=6
if n>0:
    a=0
    b=1
    print(a,b,end=" ")
    n=n-2
    if n>2:
        for i in range(n):
            temp=a+b
            a=b
            b=temp
            print(temp,end=" ")

"""15.write a program to print prime numbers"""
n=100
for i in range(2,n+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i,end=" ")

"""16.count the number of elements in heights that are not in their expected sorted order"""
heights=[1,1,4,2,1,3,5]
expected=[1,1,1,2,3,4,6]
count=0
n=len(heights)
for i in range(n):
    if heights[i]!=expected[i]:
        count+=1
print(count)

"""17.write a program to print duplicate values"""
my_list=[1,1,23,4,5,6,12,12,9]
unique=[]
duplicate=[]
for i in my_list:
    if i not in unique:
        unique.append(i)
    else:
        duplicate.append(i)
print(duplicate)

"""18.write a program to print reverse the given array/list"""
nums=[1,2,8,4,5,6,7]
print(nums)
n=len(nums)-1
for i in range(n//2):
    temp=nums[i]
    nums[i]=nums[n-i]
    nums[n-i]=temp
print(nums)

"""19.write a program to find sum of elements at even index positions after reversing an array"""
arr=[10,20,30,40,50,60]
n=len(arr)
sum=0
arr.reverse()
for i in range(n):
    if i%2==0:
        sum+=arr[i]
print(sum)

"""20.write a program to find maximum consecutive 1 in list"""
nums=[1,1,0,1,1,1,1,0]
count=0
max=0
for i in nums:
    if i==1:
        count+=1
        if count>=max:
            max=count
    else:
        max=count
        count=0
print(max)

"""21.Write a program to find leap year or not"""
n=int(input("enter a year:"))
if (n%4==0 and n%100!=0) or (n%400==0):
    print("Leap Year")
else:
    print("Not a leap Year")


"""22.Write a program which takes n integer in as input and returns the sum of prime numbers less than n"""
n=int(input("enter a number:"))
sum=0
for i in range(2,n):
    is_prime= True
    for j in range(2,int(i**0.5)+1):
        if (i%j==0):
            is_prime=False
            break
    if is_prime:
        sum+=i
print(sum)

"""23.Write a program to print median of sorted arrays"""
nums1=[1,2]
nums2=[3,4]
nums=nums1+nums2
nums.sort()
n=len(nums)
if n%2==0:
    median=(nums[n//2-1]+nums[n//2])/2
else:
    median=nums[n//2]
print(median)

"""24.Write a program to print sum between 0 to 0 from given array."""
nums=[0,1,0,3,0,2,2,0]
sums=[]
current_sum=0
in_between=False
for num in nums:
    if num ==0:
        if in_between:
            sums.append(current_sum)
            current_sum=0
        in_between=True
    else:
        if in_between:
            current_sum+=num
print(sums)






            
    

