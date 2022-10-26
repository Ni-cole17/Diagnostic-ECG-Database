
import os
import csv

class SaveData:
  def __init__(self,some_dict,file_name):
    self.file_name = file_name
    self.some_dict = some_dict
  
  def save_csv(self,dir):
    file_exists = os.path.isfile(dir)
    header = []
    row = []
    with open(dir, 'a') as csv_file:
      writer = csv.writer(csv_file)
      for key, value in self.some_dict.items():
        header.append(key)
        row.append(value) 
      if file_exists == False:
        writer.writerow(header)
      writer.writerow(row)

  def save(self): # Falta adicionar o idPaciente
    dir = self.file_name
    self.save_csv(dir)
