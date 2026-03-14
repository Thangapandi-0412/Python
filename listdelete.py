def even(x):
   if(x%2==0):
      return x
list1=[1,2,3,4,5,6,7,8,9,10]
print("The real list is",list1)
list2=list(map(even,list1))
print("The modified list is",list2)

