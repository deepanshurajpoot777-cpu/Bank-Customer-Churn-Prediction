from preprocessing import x_train, y_train
from sklearn.ensemble import RandomForestClassifier
import joblib

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(x_train, y_train)

joblib.dump(model, "random_forest_model.joblib")