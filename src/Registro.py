from src.Signal import Signal
from src.Recordinfo import Recordinfo
import numpy as np

class Registro:
  def __init__(self,fields,signal_fields,signal,new_patient,idP,idS):
    self.record_info = fields
    self.signal_fields = signal_fields
    self.new_patient = new_patient
    self.idP = idP
    self.idS = idS
    self.signal = signal

  def save_data(self):
    if self.new_patient == True:
      patient = Recordinfo(self.record_info,self.idP)
      patient.savedados()
      self.save_signal()
    else:
      self.save_signal()

  def save_signal(self):
    signal = Signal(self.signal_fields,self.idP,self.idS,self.new_patient)
    np.savetxt(f'Signals/{self.idP}_{self.idS}.txt', self.signal, fmt='%f')
    signal.savedados()