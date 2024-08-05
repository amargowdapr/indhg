import numpy as np
#Create a vector as a Row
vector_row = np.array([ 1,2,3,4,5,6])
# print vector
print(vector_row)
matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])  
#Create a Matrix 
print(matrix)
#Select 3rd element of Vector
print(vector_row[2])    
#Select 2nd row 2nd column
print(matrix[1,1])              
#Select all elements of a vector
print(vector_row[:])
#Select everything up to and including the 3rd element
print(vector_row[:3])
#Select the everything after the 3rd element
print(vector_row[3:])
#Select the last element
print(vector_row[-1])
#Select the first 2 rows and all the columns of the matrix
