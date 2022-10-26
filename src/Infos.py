from src.SaveData import SaveData

class Infos:
  def __init__(self, record_info_dict,idP,csv):
    self.record_info = record_info_dict
    self.csv = csv
    self.idP = idP


  def savedados(self):
    k = SaveData(self.record_info,self.csv)
    k.save()