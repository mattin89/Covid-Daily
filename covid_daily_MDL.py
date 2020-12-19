'''
By Mario De Lorenzo, md3466@drexel.edu

Simple python script to extract daily useful data. There are some examples on how to manipulate data to show ratios and
re-order columns. This script can get only daily data and not past data.
'''

import covid_daily

overview = covid_daily.overview(as_json=False) #Download the DataFrame
print(overview.head()) #show first five entries

overview['Ratio Cases/Population'] = overview['TotalCases'][1:-1] / overview['Population'][1:-1] #Create a new column with the ratio of Total Cases over Population
print(overview.head())
overview.sort_values('Ratio Cases/Population', inplace=True, ascending = False) #Sort values in descending order in respect to ratio of Total Cases over Population
print(overview.head())

print(overview[['Country,Other','TotalCases','Population', 'Ratio Cases/Population']].head(20)) #Prints specific columns

overview['index c/p'] = list(range(1,len(overview)+1)) #Gives new index to the ordered DataFrame
#To DO: Find a new method to give index to ordered DataFrame


