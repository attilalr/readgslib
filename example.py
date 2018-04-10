import readgslib

a = readgslib.read('test_data.gslib')

print (a)

# columns names
print (a.cols)

# get column data
print (a.col('X'))

# by the column index
print (a.col(0))

# get full matrix data
print (a.matrix())


