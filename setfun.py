s1={1,5,13,19,38,64,252}
s2={6,9,26,57,111,136,158}
s={110,164,256,354}
print("The orginal set s1 is:",s1)
print("The orginal set s2 is:",s2)
s2.update(s)
print("The updated set is;",s2)
s1.pop()
print("The popped set is:",s1)
s2.clear()
print("The cleared set is:",s2)
s1.remove(252)
print("After removing the 252 is:",s1)
