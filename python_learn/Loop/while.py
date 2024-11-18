 #display all the digits from 0 to 10 in ascending order
i=0
while (i<=10) :
    print(i)
    i=i+1

     # 10 to 0 in descending order

j=10
while (j>=0) :
    print(j)
    j=j-1

 # Strip the first 2 characters of a string and print result
#  • E.g. SaReGaMaPa   

s="SaReGaMaPa"
i=2
while(len(s)>2) :
    print(s[i:])
    s =s[2:]