# Diagnostic-ECG-Database

  Esse repositório faz parte do projeto da disciplina de Técnicas Computacionais e tem como objetivo facilitar a visualização da base de dados explorada. Para isso a base passou pela etapa de ETL (Extraction, Transform e Load) seguido de uma etapa de visualização dos dados. 
  Todos os processos realizados nesse trabalho podem ser testados com o jupyter notebook Prepare_and_Visualize_Data.ipynb.

### Base de dados
  A base de dados utilizada nesse projeto está no seguinte link https://www.physionet.org/content/ptbdb/1.0.0/.
  
  ![ptb](https://user-images.githubusercontent.com/65842535/198130224-df2e3779-4ce5-4749-b153-c3203248aab4.png)

  Ela representa uma base de dados de sinais de ECG com um total de 549 registros de 290 pacientes, sendo cada registro feito com 16 canais (14 de ECGs, 1 de respiração e 1 de line voltage).
  
  Cada registro de ECG tem uma classe de diagnóstico. As classes encontradas na base de dados estão listadas abaixo
    - Myocardial infarction 
    - Cardiomyopathy/Heart failure
    - Bundle branch block
    - Dysrhythmia
    - Myocardial hypertrophy
    - Valvular heart disease
    - Myocarditis
    - Miscellaneous
    - Healthy controls
   
 ### Extração e Organização dos dados
   
 #### Geração do json com heas
   A primeira etapa de extração dos dados foi a geração de um json (patient_heas.json) para organizar os arquivos .hea de cada paciente da base dados, isso porque um paciente pode ter um ou mais arquivos .hea. Assim, esse json foi bastante útil para extrair e salvar os dados de cada registro mais rapidamente.
   
 #### Geração do Record_info.csv e Signal_info.csv
   Para realização dessa etapa foram criadas 7 classes para melhor organizar o carregamento dos dados. O diagrama de classes assim como a explicação de cada classe está especificada abaixo.
   
   ![image](https://user-images.githubusercontent.com/65842535/198134205-efea0e94-4d71-4dbc-976a-cab5a4f79174.png)
   
   #### Classe ReadFile
   
   ![image](https://user-images.githubusercontent.com/65842535/198134410-d3284fcb-096e-4695-8310-a8d26d369983.png)

   A classe ReadFile recebe um registro (arquivo .hea) e o paciente.
   Possui o método read() que irá ler o arquivo do paciente e irá retornar o sinal e um dicionário com informações sobre o registro (signals e fields)
   
   #### Classe OrganizeFiles
   
   ![image](https://user-images.githubusercontent.com/65842535/198136057-48aa9589-6700-42cb-876d-efae34f4ac6a.png)
   ![image](https://user-images.githubusercontent.com/65842535/198136195-c3bfefa4-d770-4d8c-a43d-2e27212f49eb.png)
   
   O objetivo dessa classe é organizar o dicionário fields retornado pela Classe ReadFile, separando em informações do registro e informações do sinal que posteriormente vão ser salvas nos arquivos csvs. Um dos problemas do dicionário fields é que existe uma key chamada comments que é um dicionário em forma de lista, 


   
   

 
