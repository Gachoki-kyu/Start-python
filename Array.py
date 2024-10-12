# An array is a variable that can more than one value at a time
cars = ['ford','bmw','honda']
print(cars) #prints all the values
x = cars[0]
print(x) # prints the first value which has index 0 
cars[2] = 'volvo'# changes honda to volvo
print(cars)

cars.append('nissan') #add nissan into cars
print(cars)

cars.pop(2) #removes the third element you can also use cars.remove('volvo')
print(cars)