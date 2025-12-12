## Author: Chris McDonald
## Creation Date: 16-May-2025
## Last Updated: 13-June-2025

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('linear-regression/data/advertising.csv', index_col=0)

eval = df.sample(n=5, random_state=42) ## Pick rows for final visual testing
df = df.drop(eval.index) ## Drop rows from DataFrame

X = df[['TV', 'radio', "newspaper"]]
y = df['sales']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler() ## Scalar for input features
model = LinearRegression()

X_train = scaler.fit_transform(X_train) ## Fit scaler only to training data
X_test = scaler.transform(X_test) ## Transforming test data using fitted scaler to avoid data leakage
X_eval = scaler.transform(eval[['TV', 'radio', 'newspaper']])
y_eval = eval['sales'].values[0]

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Scaler MSE: {mse}\nScaler R2: {r2}")

y_eval_pred = model.predict(X_eval)[0]

print(f"Evaluating model using: {X_eval}\n\n")
print(f"Scaler redicted sales: {y_eval_pred:.2f}")
print(f"Actual sales: {y_eval}")

print("Model coefficients:", model.coef_)
print("Model intercept:", model.intercept_)
