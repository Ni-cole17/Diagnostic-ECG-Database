from src.SaveData import SaveData
from src.Infos import Infos

class Signal(Infos):
  def __init__(self,signal_dict,idP,idS,new_patient):
    super().__init__(signal_dict,idP,'Signal_info.csv')
    self.new_patient = new_patient
    self.idS = idS

  def savedados(self):
    self.record_info['idP'] = self.idP
    self.record_info['idS'] = self.idS
    self.record_info['data_path'] = 'Signal/'+str(self.idP)+'_'+str(self.idS)+'.txt'
    k = SaveData(self.record_info,self.csv)
    k.save()
