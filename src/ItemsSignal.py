import pandas as pd
import numpy as np

class ItemsSignal:
  def __init__(self,base,idP,idS,signal):
    '''
    this class uses the same parameters as the
    visualization class to extract the components from the ecg register for the pacient selected
    '''
    self.base = base
    self.idP = idP
    self.idS = idS
    self.signal = signal

  def Query_record(self,Data):
     '''
     This method returns the patient's data presents in the database

     INPUT
     Data(DataFrame): DataFrame signal or base
     '''
     return Data[(Data.idP == self.idP) & (Data.idS == self.idS)]

  def take_fs(self):
    '''
    This method returns the fs of the record

    '''
    select = self.Query_record(self.signal)
    fs = int(pd.Series(select.fs).values)
    return fs

  def take_signal(self):
    '''
    This method returns the array of the record
    '''
    select = self.Query_record(self.signal)
    path = str(pd.Series(select.data_path).values[0])
    return np.loadtxt(path)

  def take_time(self):
    '''
    This method return the values of time record
    '''
    fs = self.take_fs()
    sizesig = len(self.take_signal())
    ts = 1 / fs
    t = np.arange(0, sizesig) * ts
    return t
