import pandas as pd
from sklearn.preprocessing import LabelEncoder

df=pd.read_csv("Bank Customer Churn Prediction.csv")

# Data encode
le=LabelEncoder()
df["gender"]=le.fit_transform(df["gender"])
df=pd.get_dummies(df,columns=["country"],drop_first=True,dtype=int)

print("/n After encoding")
print(df.tail())

print("\n columns")
print(df.columns)

print("\n Data Type")
print(df.dtypes)
#Feature and target
x=df.drop("churn",axis=1)
y=df["churn"]

print("\nFeatures")
print(x.head())

print("\nTarget")
print(y.head())

# train test split
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

# feature scalling
from sklearn.preprocessing import StandardScaler

scaler=StandardScaler()
x_train=scaler.fit_transform(x_train)
x_test=scaler.transform(x_test)

import joblib

joblib.dump(scaler, "scaler.joblib")