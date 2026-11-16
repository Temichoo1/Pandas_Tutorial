import pandas as pd

Flavours_excel_df = pd.read_csv(r"Data\Flavors.csv")
print(Flavours_excel_df)

#Grouping by base flavour
group_by_frame = Flavours_excel_df.groupby('Base Flavor').mean(numeric_only=True)
print(group_by_frame)

#Grouping by count
group_by_count = Flavours_excel_df.groupby('Base Flavor').count()
print(group_by_count)

#Grouping by min
group_by_min = Flavours_excel_df.groupby('Base Flavor').min()
print(group_by_min)

#Grouping by min
group_by_max = Flavours_excel_df.groupby('Base Flavor').max()
print(group_by_max)

#Aggregations by min
group_by_agg = Flavours_excel_df.groupby('Base Flavor').agg({'Flavor Rating': ['mean', 'max', 'count', 'sum'], 'Texture Rating': ['mean', 'max', 'count', 'sum'] })
print(group_by_agg)