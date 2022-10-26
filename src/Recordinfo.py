from src.SaveData import SaveData
from src.Infos import Infos

class Recordinfo(Infos):
  def __init__(self, record_info_dict,idP):
    super().__init__(record_info_dict,idP,'Record_info.csv')

  def savedados(self):
    self.record_info['idP'] = self.idP
    k = SaveData(self.record_info,self.csv)
    k.save()