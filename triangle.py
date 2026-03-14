a=int(input("Enter the value of the 1 side"))
b=int(input("Enter the value of the 2 side"))
c=int(input("Enter the value of the 3 side"))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("The area of the triangle is",area)
