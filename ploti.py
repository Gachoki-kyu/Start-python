import matplotlib.pyplot as plt
import numpy as np

# ploting a single line
'''
x = np.array([0,6])
y = np.array([0,250])
'''
#ploting more that 2 points
'''
x = np.array([1,3,5,7])
y = np.array([7,3,8,1])
'''
# markers
'''
x = np.array([2,4,5,9,12])
y = np.array([10,8,2,5,7])
plt.plot(x,y, '*:k')
'''
#line
'''
y = np.array([2,6,9,3])
plt.plot(y, linestyle = "dashed")
'''
#labels
'''
x = np.array([10,20,30,40,50,60,70,80,90,100])
y = np.array([1,2,3,4,5,6,7,8,9,10])

font1 = {'family':'sherif','color':'blue','size':'20'} # adding color,size and font family to the title
font2 = {'family':'sherif','color':'red','size':'15'} #adding color,size and font family to the labels

plt.plot(x,y)
plt.title("plot of men aganist their children", fontdict = font1)
plt.xlabel("number of men", fontdict = font2)
plt.ylabel('their children', fontdict = font2)
'''
# bars
'''
x = np.array(['A','B','C','D'])
y = np.array([10,50,84,36])

plt.bar(x,y, color = 'red', width = 0.3)
'''
#histogram
x = np.random.normal(170,10,250)
#print(x) # prints a random array with 250 values concentrated at 170 and a deviation of 10
plt.hist(x)
plt.show()