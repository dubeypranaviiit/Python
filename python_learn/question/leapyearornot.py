year=int(input("Enter the year:"))
if(year%4==0) :
    if(year%100==0 and year%400==0 ) :
        print("Leap year",year)
    elif(year%100 ==0 and year%400 !=0 ) :
        print("Not a neap year")
    else:
        print("Print leap year")
else:
    print("Not a leap year")
