import re

class OrganizeFields:
  def __init__(self, fields_dict):
    self.fields_dict = fields_dict

  #Função que converte a formata a lista "comment para poder passar ela para dicionário
  def comments_to_list(self):
    comments = self.fields_dict['comments']
    commentslist = []
    for i in range(len(comments)):
     commentslist.append(re.sub(r': +',"//",comments[i].strip()).split("//"))
    commentslist.remove(['Diagnose:'])
    commentslist.remove(['Hemodynamics:'])
    commentslist.remove(['Therapy:'])
    return commentslist

  #Função que converte lista para dicionário
  def list_to_dict(self):
    comments_list = self.comments_to_list()
    result_dct = {}
    for lst in comments_list:
      if len(lst) == 2:
        result_dct[lst[0]] = lst[1] 
      else:
        result_dct[lst[0].replace(':','')] = 'n/a' 
    return result_dct

  #Função que mescla dicionário "comments" com os outros dicionários e forma um dicionário com tudo
  def merge_dict(self,comments_dict):
    self.fields_dict.pop('comments', None)
    for k,v in comments_dict.items():
      self.fields_dict[k] = v
    return self.fields_dict

  def split_fields(self,dictionary):
    keys = list(dictionary.keys())
    record_infos_keys = keys[7:]
    signal_infos_keys = keys[:7]
    return record_infos_keys,signal_infos_keys

  def get_dicts(self):
    dict_signal = {}
    dict_record_info = {}
    comments_dict = self.list_to_dict()
    final_dict = self.merge_dict(comments_dict)
    record_infos_keys,signal_infos_keys = self.split_fields(final_dict)
    for k,v in final_dict.items():
      if k in record_infos_keys:
        dict_record_info[k] = v
      else:
        dict_signal[k] = v
    return dict_record_info, dict_signal
