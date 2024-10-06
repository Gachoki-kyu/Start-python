# accessing element of a string
a = "this is a string"
print(a[0]) #return the first element of a string
print(len(a)) #return the lrngth of the 

txt = "to check if there is a string"
print("check" in txt) # check for a string in a sentence returns true or false
if "check" in txt:
    print("yes! check is in the string")
print(txt.upper())

#looping through a string
for x in "kenya":
 print(x)

con = "this is a crazy world we living"
print(con.split("is")) 

print(con + txt) #concantination