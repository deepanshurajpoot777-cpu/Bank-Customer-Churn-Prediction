from preprocessing import x_train, y_train

from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

model.fit(x_train, y_train)

import joblib

joblib.dump(model, "churn_model.joblib")