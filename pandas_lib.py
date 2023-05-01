import pandas as pd
import matplotlib.pyplot as plt
a = [1, 2, 3]
b = pd.Series(a)
print(b)
#to create a label, use the index argument 
b= pd.Series(a, index=["a", "b", "c"])
print(b)
# to create key/value object
person = {"name":"hatim", "age":35, "work":"data management analyst"}
b = pd.Series(person)
print(b)
# to select only some of items, use the index argument 
b=pd.Series(person, index=["name", "work"])
print(b)
#create DataFrame 
data= {"name": ["hatim", "maha", "zakaria"], "age": [35, 29, 37]}
df= pd.DataFrame(data)
print(df)
#DataFrame is table with rows and columns. to return rows, use loc attribute
print(df.loc[0])
print(df.loc[[0,1]]) # when using[], the result is a pandas DataFrame
#to name index, use index argument
df= pd.DataFrame(data,index = ["client1", "client2", "client3"])
#assigne names to the row and column indexes
df.columns.name = "client"
print(df)
#to return specified row
print(df.loc["client1"])
# read csv file
df = pd.read_csv("Uber.csv")
print(df) #print as pandas the first 5 lines and the last 5 lines 
#print(df.to_string()) #print all the entire DataFrame
#to check max-row returned 
#print(pd.options.display.max_rows)
print(df.head()) # print the header and first 5 rows by default
print(df.head(10))# print the header and first 10 rows
print(df.tail()) # print the headers and last 5 rows by default
print(df.tail(10)) # print the headers and last 10 rows 
print(df.info())# info() method used to get information about data
#null values 
print(df.isnull())
print(df.isnull().sum())
#data cleaning
#remove empty cells
new_df = df.dropna()
print(new_df) 
print(new_df.info())
# we had create new dataframe basic from our data without rows contain empty values with changing our data
# to make change in our data, use inplace = True
df.dropna(inplace = True)
print(df.info())
#another way is to replace empty cells with values. to do it, use fillna() method
df=pd.read_csv('Uber.csv')
df.fillna("hatim", inplace=True) # replace empty values by value 130 and this changement will done in DataFrame
#a common way to replace empty value by mean 
df=pd.read_csv("Uber.csv")
df.columns=df.columns.str.replace("*", "")
print(df)
#let use other data 
df=pd.read_csv("data.csv")
x=df['Calories'].mean()
print("this a mean calories is :",x)
df["Calories"].fillna(x, inplace = True)
print(df)
#using interpretor
df=pd.read_csv("data.csv")
df["Calories"].interpolate(inplace = True)
print(df)
#replace empty values by median
df=pd.read_csv("data.csv")
x=df['Calories'].median()
print("this is a median of Calories : ", x)
df["Calories"].fillna(x, inplace = True)
print(df)
#replace empty values by mode
df=pd.read_csv("data.csv")
x=df['Calories'].mode()[0]
print("this is a mode of Calories : ", x)
df["Calories"].fillna(x, inplace = True)
print(df)
#wrong data may causes issues 
for x in df.index: 
    if df.loc[x, "Duration"]>120:
        print("here the rows where we have mistakes in data:\n", df.loc[x])
        df.loc[x,"Duration"] = 120
#removing symbol from columns names
df=pd.read_csv("Uber.csv")
df.columns=df.columns.str.replace("*", "")
print(df)
print(df.info())
#changing a type of date column
#exclude row containing "Totals" value
df=df[df['START_DATE'] !='Totals']
#convert the rest of column to datetime format
df['START_DATE']=pd.to_datetime(df['START_DATE'])
print(df.info())
df=df[df['END_DATE'] != 'Totals']
df['END_DATE']= pd.to_datetime(df['END_DATE'])
print(df.info())
print(df.columns)
'''#duplicates give use wrong result
print(df.duplicated())
#print the rows where the duplicates is True 
duplicates = df.duplicated()
for index, row in df[duplicates].iterrows():
    print("the index of row is : \n ", index)
    print("here there are the rows where duplicated producte: \n ", row)
#to remove duplicates, use the drop_duplicated() method
df.drop_duplicates(inplace= True)
#to find a relationship between each columns. use the correlation function corrs()
print(df.corr())
#plot is best way to visualize
df.plot(kind = 'scatter', x= 'Duration', y='Calories')
plt.show()
df["Duration"].plot(kind = 'hist')
plt.show()
#wrong type of data will give us a wrong result. so always check that we have a same type and convert it if not
uber = pd.read_csv("Uber.csv")
print(uber.head())
print(uber.info())
print(uber.columns)
'''