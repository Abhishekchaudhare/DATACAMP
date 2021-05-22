import pandas as pd
titanic=pd.read_csv("HOW TO\Titanic.csv")
import re

#1 contains method
#e at any place
#print(titanic[titanic.sex.str.contains('e',regex=False)])
#e at second place only, only female dataframe
female_titanic=titanic[titanic.sex.str.contains('^[a-z]e',regex=True)]
#print(female_titanic['sex'].value_counts())
#only extract a column
#1st method
female_col1=titanic[titanic.sex.str.contains('^[a-z]e',regex=True)]['sex']
#print(female_col1)
#2nd method
female_col2=titanic.loc[titanic.sex.str.contains('^[a-z]e',regex=True),'sex']
#print(female_col2)


#2 Replace method
#1st 
titanic['sex_2']=titanic['sex'].str.replace(r'ma','00')
#print(titanic['sex_2'])

#2nd 
titanic['sex_3']=titanic['sex'].str.replace(r'male$','ladka')
print(titanic['sex_3'])

