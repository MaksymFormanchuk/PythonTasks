import sys

def exist_check(a, b, c):
    if (a+b>c) and (b+c>a) and (a+c>b):
        str1 = "possible"
        return str1
    else:
        sys.exit("Triangle is not possible")
        


def type_check(a,b,c):
    if (c**2==a**2+b**2) or (a**2==c**2+b**2) or (b**2==a**2+c**2):
        str2 = "right"
    elif a==b==c:
        str2 = "equilateral"
    elif (a!=b) and (b!=c) and (c!=a):
        str2 = "scalene"
    else:
        str2 = "isosceles"
    return str2  


a = float(input("Enter side1:" ))
b = float(input("Enter side2:" ))
c = float(input("Enter side3:" ))

print("Triangle with such sides is " + exist_check(a, b, c))
print("Type of this triangle is " + type_check(a,b,c))