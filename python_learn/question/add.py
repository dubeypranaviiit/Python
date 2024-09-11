# program to add  digit of a number
num =input("Enteer two digit number :")
print(type(num)) # since num is string so we can accsess through index
first_digit=num[0]
second_digit=num[1]
print(int(first_digit)+int(second_digit))