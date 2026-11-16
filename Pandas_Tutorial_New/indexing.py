import pandas as pd 

population_csv_df = pd.read_csv(r"Data\world_population.csv", index_col='Country') #setting the counyry as theindex from thevery beginning

print(population_csv_df)

##resetting the index 
#population_csv_df.set_index('Rank', inplace=True)
#print(population_csv_df)

"""search based on index"""
#population_csv_df = population_csv_df.set_index('Country')
Albania_details = population_csv_df.loc['Albania']
print(Albania_details)
print(population_csv_df.index.name)
population_csv_df.sort_index()