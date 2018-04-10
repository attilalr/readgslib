import numpy as np

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
    for i, col in enumerate(self.cols):
      self.dict_data[col] = self.m[:,i]    
  
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
    
  def replace_nan(x, col=None):
    if col == None:
      self.m[self.m == self.nan] = x
    elif:
      b = self.m[:, col]
      b[b==self.nan] = x
    
  def __str__(self):
    return '<Obj. from Gslib data, cols: '+', '.join(self.cols)+', data matrix shape: '+str((self.m).shape)+'>'
    
#  def __repr__(self):
#    return __str__()
