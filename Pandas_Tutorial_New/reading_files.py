import pandas as pd

"""  READING FILES """

#The use of header = none, removes the headers, and the name  enables us add new header names to the dataframe

###Countries_df = pd.read_csv(r"Data\countries of the world.csv", header = None, names=['country', 'region'])

        ###  READING CSVS
Countries_csv_df = pd.read_csv(r"Data\countries of the world.csv") #adding , header = None, names=['country', 'region'] will remove the headers, then add new headers
#print(Countries_csv_df)
#
#        ### READING TXT files
#Countries_txt_df = pd.read_table(r"Data\countries of the world.txt")
#print(Countries_txt_df)


        ### READING JSON files
#Countries_json_df = pd.read_json(r"Data\json_sample.json")
#print(Countries_json_df)

        ### READING EXCEL files
Countries_excel_df = pd.read_excel(r"Data\world_population_excel_workbook.xlsx")
#print(Countries_excel_df)

""" Sometimes when reading the files, its important to be able to visualise all the data, so invcreasing the display of the max rows and max columns is advisable """
""" using the command below helps in that aspect """
#pd.set_option('display.max_rows', 50)
#pd.set_option('display.max_columns', 50)
  

""" GETTING THE INFORMATION ABOUT DATAFRAMES:  """

Countries_csv_df.info()  #tells you all the datatypes and the memore being used
Countries_excel_df.info() #tells you all the datatypes and the memore being used

Countries_csv_df.shape
Countries_excel_df.shape
