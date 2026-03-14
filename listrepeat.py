list1=[1,3,7,5,6,8,7,1,9,6,2]
list2=[]
a=int(input("Enter the element"))
for i in range(len(list1)):
   if list1[i]==a:
      list2.append(i) 
print("The value is found at index of",list2)
print(a,"occurng is",list1.count(a))

