#25341a05l1 vinay
# Program to create a 3x3 matrix using nested list comprehension

matrix = [[i + j * 3 for i in range(1, 4)] for j in range(3)]

print("3x3 Matrix:")
for row in matrix:
    print(row)

''' output
3x3 Matrix:
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
'''