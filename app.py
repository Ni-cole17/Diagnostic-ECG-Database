import streamlit as st
import tempfile
import numpy as np
#from tensorflow.keras.preprocessing import image as keras_image
#from tensorflow.keras.models import load_model
from skimage.transform import resize
from skimage.io import imread
from PIL import Image
import pandas as pd
import scipy.stats
from scipy.stats import norm
import altair as alt
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import wfdb
import os
import random
import plotly.express as px
import visu1
import plotly.figure_factory as ff
import re
import json



# configurações da página (o nome que aparece la em cima nas guias do chrome)
icon = Image.open('Brasão_da_UFPE.png') #"💉"
st.set_page_config(page_title="TC 2022.2", layout="wide", page_icon=icon) # layout centered or wide; page icon pode ser qualquer emoji

st.title("📊 Projeto Final - Técnicas Computacionais")
# outras configurações da página 
#choice = st.sidebar.selectbox("Menu", ["Load Images","Show Images Samples","Model and Results"])

image = Image.open('Brasão_da_UFPE_Branca.png')
st.sidebar.image(image, width=250)
st.subheader("Index")
#options = st.sidebar.selectbox('Select an option:',('Show Images', 'Selected Images', 'Model and Results', 'Keep things'))
t1, t2 = st.tabs(['Visualização', 'Outros'])
st.sidebar.title("Integrantes:")
st.sidebar.info(
    """
  Nathália Giovanna (9º período);
  Nicole Charron (7º período);
  Pedro Gurgel (7º período).
    """
)

st.sidebar.title("Professor:")
st.sidebar.info(
    """
  Fernando José Ribeiro Sales.
  Graduado em Engenharia Eletrônica pelo ITA e Doutor em Cardiologia pela USP (2009).

    """
)

st.sidebar.title("Agradecimentos")
st.sidebar.info(
    """
   Gostaríamos de agradecer ao professor Fernando Sales, pela oportunidade de cursar esta disciplina, na qual nos submetemos a desafios constantes que nos engrandeceram profissionalmente.
    """
)



sig = "/content/Signal_info.csv"
base = "/content/Record_info.csv"

a = visu1.distr(base,sig)
pac, rec, pac_rec = a.get_records_name()
csv = pd.read_csv(base)

st.set_option('deprecation.showPyplotGlobalUse', False)


with t1:
  st.subheader("All images in the selected folder:")


  option1 = st.selectbox(
   'Escolha o paciente e o registro:',
     np.array(pac_rec)
   )
  x = (option1.split('-'))
  Call_Class = visu1.Visualization(base,sig,x[0],x[1])
  
  option0 = st.selectbox(
    'Escolha o tipo de visualização:',
    ('Distribuição de registros por classe diagnóstica',
    'Distribuição da duração dos registros por classe',
    'Lista dos pacientes e registro por classe e por dados clínicos',
    'Visualização de um trecho do sinal e vetocardiograma',
    'Registro como imagem',
    'Nenhum'
  ))
  if option0 == 'Nenhum':
    st.write("Nada para viasualizar")

  elif option0 == 'Distribuição de registros por classe diagnóstica':
    st.table(Call_Class.table_Distribution('Reason for admission'))
    st.plotly_chart(Call_Class.Plot_Bar('Reason for admission'), use_container_width=True)
  
  elif option0 == 'Distribuição da duração dos registros por classe':
    option001 = st.selectbox(
    'Escolha a classe:',
     ('Myocardial infarction', 'Healthy control', 'Cardiomyopathy', 'Bundle branch block', 'Dysrhythmia', 'Hypertrophy', 'Valvular heart disease', 'Myocarditis', 'Stable angina', 'Palpitation', 'Heart failure (NYHA 4)', 'Unstable angina', 'Heart failure (NYHA 2)', 'Heart failure (NYHA 3)'))
   
    st.pyplot(Call_Class.plot_hist(option001))


  elif option0 == 'Lista dos pacientes e registro por classe e por dados clínicos':
    option01 = st.selectbox(
    'Escolha a classe:',
     ('Myocardial infarction', 'Healthy control', 'Cardiomyopathy', 'Bundle branch block', 'Dysrhythmia', 'Hypertrophy', 'Valvular heart disease', 'Myocarditis', 'Stable angina', 'Palpitation', 'Heart failure (NYHA 4)', 'Unstable angina', 'Heart failure (NYHA 2)', 'Heart failure (NYHA 3)'))
   
    option02 = st.selectbox(
    'Escolha a classe:',
     np.array(list(csv.columns)))

    option03 = st.selectbox(
    'Escolha a classe:',
     np.array(list(csv[option02])))

    if option02 == 'todos':
      st.table(Call_Class.table_pacient_data(option01))
    else:
      st.table(Call_Class.table_pacient_data(option01,data = option02,parameter = option03))



  elif option0 == 'Visualização de um trecho do sinal e vetocardiograma':
     st.plotly_chart(Call_Class.Vetocardiogram(), use_container_width=True)

  elif option0 == 'Registro como imagem':
     st.pyplot(Call_Class.plot_signal(Type = 'channels'))
     st.pyplot(Call_Class.up_plot())

     
    
  #else:
  #  option1 = st.selectbox(
  #    'Escolha o paciente:',
  #    np.array(rec)
  #  )


#with t2:

 # st.plotly_chart(b, use_container_width=True)



#with t3:
 # st.subheader("Images selected by the algorithm:")

