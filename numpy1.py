import numpy as np

#Create Array
arr1d = np.array([1,2,3,4,5])
arr2d = np.array([[85,90,78], [72,88,95], [91,76,83]])

print(arr2d.shape) #returns no. of rows and columns of array or shape of array
print(arr2d.dtype) #returns type of elements present in array
print(arr2d.ndim) #returns dimension of array

zeros = np.zeros((3,4)) #Creates a zero matrix of given no. of rows and columns
print(zeros)

ones = np.ones((2,5))  #Creates a matrix full of 1's of given no. of rows and columns
print(ones)

rng = np.arange(0,50,5) #Creates an array of elements from the range of 0 to 50 with diffrence of 5
print(rng)

lin = np.linspace(0,1,11) #Creates an array of 11 elements between 0 to 1
print(lin)

random = np.random.randint(40,100,(5,3)) #Creates a matrix of 5x3 of random numbers between range of 40 to 100
print(random)

arr = np.array([10,20,30,40,50])

print(arr * 2) #Multiplies 2 with every element in arr

print(arr + 5) #Adds 5 with every element in arr

print(arr ** 2)# Squares every element in arr

#Statistics operations with NumPy
marks = np.array([[85,90,78], [72,88,95], [91,76,83]])

print(np.mean(marks)) #Overall mean / Average

print(np.mean(marks, axis = 1)) #Mean per row(1)

print(np.mean(marks, axis = 0)) #Mean per column(0)

print(np.mean(marks)) #Maximum number

print(np.std(marks)) #Standard Deviation

arr1 = np.array([55,82,43,91,67,78,35,88])
print(arr1[arr1 > 70]) #Returns those elements who are greater than 70
