#functions in python
def my_fun(name):
    print("hello "+ name)
my_fun("ben")

def area(len,wid):
    return len*wid 
er = int(area(34,4))
print(er)

# recursive function
def my_recu(k):
 if k > 0:
  result = k + my_recu(k - 1)
  print(result)
 else:
  result = 0
 return result

print("recursive numbers:")
my_recu(6)