import readgslib
import numpy as np

### read class #
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

### write class #

b = readgslib.write()

b.set_title('Title test')
v1 = [3,2,4]
v2 = np.array([3,2,4])

b.put_var('Var1', v1)

b.put_var('VAR2', v2)

b.write('test_gslib.dat')

# the file will be (without '#'):
#Title test
#2
#Var1
#VAR2
#3 3
#2 2
#4 4


import pandas as pd
# Example for read a gslib file and transform in a pandas dataframe.
file_pocos = 'example.gslib'
a = readgslib.read(file_pocos)
df = pd.DataFrame(columns=a.cols, data=a.matrix())

# Write a pandas df in gslib format
b = readgslib.write()
b.set_title('Title')

for col in df.columns:
    b.put_var(col, df_pocos_estrat[col])
b.write('data_gslib_from_pandas_df.dat')
