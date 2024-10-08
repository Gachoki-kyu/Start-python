#lists

mylist = ["mango","banana","apple"]
print(mylist) #print the list
print(len(mylist)) #print the length
thislist = list(("kenya", 'uganda','tanzania')) # using list() constructor. NOTE the double blackets
print(thislist)
print(type(thislist)) # show type which is a list
thislist.append("egypt")
print(thislist)
for x in thislist:
 print(x)