def intrest(a,b,c):
   c=int(input("Enter the age:"))
   a=int(input("Enter the principle amount:"))
   b=int(input("Enter the time:"))
   if(c>60):
      d=0.12
      simpleint=(a*d*b)/100
      print("The value is",simpleint)
   else:
      d=0.1
      simpleint=(a*d*b)/100
      print("the value is",simpleint)
intrest(1,3,4)
