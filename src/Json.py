import json
import pandas as pd

class Json:
  def __init__ (self,path_json):
    self.path_json = path_json

  def save_json(self,dictionary):
    with open(self.path_json, "w") as outfile:
      json.dump(dictionary, outfile,indent = 4)
  
  def load_json(self):
    dict_json = dict(pd.read_json(self.path_json,typ='series'))
    return dict_json
