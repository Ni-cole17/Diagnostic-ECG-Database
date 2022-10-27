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
   A primeira etapa de extração dos dados foi a geração de um json (patient_heas.json) para organizar os arquivos .hea de cada paciente da base dados, isso porque um paciente pode ter um ou mais arquivos .hea. Assim, esse json foi bastante útil para extrair e salvar os dados de cada registro mais rapidamente. Para ele foi utilizado a classe Json, tanto para salvar, quanto para carregar.
   
 #### Geração do Record_info.csv e Signal_info.csv
   Para realização dessa etapa foram criadas 7 classes para melhor organizar o carregamento dos dados. O diagrama de classes assim como a explicação de cada classe está especificada abaixo.
   
   ![image](https://user-images.githubusercontent.com/65842535/198134205-efea0e94-4d71-4dbc-976a-cab5a4f79174.png)
   
   #### Classe ReadFile
   
   A classe ReadFile recebe um registro (arquivo .hea) e o paciente.
   Possui o método read() que irá ler o arquivo do paciente e irá retornar o sinal e um dicionário com informações sobre o registro (signals e fields)
   
   #### Classe OrganizeFiles
   
   O objetivo dessa classe é organizar o dicionário fields retornado pela Classe ReadFile, separando em informações do registro e informações do sinal que posteriormente vão ser salvas nos arquivos csvs. Um dos problemas do dicionário fields é que existe uma key chamada comments que é um dicionário em forma de lista. Logo os métodos dessa classe irão fazer a conversão dessa lista em dicionário e posteriormente juntar esse dicionário resultante com o fields. Ao final, as informações do dicionário, agora completo, irá ser separado em um dicionário com as infos do sinal e as infos do registro.
   
   #### Classe Registro
  
   Essa Classe é responsável por salvar os dados dos registros em seus respectivos diretórios. Ela recebe as informações do sinal, do registro, o array do sinal, o id do paciente, id do registro e uma flag para indicar se aquele paciente já foi ou não registrado na base anteriormente.
   
   #### Classe Infos, Signal e RecordInfo
   
   A classe Infos é a classe mãe de Signal e RecordInfo, ela é responsável por receber os dados e instanciar a classe SaveData para salvar cada objeto em seu respectivo caminho. A classe Signal e RecordInfo, são classes filhas da Classe info, visto que ambas implementam os mesmos métodos e recebem atributos semelhantes.
   
   #### Classe SaveData
   
   Essa Classe recebe um dicionário e um csv, a responsabilidade dela é salvar o dicionário no csv. Ela tem dois métodos, o save e o save_csv, foi feito assim pois se caso quiser adicionar um outro método para salvar um outro tipo de arquivo, ficaria mais fácil.
   
   ### Visualização dos sinais
   
   #### Classe ItemsSignal
  
   O objetivo dessa classe é a partir dos dados extraídos e organizados nas classes anteriores, extrair as características do registro de ecg do paciente, desde o número de amostras (take_fs) até o tempo de duração do registro (take_time). A classe ItemsSignal está conectada a classe Visualization, que será responsável por pegar essas informações extraídas pela ItemsSignals e realizar a visualização do registro.
   
   #### Classe Visualization 
    
   Essa classe tem como objetivo extrair todas as informações possíveis dos dados que foram organizados, desde plots de distribuição(Plot_Bar,table_Distribution), histograma do tempo de registro para diferentes problemas de saúde(plot_hist), tabelas de informações dos pacientes(table_pacient_data) até gráficos dos registros de ECG dos pacientes(plot_signal,up_plot,Vetocardiogram).
   
   #### Classe RecordTime
   
   Essa classe foi feita também como um pré-processamento dos dados, visto que demoraria muito tempo (cerca de 10 minutos) para plotar um gráfico de distribuição de duração dos registros. Logo, o objetivo dessa classe é gerar um dicionário (classes_times.json), no qual as keys são os nomes das classes e os values são arrays com o tempo de duração dos registros que pertencem àquela classe. Isso vai facilitar a observação desse tipo de dado.
   
   
   
   
   

 
