import wfdb

class ReadFile:
  def __init__(self, registro, paciente):
    self.registro = registro
    self.paciente = paciente
  def read(self): 
       signals, fields = wfdb.rdsamp(self.registro, channels=[*range(15)], pn_dir='ptbdb/'+ self.paciente + '/')
       return signals, fields
