
import math
class complexno:
  '''complex no class '''
  def __init__(self,real=0,imagenary=0):
    '''constructor. Needs real and imagenary values is input parameter. By Default is initialised to 0,0'''
    self.real=real
    self.imagenary=imagenary
  
  def __repr__(self):
    
    return '{}+{}j'.format(self.real,self.imagenary)
  
  def add(self,no2):
    '''returns sum of two complex numbers'''
    real=self.real+no2.real
    imagenary=self.imagenary+no2.imagenary
    return complexno(real,imagenary)
  
  def sub(self,no):
    '''returns '''
    real=self.real-no.real
    imagenary=self.imagenary-no.imagenary
    return complexno(real,imagenary)

  def multiply(self,no):
    real=self.real*no.real-self.imagenary*no.imagenary
    imagenary=self.real*no.imagenary+self.imagenary*no.real
    return complexno(real,imagenary)
  
  def conj(self):
    return complexno(self.real,-self.imagenary)

  def magnitude(self):
    return math.sqrt(self.real**2+self.imagenary**2)

  def div(self,no):
    product=self.multiply(no.conj())
    real=product.real/(no.magnitude()**2)
    im=product.imagenary/(no.magnitude()**2)
    return complexno(real,im)

  

no1=complexno(1,2)
no2=complexno(0,1)
no3=no1.add(no2)
print(no3)
print(no3.magnitude())
no4=no1.div(no2)
print(no4)