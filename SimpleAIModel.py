# Step 1: Import the tools
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

#Give the ai numbers and there corresponding values telling if they are large or small numbers
X = [[10], [20], [30], [70], [80], [100]]
Y=[0, 0, 0, 0, 0, 1]

#Ai actually reads the numbers and connects the dots
model = DecisionTreeClassifier()
model.fit(X, Y)

#Ai makes the prediction
print("Prediction for 999:", model.predict([[999]])[0])
print("Prediction for 1000:", model.predict([[1000]])[0])



