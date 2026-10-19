import joblib

model = joblib.load("churn_model.joblib")

from preprocessing import x_test,y_test,x_train,y_train

y_pred=model.predict(x_test)


from sklearn.metrics import accuracy_score,f1_score,precision_score,recall_score

accurcy=accuracy_score(y_test,y_pred)
print(accurcy)

precision=precision_score(y_test,y_pred)
print(precision)

recall=recall_score(y_test,y_pred)
print(recall)

f1=f1_score(y_test,y_pred)
print(f1)

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)

print("Confusion Matrix:")
print(cm)

#RANDOM FOREST MODEL JOBLIB..........................

model = joblib.load("random_forest_model.joblib")


from preprocessing import x_test,y_test,x_train,y_train

y_pred=model.predict(x_test)


from sklearn.metrics import accuracy_score,f1_score,precision_score,recall_score

accurcy=accuracy_score(y_test,y_pred)
print(accurcy)

precision=precision_score(y_test,y_pred)
print(precision)

recall=recall_score(y_test,y_pred)
print(recall)

f1=f1_score(y_test,y_pred)
print(f1)


#graidient boosting model...................

model=joblib.load("gradient_boosting_model.joblib")
from preprocessing import x_test,y_test,x_train,y_train

y_pred=model.predict(x_test)


from sklearn.metrics import accuracy_score,f1_score,precision_score,recall_score

accurcy=accuracy_score(y_test,y_pred)
print(accurcy)

precision=precision_score(y_test,y_pred)
print(precision)

recall=recall_score(y_test,y_pred)
print(recall)

f1=f1_score(y_test,y_pred)
print(f1)

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)

print("Confusion Matrix:")
print(cm)
