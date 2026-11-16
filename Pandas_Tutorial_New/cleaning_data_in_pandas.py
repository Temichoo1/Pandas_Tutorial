import pandas as pd

"""
    There are issues with phone number formatting, Last Name, First NAme, Address(i will probably be splitting these out)
    and i will be addressing these issues, so the data cab be standardised and ready for ingestion into SQL Tables
    Also reviewing unwanted columns as well and removing duplicates
"""

df_1 = pd.read_excel(r"Data\Customer Call List.xlsx")
#printing the initial dataet to see the issues before cleaning
#introducing the shape will help us see the reduction and removal of any duplicated rows
print(df_1)
print(df_1.shape)

"""1st step: drop duplicates"""
#CONFIRM DUPLICATES
df_1_duplicates = df_1.duplicated()
print(df_1_duplicates)

#REMOVE DUPLICATES
df_1 = df_1.drop_duplicates()
print(df_1)
print(df_1.shape)

"""2nd step: remove unused columns"""
df_1 = df_1.drop(columns='Not_Useful_Column')
print(df_1)
print(df_1.shape)

"""3rd step: remove unwanted spaces especially in the first names section and will do the same for LAst name as well to be on the safe side, line 16"""
df_1['First_Name'] = df_1['First_Name'].str.strip()
print(df_1)
#to be on the safe side ill do the same for Last NAme

""" we can remove the data line by line
        df_1['Last_Name'] = df_1['Last_Name'].str.strip()
        df_1['Last_Name'] = df_1['Last_Name'].str.lstrip("...")
        df_1['Last_Name'] = df_1['Last_Name'].str.lstrip("/")
        df_1['Last_Name'] = df_1['Last_Name'].str.rstrip("_")
"""

df_1['Last_Name'] = df_1['Last_Name'].str.strip("123._/") #PUTTING AL THEVALUES TO BE REMOVED INTO ONE STRING
print(df_1)

"""4th step: formatting the phone numbers: This can be tricky because there are many types and we need it to align in the correct format"""
#replace any invalid characters with nothing
df_1['Phone_Number'] = df_1['Phone_Number'].str.replace('[^a-zA-Z0-9]','')
print(df_1)
#change the format to string
df_1['Phone_Number'] = df_1['Phone_Number'].apply(lambda x: str(x))
print(df_1)

#standardising the format
df_1['Phone_Number'] = df_1['Phone_Number'].apply(lambda x: x[0:3] + '-' + x[3:6] + '-' + x[6:10])
print(df_1)

#replacing nan-- and  N/a-- 
df_1['Phone_Number'] = df_1['Phone_Number'].str.replace('nan--','')
print(df_1)
df_1['Phone_Number'] = df_1['Phone_Number'].str.replace('N/a--','')
print(df_1)
