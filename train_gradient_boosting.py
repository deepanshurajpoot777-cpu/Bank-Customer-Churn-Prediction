from preprocessing import x_train, y_train
from sklearn.ensemble import GradientBoostingClassifier
import joblib

model = GradientBoostingClassifier(random_state=42)

model.fit(x_train, y_train)

joblib.dump(model, "gradient_boosting_model.joblib")