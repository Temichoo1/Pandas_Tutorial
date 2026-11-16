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
df_1['Phone_Number'] = df_1['Phone_Number'].str.replace(r'[^0-9]', '', regex=True)
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
df_1['Phone_Number'] = df_1['Phone_Number'].str.replace('--','')
print(df_1)

"""5th step: splitting the address"""
#df_1['Address'] = df_1['Address'].str.split(',', n=2, expand=True) #we cant leave it this way as we need to split the address
df_1[['Street_Address', 'State', 'Zip_Code']] = df_1['Address'].str.split(',', n=2, expand=True)
print(df_1[['Street_Address', 'State', 'Zip_Code']])
print(df_1)


"""6th step: Paying Customer & Do_Not_Contact column entries as they are in 'Y' and 'N' format we need to amend it to be formatted properly and alligned accros board"""
df_1['Paying Customer'] = df_1['Paying Customer'].str.replace('Yes', 'Y')
df_1['Paying Customer'] = df_1['Paying Customer'].str.replace('No', 'N')
df_1['Do_Not_Contact'] = df_1['Do_Not_Contact'].str.replace('Yes', 'Y')
df_1['Do_Not_Contact'] = df_1['Do_Not_Contact'].str.replace('No', 'N')
print(df_1)

df_1 = df_1.fillna('')
print(df_1)

"""7th: filter by customers who do not want to be contacted"""

""" 
    We can do it this wasy which is longer

for x in df_1.index:
    if df_1.loc[x, "Do_Not_Contact"] == 'Y':
        df_1.drop(x, inplace=True)
"""
#this is simpler
df_1 = df_1[df_1['Do_Not_Contact'] != 'Y']

print(df_1)
