import readgslib

a = readgslib.read('test_data.gslib')

print (a)

# columns names
print (a.cols)

# name of the second column
print (a.cols[1])

# get column data
print (a.col('X'))

# by the column index
print (a.col(0))

# get full matrix data
print (a.matrix())

# set nan
a.set_nan(-99)

# replace all nans
a.replace_nan(0)

# get full matrix data
print (a.matrix())

