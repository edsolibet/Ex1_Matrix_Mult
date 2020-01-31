import sys

# parse 2x2 matrix as list of string

mat1= sys.argv[1:5]
mat2= sys.argv[5:9]

# convert list of string to list of int
for i in range(len(mat1)):
 mat1[i] = int(mat1[i])
 mat2[i] = int(mat2[i])

# function for matrix multiplication of 2 2x2 matrix
# output: list for 2x2 matrix

def matrix_mult(mat1, mat2):
 a = mat1[0]*mat2[0] + mat1[1]*mat2[2]
 b = mat1[0]*mat2[1] + mat1[1]*mat2[3]
 c = mat1[2]*mat2[0] + mat1[3]*mat2[2]
 d = mat1[2]*mat2[1] + mat1[3]*mat2[3]
 return [[a, b], [c, d]]

# calculate and print output
mat = matrix_mult(mat1, mat2)
print (mat)



