import numpy as np

def calculate(list):
  a = np.array(list)
  try:
    b = np.reshape(a, (3,3))
  
    value1 = np.mean(b, axis=0).tolist()
    value2 = np.mean(b, axis=1).tolist()
    value3 = np.mean(a, axis=0).tolist()
  
    calculations = {}
  
    calculations.update({'mean': [value1,value2,value3]})
  
    value1 = np.var(b, axis=0).tolist()
    value2 = np.var(b, axis=1).tolist()
    value3 = np.var(a, axis=0).tolist()
  
    calculations.update({'variance': [value1,value2,value3]})
  
    value1 = np.std(b, axis=0).tolist()
    value2 = np.std(b, axis=1).tolist()
    value3 = np.std(a, axis=0).tolist()
  
    calculations.update({'standard deviation': [value1,value2,value3]})
  
    value1 = np.amax(b, axis=0).tolist()
    value2 = np.amax(b, axis=1).tolist()
    value3 = np.amax(a, axis=0).tolist()
  
    calculations.update({'max': [value1,value2,value3]})
  
    value1 = np.amin(b, axis=0).tolist()
    value2 = np.amin(b, axis=1).tolist()
    value3 = np.amin(a, axis=0).tolist()
  
    calculations.update({'min': [value1,value2,value3]})
  
    value1 = np.sum(b, axis=0).tolist()
    value2 = np.sum(b, axis=1).tolist()
    value3 = np.sum(a, axis=0).tolist()
  
    calculations.update({'sum': [value1,value2,value3]})
  
    return calculations
  except ValueError:
    raise ValueError("List must contain nine numbers.")