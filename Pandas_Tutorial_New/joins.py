##MERGE JOIN AND CONCATENATE

"""Focusisng on Merge, Inner, outer, left and right joins"""

import pandas as pd

df_1 = pd.read_csv(r"Data\LOTR.csv")
print(df_1)

df_2 = pd.read_csv(r"Data\LOTR 2.csv")
print(df_2)

                    #####  MERGE  #####
"""Inner JOIN is the default join"""
merged_frame_inner = df_1.merge(df_2, how='inner', on=['FirstName', 'FellowshipID'])
print(merged_frame_inner)

"""Outer JOIN included with a filter to order the dataframe"""
merged_frame_outer = df_1.merge(
    df_2,
    how='outer', 
    on=['FirstName', 'FellowshipID']
).sort_values(by='FellowshipID')

print(merged_frame_outer)


"""LEFT JOIN included with a filter to order the dataframe"""
merged_frame_left = df_1.merge(
    df_2,
    how='left', 
    on=['FirstName', 'FellowshipID']
).sort_values(by='FellowshipID')

print(merged_frame_left)



"""RIGHT JOIN included with a filter to order the dataframe"""
merged_frame_right = df_1.merge(
    df_2,
    how='right', 
    on=['FirstName', 'FellowshipID']
).sort_values(by='FellowshipID')

print(merged_frame_right)

