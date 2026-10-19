import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("Bank Customer Churn Prediction.csv")
# print(df.head())
print(df.columns)
# Bar chart
churn=df["churn"].value_counts()
plt.bar(churn.index,churn.values)
plt.xticks([0,1],["No churn","churn"])
plt.xlabel("Customer status")
plt.ylabel("Number of customers")
plt.title("Customer churn Distribution")
plt.show()

# Histogram
plt.hist(df["age"],bins=20)
plt.xlabel("Age")
plt.ylabel("Number of Customers")
plt.title("Age Distribution")
plt.show()

#Histogram
plt.hist(df["credit_score"],bins=20)
plt.xlabel("Credit Score")
plt.ylabel("Number of Customers")
plt.title("Credit Card Distribution")
plt.show()

#Histogram
plt.hist(df["balance"],bins=20)

plt.xlabel("Balance")
plt.ylabel("Number of customers")
plt.title("Balance Distribution")
plt.show()

# BAR Graph
gender=df["gender"].value_counts()

plt.bar(gender.index,gender.values)

plt.xlabel("Gender")
plt.ylabel("Number of customers")
plt.title("Gender Distribution")
plt.show()

#scatter
plt.scatter(df["age"],df["balance"])
plt.xlabel("Age")
plt.ylabel("Balance")
plt.title("Age vs Balance")
plt.show()

#Bar
country_churn=df.groupby("country")["churn"].sum()
plt.bar(country_churn.index,country_churn.values)

plt.xlabel("Country")
plt.ylabel("Number of churned Customers")
plt.title("churn by country")
plt.show()
