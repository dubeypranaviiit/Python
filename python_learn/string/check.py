# a=input("Enter your string")
# b=input("What you want to search")

# print(b in a)
# if (b in a) :
#     print("true")
# string = "python PROgramming"
# capitalized = string.capitalize()
# print(capitalized)  # Output will be "Python programming"
# def contains_vowels(s):
#     vowels = "aeiouAEIOU"
#     for char in s:
#         print(char)
#         # if char in vowels:
#         #     return True
#     return False

# result = contains_vowels("hello")
# print(result) 
# Strip the first 2 characters of a string and print result
#  SaReGaMaPa
#  ReGaMaPa
#  GaMaPa
#  MaP

# s="SaReGaMaPa"
# j=len(s)
# i=0
# while j>=2 :
#     str=s[i:]
#     print(str)
#     i=i+2
#     j=j-2
# x = 0b11011000
# print(x)

# x = 0b_1101_1000
# print(x)
# print(type(x))
# b=-7%2 
# b=7%2
# print(b)
# for j in range(10,5,-2):
# 	print(j)
# L1=[1,2,3,4,5]
# L2=[5,4,3,2,1]
# L3=L1+L2
# print(L1,'\n',L2,'\n',L3)
# L1=[1,2,3,4,5]
# L2=[]
#L2=L2+L1 #or L2[:]=L1 #( Both are valid statements)
# L2[:]=L1
# L1[1]=6
# print(L1,'\n',L2)

# L1=[1,3,[11,13,15,[17,19],21],5,7]
# print(L1)
# print(L1[0:3])
# print(L1[2])
# print(L1[2][0])
# print(L1[2][3])
# print(L1[2][3][0])
# S='UNPACK Me'
# S1=[*S]
# print(S1)
# s="UNPACK Me"
# s1=s.split()
# print(s1)
# L1=['HI',"RR"]
# L3=[7,8,9,*L1,10]
# print(L3)
l1=[1,2,3]
l2=list({1,2,3})
print(id(l1))
print(id(l2))

l1=[1,2,3,[5,6]]
l2=l1
l2[2]=5
# l2=[1,2,3]
print(l1)
print(l1)

n=int(input())
fac=1
for i in range(1,n+1):
#    print(i)
   if (i==0 and i==1):
      fac=1
   else:
      fac*=i

print(fac)





