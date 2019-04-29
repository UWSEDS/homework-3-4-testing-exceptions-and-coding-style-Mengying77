# HW2 - Using Functions
""" 1. Find an on-line data source (e.g., from data.gov). Write python codes that 
read the on-line file and create a data frame that has at least 3 columns."""
import pandas as pd
data = pd.read_csv('https://data.cityofnewyork.us/api/views/kku6-nxdu/rows.csv?accessType=DOWNLOAD', sep=',', header = 0)
#data.head(5)

df = data.loc[:,['COUNT PARTICIPANTS','COUNT PERMANENT RESIDENT ALIEN', 'COUNT US CITIZEN', 
          'COUNT CITIZEN STATUS TOTAL', 'COUNT HISPANIC LATINO', 'COUNT AMERICAN INDIAN', 
          'COUNT WHITE NON HISPANIC', 'PERCENT BLACK NON HISPANIC', 'COUNT ASIAN NON HISPANIC']]
#df.head(5)

""" 2. (3 points) Create the function test_create_dataframe that takes a pandas 
    DataFrame as input and returns True if the following conditions hold:
        1. The DataFrame contains only the columns that you specified in #1.
        2. The columns contain the correct data type
        3. There are at least 10 rows in the DataFrame."""
def test_create_dataframe(dataframe):
    list_of_cols = list(df.columns)  # make a list of the names of the columns
    
    # if Dataframe has less than 10 rows, return False
    if dataframe.shape[0] < 10:
        return False
    # check each row if 1) each column names of the dataframe are contained in the one from #1;
    # 2) if datatype of each column is the same as those in #1. Return False if any one is not met.
    for i in list(dataframe.columns):
        if (i not in list_of_cols or dataframe[i].dtype != df[i].dtype):
            return False
    return True

# Test case: Return True
df2 = data.loc[:,['COUNT PARTICIPANTS','COUNT PERMANENT RESIDENT ALIEN', 'COUNT US CITIZEN']]
a = test_create_dataframe(df2)
#print(a)
