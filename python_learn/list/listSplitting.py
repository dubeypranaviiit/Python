import re
str ="Ram Kam";
# print(type(str));
# ls_conversion =str.split();
# print(ls_conversion)
# print(type(ls_conversion));
# print(ls_conversion)
# ls=str.split('d')
# print(ls)

# lb=str.split('n')
# print(lb)
lc=re.split('(a)',str)
print(lc)
#string to list using list constructor()
a=list(str)
print(a)