import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("messy_project_1.csv",encoding='latin1')
print(df)
# print(df.info())
# print(df.isna().sum())

# Remove the extra indentation sides only
# df['name'] = df['name'].str.strip()
# df['gender'] = df['gender'].str.strip() 
# df['city'] = df['city'].str.strip()
# df['department'] = df['department'].str.strip()

# Remove the extra indentation in between and both sides also with resolve upper case and lower case problem
df['name'] = (
    df['name'].str.lower().str.replace(r'\s+',' ',regex=True).str.strip()
)
df['gender'] = (
    df['gender'].str.lower().str.replace(r'\s+',' ',regex=True).str.strip()
)
df['city'] = (
    df['city'].str.lower().str.replace(r'\s+',' ',regex=True).str.strip()
)
df['department'] = (
    df['department'].str.lower().str.replace(r'\s+',' ',regex=True).str.strip()
)

print("\nNan Name")
MN = df[df['name'].isna()]
print("\n",MN['emp_id'])

print("Nan Gender\n")
MFN = df[(df['gender']!="m") & (df['gender']!="f")]
print(MFN['emp_id'])

print("\n Not age : ")
NA = df[df['age'].isna()]
print(NA['emp_id'])

print("\n Not city : ")
NA = df[df['city'].isna()]
print(NA['emp_id'])

print("\n Not salary : ")
NA = df[df['salary'].isna()]
print(NA['emp_id'])

print("\n Not department : ")
NA = df[df['department'].isna()]
print(NA['emp_id'])

print("duplicates are : ")
DN = df[df.duplicated(subset=['name','city','department'])]
print(DN['emp_id'])

# Remove mess from 'Gender'
RGM = df[(df['gender']!='m') & (df['gender']!='f')]
print(RGM['gender']) # find different inserted gender

RMM = df[df['gender']=='male'] #Remove messy male
print(RMM)
df.loc[[6,12],'gender']='m' #Update the data


RMF = df[df['gender']=='female'] #Remove messy female
print(RMF)
df.loc[[1,18],'gender']='f' # Update the data


print("original data updated")
print(df)

#Remove mess from employee id
print(df['emp_id'].info())
df.loc[df['emp_id']>=22,'emp_id']=None
df['emp_id']=df['emp_id'].interpolate(method='linear') # interpolation method is not working for it
print(df)

# use range to sequence the emp_id 
df['emp_id'] = range(1,1+len(df)) #Remove mess from employee id
print(df) 

#Remove mess from age
NanAge = df[df['age'].isna()]
print("messy age : ")
print(NanAge['name'])
df.loc[10,'age'] = 41
print(df)

# Changing multiple datatypes in data frame
df = df.astype({
    'age': 'int',
    'salary': 'int'
})
print(df)

# Remove mess from name by deleting duplicates and Nan values
NanName = df[df['name'].isna()]
print("Nan values in name : ")
print(NanName['emp_id'])
df=df.drop(20) # Delete the row of invalid name 
print(df)

df=df.drop_duplicates(['name','gender','salary','department']) # remove duplicates on the basis of name,'gender','salary','department'
print(df)

#Now again indexing :
df['emp_id'] = range(1,1+len(df))
print(df)

# Now take data to uppercase
df['name']=df['name'].str.upper()
df['gender']=df['gender'].str.upper()
df['department']=df['department'].str.upper()
df['city']=df['city'].str.upper()
print(df)

# Take output 
df.to_excel("C:\\Users\\Hp\\Downloads\\cleaned_practice1.xlsx",index=False)


