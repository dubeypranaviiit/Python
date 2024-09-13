height=float(input())
weight=float(input())

bmi=weight/(height * height)
if(bmi<3) :
    print("You are under weight")
elif(bmi<5) :
            print("Normal weight")
else :
        print("You are overweight")