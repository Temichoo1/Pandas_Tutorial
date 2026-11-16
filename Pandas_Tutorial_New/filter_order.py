import pandas as pd

population_csv_df = pd.read_csv(r"Data\world_population.csv") #adding , header = None, names=['country', 'region'] will remove the headers, then add new headers

#print(population_csv_df)

""" Filtering by columns """

rank_10_df = population_csv_df[population_csv_df['Rank'] <= 10]

print(rank_10_df)

            #declaring the specific ountries
specific_countries = ['Bangladesh', 'Brazil']

            #list of specific countries using the .isin() function
#
list_of_specific_countries_using_isin = population_csv_df[population_csv_df['Country'].isin(specific_countries)]
print(list_of_specific_countries_using_isin)

              #list of specific countries using the .contains() function     similar to SQL like function  
list_of_specific_countries_using_contains  = population_csv_df[population_csv_df['Country'].str.contains('Nigeria', 'Pakistan')] #for multiple countries we'd use ('Nigeria|Pakistan')
print(list_of_specific_countries_using_contains)

                #setting indexes and filtering the whole CSV into a brand new daraframe where we only want to see specific columns
population_csv_2_df = population_csv_df.set_index('Country')
print(population_csv_2_df)

population_csv_2_df = population_csv_2_df.filter(items = ['Rank', 'Continent', 'World Population Percentage', 'Growth Rate'])
print(population_csv_2_df)


                #filtering by ascending or descending
#filtering by the rank and continent, and specifying how to filter based on each individiual column
population_csv_2_df = population_csv_2_df[population_csv_2_df['Rank'] < 10].sort_values(by=['Rank', 'Continent'], ascending=[False,True])
print(population_csv_2_df)