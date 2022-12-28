import numpy as np

arr = np.array([a for a in range(11)])

arr[1:9:3] # doesn't work add arr as variable
arr = arr[1:9:3] # start, stop, step
print(f'first array indexed simple start, stop and step {arr}')

'''
Slicing 2D arrays
'''
 #first index row,  second index column,
array2d = np.array([[1,2,3],
           [4,5,6],
           [7,8,9]
           ])

index2d_a = array2d[2,1] # returns the second row and second number #8
print(index2d_a)

employees = np.array([['Jonny', 21, 'Assistant'],
                      ['Susan', 18, 'Intern'],
                      ['James', 27, 'Manager']
])

age_employees = np.int_(employees[:, 1]) # np.int_ converts the string into integers
print(age_employees)
employees_under_25 = employees[1,:]

'''slicing a 3d array'''

array_3d = np.array([[[1,2,3], [4,5,6]],
                      [[7,8,9], [10, 11, 12]],
                      [[13,14,15], [16,17,18]],
                      [[19,20,21], [22,23,24]]
                      ])

# 3 commas for row column and depth?
index3d_a = array_3d[1,1,2]
index3d_b =  array_3d[3, 1, 0]
print(index3d_a)
print(index3d_b)

'''the number of brackets used determines the size of the dimension

using maths to manipulate the array'''

print(array2d + array_3d)
