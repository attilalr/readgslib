import numpy as np
import os.path

class read:
  def __init__(self, filename, verbose=0, nan=None):
    if verbose:
      print ('Opening file '+filename+' ...')
    self.filename = filename

    self.verbose = verbose
    self.set_nan(nan)
    
    try:
      file = open(filename)
      if verbose:
        print ('OK.')
    except:
      print ('ERROR opening file '+filename+'.')

    self.initread()
    
  def initread(self):
    file = open(self.filename)
    self.title = file.readline()
    if self.verbose:
      print ('Title: '+self.title)
    try:
      self.ncols = int(file.readline().split()[0])
      if self.verbose:
        print ('Number of columns: '+str(self.ncols))
    except:
      print ('Error when processing 2nd line.')
      
    self.cols = list()
    for i in range(self.ncols):
      self.cols.append(file.readline().split()[0])
      
    if self.verbose:
      print ('Trying to extract '+str(self.ncols)+' cols: '+', '.join(self.cols))
      
    file.close()
      
    self.m = np.loadtxt(self.filename, skiprows=self.ncols+2, delimiter=None)
    
    self.dict_data = {}
    if len(self.cols) > 1:
      for i, col in enumerate(self.cols):
        self.dict_data[col] = self.m[:,i]    
    else:
      self.dict_data[self.cols[0]] = self.m[:]
  
  def set_nan(self, nan):
    self.nan = nan
    
  def cols(self):
    return self.cols
    
  def col(self, col_item):
    if type(col_item) == type('a'):
      return self.dict_data[col_item]
    elif type(col_item) == type(1):
      return self.m[:,col_item]
    
  def matrix(self):
    return self.m
    
  def replace_nan(self, x, col=None):
    if col == None:
      self.m[self.m == self.nan] = x
    else:
      b = self.m[:, col]
      b[b==self.nan] = x
    
  def __str__(self):
    return '<Obj. from Gslib data, cols: '+', '.join(self.cols)+', data matrix shape: '+str((self.m).shape)+'>'


### write class

class write:
  def __init__(self, verbose=0, nan=None):
    self.clear()
    self.set_nan(nan)
    
  def clear(self):
    self.filename = None
    self.ncols = None
    self.cols = list()
    self.title = None
    self.rows = None
    self.m = None
    self.dict_data = dict()
    
  def set_nan(self, nan):
    self.nan = nan

  def set_title(self, title):
    self.title = title
    
  def put_var(self, name, vec):
    # check if there is data already in the matrix
    if type(self.m) == type(None):
      vec = np.squeeze(np.array(vec))
      if len(vec.shape) > 1:
        # error, input vector with dim > 1
        pass
      else:
        nrows = vec.size
        self.rows = nrows
        self.cols.append(name)
        self.m = vec.reshape((vec.size, 1))
        self.ncols = 1
        self.dict_data[name] = self.m[:, -1]
    else:
      # if theres is data already we must to check the row number
      vec = np.squeeze(np.array(vec))
      if len(vec.shape) > 1:
        # error, input vector with dim > 1
        pass
      else:
        nrows = vec.size
        if nrows != self.rows:
          print ('Wrong number of rows for variable '+str(name))
          # exit
        else:         
          self.cols.append(name)
          self.m = np.hstack((self.m, vec.reshape(vec.size, 1)))
          self.dict_data[name] = self.m[:, -1]
          self.ncols = self.ncols + 1
  
  def write(self, filename, overwrite=False):
    self.filename = filename
  
    if os.path.isfile(self.filename) and overwrite == False:
      # dont write
      print ('File exist. Use parameter overwrite=True to overwrite file.')
    else:
      # write file
      if self.title == None:
        self.title = 'Dummy Title'
      string = self.title+'\n'+str(self.ncols)+'\n'
      for i, col in enumerate(self.cols):
        string = string + col
        if i != len(self.cols)-1:
          string = string + '\n'
      np.savetxt(self.filename, self.m, header=string, delimiter=' ', fmt='%s', comments='')

  def cols(self):
    return self.cols
    
  def col(self, col_item):
    if type(col_item) == type('a'):
      return self.dict_data[col_item]
    elif type(col_item) == type(1):
      return self.m[:,col_item]
    
  def matrix(self):
    return self.m
    
  def replace_nan(self, x, col=None):
    if col == None:
      self.m[self.m == self.nan] = x
    else:
      b = self.m[:, col]
      b[b==self.nan] = x
    
  def __str__(self):
    return '<Obj. to writ Gslib data, cols: '+', '.join(self.cols)+', data matrix shape: '+str((self.m).shape)+'>'

