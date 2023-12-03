import pandas as pd
import sys
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.tree import plot_tree
from sklearn.metrics import accuracy_score,mean_absolute_error

data = pd.read_csv("C:/xampp/htdocs/agriculture-portal-main/farmer/ML/fertilizer_recommendation/fertilizer_recommendation.csv")

le_soil = LabelEncoder()
data['Soil Type'] = le_soil.fit_transform(data['Soil Type'])
le_crop = LabelEncoder()
data['Crop Type'] = le_crop.fit_transform(data['Crop Type'])

X = data.iloc[:, :8]
y = data.iloc[:, -1]
print(X)
print(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
dtc = DecisionTreeClassifier(random_state=0)
dtc.fit(X, y)
y_pred = dtc.predict(X_test)

# Calculate and print the accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy of the model on the test set: {accuracy}")
print("Number of features in the tree:", dtc.feature_importances_)
fig = plt.figure(figsize=(25,20))
_ = plot_tree(dtc, 
                   feature_names=X.columns,  
                   class_names=data['Fertilizer Name'],
                   filled=True)
plt.show()
# data['Fertilizer Name'] = pd.to_numeric(data['Fertilizer Name'], errors='coerce')
# data = data.dropna(subset=['Fertilizer Name'])# jsonn = sys.argv[1]
# jsonp = sys.argv[2]
# jsonk = sys.argv[3]
# jsont = sys.argv[4]
# jsonh = sys.argv[5]
# jsonsm = sys.argv[6]
# jsonsoil = sys.argv[7]
# jsoncrop = sys.argv[8]

# soil_enc = le_soil.transform([jsonsoil])[0]
# crop_enc = le_crop.transform([jsoncrop])[0]


# user_input = [[jsont,jsonh,jsonsm,soil_enc,crop_enc,jsonn,jsonk,jsonp]]

# fertilizer_name = dtc.predict(user_input)

# print(str(fertilizer_name[0]))