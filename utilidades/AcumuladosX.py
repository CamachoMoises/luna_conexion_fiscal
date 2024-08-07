from Util import Util

class AcumuladosX(object):
  #Global variables
  _freeTax = 0L
  _generalRate1 = 0L
  _generalRate1Tax = 0L
  _reducedRate2 = 0L
  _reducedRate2Tax = 0L
  _additionalRate3 = 0L
  _additionalRate3Tax = 0L

  def __init__(self, trama):
    if (trama != None):
      if (len(trama) > 0):
        try:
          _arrayParameter = trama.split(chr(0X0A)) 
          print(_arrayParameter)
          _arraySubParameter= _arrayParameter[0].split(' ')
          if (len(_arrayParameter) >= 7):
            self._freeTax = Util().DoValueDouble(_arraySubParameter[1])
            self._generalRate1 = Util().DoValueDouble(_arrayParameter[1])
            self._reducedRate2 = Util().DoValueDouble(_arrayParameter[2])
            self._additionalRate3 = Util().DoValueDouble(_arrayParameter[3])
            self._generalRate1Tax = Util().DoValueDouble(_arrayParameter[4])
            self._reducedRate2Tax = Util().DoValueDouble(_arrayParameter[5])
            self._additionalRate3Tax = Util().DoValueDouble(_arrayParameter[6])
        except():
            return
  
  def FreeTax(self):
    return self._freeTax
  
  def GeneralRate1(self):
    return self._generalRate1
  
  def GeneralRate1Tax(self):
    return self._generalRate1Tax
  
  def ReducedRate2(self):
    return self._reducedRate2

  def ReducedRate2Tax(self):
    return self._reducedRate2Tax
  
  def AdditionalRate3(self):
    return self._additionalRate3
    
  def AdditionalRate3Tax(self):
    return self._additionalRate3Tax


