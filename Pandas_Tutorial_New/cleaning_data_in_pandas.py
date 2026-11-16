import pandas as pd

"""
    There are issues with phone number formatting, Last Name, First NAme, Address(i will probably be splitting these out)
    and i will be addressing these issues, so the data cab be standardised and ready for ingestion into SQL Tables
    Also reviewing unwanted columns as well and removing duplicates
"""

df_1 = pd.read_excel(r"Data\Customer Call List.xlsx")
#printing the initial dataet to see the issues before cleaning
#introducing the shape will help us see the reductii=on and removal of any duplivcated rows
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