import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import random
from src.ItemsSignal import ItemsSignal
from src.Json import Json

class Visualization:
  def __init__(self,csv,signal,idP,idS):
    '''
    This class recive two files.csv directory, and two strings

      INPUT
        *csv (directory string): directory of file.csv about the pacient
        *signal (directory string): directory of file.csv about the ecg record features
        *idP (string): String Id pacient
        *idS (string): String Id signal 

    '''
    self.base = pd.read_csv(csv)
    self.idP = idP
    self.idS = idS
    self.signal = pd.read_csv(signal)
    self.Items = ItemsSignal(self.base,self.idP,self.idS,self.signal) 
      
  def Plot_Bar(self,column):
    '''
    This method returns a plot bar of a column from dataframe

     INPUT
        * name of column (string) 
    '''
    count = self.base[column].value_counts()
    fig = px.bar(self.base,x = count.index,y = count.values,labels={
                     "x": column,
                     "y": "count"},title = 'distribution '+ column)

    
    return fig
  
  def table_Distribution(self,column):
    '''
    This method returns a table of a column from dataframe

     INPUT
        * name of column (string) 
    '''
    return pd.DataFrame(self.base[column].value_counts())
  
  def table_pacient_data(self,issue,parameter = None,data= None):
    '''
    This method returns a Dataframe pacients with different issues

     INPUT
        *issue(string): The issue in column Reason for admission
    '''
    if data is None:
      return self.base[self.base['Reason for admission'] == issue]
    else:
      return self.base[(self.base['Reason for admission'] == issue) & (self.base[data] == parameter)]

  def plot_signal(self,Type):
      '''
      This method returns a Record ECG plotting 

      INPUT
          * Type plotting (string):
            Type ('all') : Plotting one graph with all channels in the record
          Type ('channels'): Plotting one graph with separate channels in the record
      '''
      t = self.Items.take_time()
      sig = self.Items.take_signal()

      if Type ==  'all':
        figure, ax1 = plt.subplots(1, 1,figsize=(15,7))
        ax1.plot(t, sig, linewidth=2)
        ax1.set_title("Record " + str(self.idS) + ' Pacient ' + str(self.idP))
        ax1.set_xlabel("Time(s)")
        ax1.set_ylabel("Amplitude")
        ax1.grid()
        plt.figure (figsize=(18,9))

      elif Type == 'channels':
        num_of_channels = sig.shape[1]
        cs = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
              for i in range(num_of_channels)]
        plt.figure (figsize=(30,15))
        count = 0
        for i in range(num_of_channels):
          current_color=cs[count]
          plt.plot(t,sig[::,i]+(num_of_channels-count)*1,color=current_color,linewidth=1,label = 'channel'+ str(i))
          plt.legend(labelspacing = 3)
          count = count + 1
        plt.title("Record " + str(self.idS) +  ' Pacient ' + str(self.idP))
        plt.xlabel("Time(s)")
        plt.ylabel("Amplitude")
        plt.tight_layout()

  def up_plot(self):
      '''
      This method returns a bidimensional plotting from ECG record 
      '''
      signal = self.Items.take_signal()
      plt.figure(figsize=(18,9))
      plt.imshow(signal.transpose(),aspect = 'auto',cmap= 'jet_r',origin = 'upper',resample= True)
      plt.title("Record " + str(self.idS) + ' Pacient ' + str(self.idP))
      plt.colorbar()

  def Vetocardiogram(self):
      '''
      This method returns a vectorcardiogram tridimensional plotting 
      '''
      signal = self.Items.take_signal()
      vx = signal[:,12]
      vy = signal[:,13]
      vz = signal[:,14]
      df = pd.DataFrame({"x": vx, "y":vy, "z":vz})
      fig = px.line_3d(df,x ='x',y = 'y',z = 'z',title = "Record vectorcardiogram " + str(self.idS) + ' Pacient ' + str(self.idP))
      return fig

  def plot_hist(self,classes):
    '''
      This method returns the time record distribution for all pacients issues in a histogram plot
    '''
    dictionary = Json("classes_times.json").load_json()
    X = dictionary[classes]
    plt.hist(X)
    plt.title(f'Time record distribution for the issue {classes}')
    plt.xlabel('Time (s)')
    plt.tight_layout()
    plt.show()

