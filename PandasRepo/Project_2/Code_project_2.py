import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt

data = pd.read_csv("PANDAS/practice2.csv")

df = pd.DataFrame(data)

# some word available in t so 
word_to_num= {
'ten':10,
'thirty':30,
'seventy thousand' : 70000,
}
word_to_char={
    'male' : 'M',
    'female': 'F',
    'm':'M',
    'f':'F',
}


#Remove mess from salary :
# print(df['salary'].unique()) # print unique items       
def CLR_salary(value):  # work on mess
    if pd.isna(value) :
        return pd.isna()
    
    value = str(value).lower().strip()

    if value is ["not disclosed","","nan","na"]:
        return np.isnan()
    
    if value in word_to_num:
        return word_to_num[value]
    
    value = value.replace("₹","")

    if value.endswith("k"):
        num = re.sub(r"[^\d.]","",value)
        return float(num)*1000
    
    value = re.sub("[^\d.]","",value)

    return float(value) if value != '' else np.nan

# Remove mess from gender
def CLR_gender(gen):
    if pd.isna(gen):
        return np.nan
    
    gen=str(gen).lower().strip()

    if gen in word_to_char :
        return word_to_char[gen]
    
    return gen if gen !='' else np.nan

# Remove mess form gender 
def CLR_age(dob):
    if pd.isna(dob):
        return np.nan
    
    dob = str(dob).lower().strip()

    if dob in word_to_num:
        return word_to_num[dob]
    
    return int(dob) if dob != '' else np.nan

df["salary"]=df["salary"].apply(CLR_salary) # apply function to the salary slab
df['salary']=df["salary"].interpolate(method='linear')
df['gender']=df['gender'].apply(CLR_gender) # apply function to the gender slab
df['age'] = df['age'].apply(CLR_age) # apply function to the age slab
df.loc[6,'age'] = 35 # update age 35 at index=6

# df=df.dropna() # it will remove all row which contain nan value 
df = df.dropna(subset='name') # method for specific drop nan names

df=df.drop_duplicates(['name','city','department']) # drop duplicates on the basis of name,city,department

df['emp_id'] = range(1,1+len(df)) # remove mess from employee id 
print(df)
df.to_csv("finalpractice2.csv",index=False)

# matplotlib pie between salary distribution between diffrent department
sal_it = df[df['department']=='IT']
sal_HR = df[df['department']=='HR']
sal_Admin = df[df['department']=='Admin']
sal_Finance = df[df['department']=='Finance']
sal_Management = df[df['department']=='Management']
plt.title("salary distribution between diffrent department")
plt.legend(loc='upper right',fontsize=5)
plt.pie(x=[sal_it['salary'].sum(),sal_HR['salary'].sum(),sal_Admin['salary'].sum(),sal_Finance['salary'].sum(),sal_Management['salary'].sum()],labels=['IT','HR','Admin','Finance','Management'],autopct="%1.1f%%")
plt.show()
