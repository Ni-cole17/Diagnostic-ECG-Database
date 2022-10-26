import pandas as pd
import tqdm
from src.ItemsSignal import ItemsSignal


class RecordsTime:
  def __init__(self,base,signal):
    self.base = pd.read_csv(base)
    self.signal = pd.read_csv(signal)
    self.records_name = self.get_records_name()

  def ids_to_list(self):
    patients = list(self.signal.idP)
    records = list(self.signal.idS)
    return patients,records

  def get_records_name(self):
    patients ,records = self.ids_to_list()
    records_name = [patient + '-' + record for patient, record in zip(patients, records)]
    return records_name

  def saveTimes(self):
    Class_time = {}
    pacient,record = self.ids_to_list()
    id = 0
    for values in tqdm.tqdm(range(len(pacient))):
      call = ItemsSignal(self.base,pacient[values],record[values],self.signal)
      if pacient[values] != id:
        key = list(self.base.query(f'idP == "{pacient[values]}"')['Reason for admission'])[0]
        if key not in Class_time.keys():
          Class_time[key] = []
        Class_time[key] += [len(call.take_time())/call.take_fs()]
      id = pacient[values]
    return Class_time