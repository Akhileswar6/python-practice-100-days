#1.program to find max number without using in-built function
list=[3,7,9,8,87,32,12]
max=0
for i in list:
    if i>max:
        max=i
print(max)

#2.find intersection/common elements between two lists
nums1=[1,2,2,5]
nums2=[2,2]
intersection=[]
for i in nums1:
    if i in nums2:
        intersection.append(i)
print(intersection)

#3.find unique elements without using in-built function
nums1=[78,73,89,8,6,12,44]
nums2=[73,78,89,6,8]
intersection=[]
for i in nums1:
    if i not in nums2:
        intersection.append(i)
print(intersection)

#4.program to convert the below string s='11101011110' to CAD
S="11101011110"
count=0
for i in S:
    if i=="1":
        count=count+1
    else:
        print(chr(64+count),end="")
        count=0

#5.write a program to convert the below string n=43 value:7 --> 4+3 output:prime
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

#6.write a program to convert string in format
str = "I AM STRONG"
reverse = str[::-1]
words=reverse.split()
for word in words:
    print(len(word),word)

#7.write a program to reverse a number
n=76549
reverse=0
while n>0:
    last=n%10
    reverse=reverse*10+last
    n=n//10
print(reverse)

#8.write a program to check given number is palindrome or not
str="MALAYALAM"
reverse=str[::-1]
if str==reverse:
    print("Palindrome")
else:
    print("Not palindrome")

#9.write a program to find factorial
n = 6
fact = 1
if n >= 0:
    if n == 0:
        print(fact)
    else:
        for i in range(1, n+1):
            fact = fact * i
print(fact)

#10.write a program to find perfect number
n=int(input("Enter a number:"))
perfect=0
for i in range(1,n):
    if n%i==0:
        perfect=perfect+i
if(perfect==n):
    print("perfect number")
else:
    print("not number")

#11.write a program to find the frequency of character in string
n="programming"
char="m"
count=0
for i in n:
    if i==char:
        count+=1
print(count)

#12.guess the output
n=123
sum=0
while n>0:
    last=n%10
    sum=sum+last
    n=n//10
print(sum)

#13.guess the output
text1="learning python"
text2="python"
if text2 in text1:
    print("Exists")
else:
    print("Not Exists")

#14.write a program to find fibonacci series
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

#15.write a program to print prime numbers
n=100
for i in range(2,n+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i,end=" ")

#16.count the number of elements in heights that are not in their expected sorted order
heights=[1,1,4,2,1,3,5]
expected=[1,1,1,2,3,4,6]
count=0
n=len(heights)
for i in range(n):
    if heights[i]!=expected[i]:
        count+=1
print(count)

#17.write a program to print duplicate values
my_list=[1,1,23,4,5,6,12,12,9]
unique=[]
duplicate=[]
for i in my_list:
    if i not in unique:
        unique.append(i)
    else:
        duplicate.append(i)
print(duplicate)

#18.write a program to print reverse the given array/list
nums=[1,2,8,4,5,6,7]
print(nums)
n=len(nums)-1
for i in range(n//2):
    temp=nums[i]
    nums[i]=nums[n-i]
    nums[n-i]=temp
print(nums)

#19.write a program to find sum of elements at even index positions after reversing an array
arr=[10,20,30,40,50,60]
n=len(arr)
sum=0
arr.reverse()
for i in range(n):
    if i%2==0:
        sum+=arr[i]
print(sum)

#20.write a program to find maximum consecutive 1 in list
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

#21.Write a program to find leap year or not
n=int(input("enter a year:"))
if (n%4==0 and n%100!=0) or (n%400==0):
    print("Leap Year")
else:
    print("Not a leap Year")


#22.Write a program which takes n integer in as input and returns the sum of prime numbers less than n
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

#23.Write a program to print median of sorted arrays
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

#24.Write a program to print sum between 0 to 0 from given array
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

#25.Write a program to print "True" if an array contains 3 consecutive odd numbers or "false"
nums=[1,2,3,4,5,6,7,8,9]
n=len(nums)
count=0
for i in nums:
    if i%2!=0:
        count=count+1
        if count>=3:
            print("True")
            break
    else:
        count=0
if count<3:
    print("False")
    
#26.Write a program to print if the characters in str2 is present in str1 or not
str1="abcd"
str2="abcde"
for i in str2:
  if i not in str1:
    print(i)

#27.Write a program to find given two strings are anagram or not
str1="rat"
str2="tar"
str1=sorted(str1)
str2=sorted(str2)
n=len(str1)
if len(str1)!=len(str2):
  print("not anagram")
else:
  for i in range(n):
    if str1[i]!=str2[i]:
      print("not anagram")
      break
    else:
      print("anagram")

#28.Write a program to find sum of cubes from given range
a=4
b=9
sum_of_cubes=0
for i in range(a,b+1):
  sum_of_cubes+=i**3
print(sum_of_cubes)

#30.Write a program to print "nums=['H','e','l','l','o'] O/P=['o','l','l','e','h']
nums=['H','e','l','l','o'] 
n=len(nums)-1
print(n)
for i in range(n//2):
    temp=nums[i]
    nums[i]=nums[n-i]
    nums[n-i]=temp
print(nums)

#31.Given a list of integers, move all zeros to the end while preserving the order of non-zero elements
nums=[0,1,0,3,12,0,0,6,8]
n=len(nums)
left=0
for i in range(n):
    if nums[i]!=0:
        temp=nums[i]
        nums[i]=nums[left]
        nums[left]=temp
        left+=1
print(nums)

#32.Given a list of integers, search the integer in the given list
nums=[0,1,2,4,12]
search=4
n=len(nums)
for i in range(n):
    if nums[i]==search:
        print(f"{search} found at index {i}")
        break
else:
    print(f"{search} not found in list")

#33.Given a list of integers, find the min element and it's index
nums=[3,4,2,6,7,1,8]
n=len(nums)#29.A string is valid if every opening bracket has a matching closing bracket and they are correctly nested.
s="(]"
new=""
n=len(s)
for i in range(0,n,2):
    if (s[i]=="(" and s[i+1]==")") or (s[i]=="[" and s[i+1]=="]") or (s[i]=="{" and s[i+1]=="}"):
        new+=s[i]
        new+=s[i+1]
    else:
        print("False")
        b
min=nums[0]
for i in range(n):
    if nums[i]<min:
        min=nums[i]
        index=i
print(f"Min element: {min} Index: {index}")
    
#34.Write a program to print below output without uisng slicing method
str="syncfusion"
n=len(str)
count=0
word=""
for i in range(n):
    if count==4:
        print(word)
        count=1
        word=''
    else:
        count=count+1
    word=word+str[i]
    
print("akhil")
