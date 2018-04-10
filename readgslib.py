import numpy as np

class read:
  def __init__(self, filename):
    print ('Opening file '+filename+' ...')
    self.filename = filename
    
    try:
      file = open(filename)
      print ('OK.')
    except:
      print ('ERROR opening file '+filename+'.')

    self.initread()
    
  def initread(self):
    file = open(self.filename)
    self.title = file.readline()
    print ('Title: '+self.title)
    try:
      self.ncols = int(file.readline().split()[0])
      print ('Number of columns: '+str(self.ncols))
    except:
      print ('Error when processing 2nd line.')
      
    self.cols = list()
    for i in range(self.ncols):
      self.cols.append(file.readline().split()[0])
      
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
    
  def col_data(self, col_item):
    if type(col_item) == type('a'):
      return self.dict_data[col_item]
    elif type(col_item) == type(1):
      return self.m[:,col_item]
    
  def matrix(self):
    return self.m
    
  def __str__(self):
    return '<Obj. from Gslib data, cols: '+', '.join(self.cols)+'>'
    
#  def __repr__(self):
#    return __str__()
