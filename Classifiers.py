import pandas as pd
data = pd.read_csv("weather_classification_data.csv")
data.info()
from sklearn.utils import shuffle
data = shuffle(data)
data.head()

# START CODE HERE
object_columns = data.select_dtypes(include=['object']).columns.tolist()
non_object_columns = data.select_dtypes(exclude=['object']).columns.tolist()
# END CODE HERE
print(f"Object Columns: {object_columns}\nNon Object Columns: {non_object_columns}")

# DON'T EDIT THIS CELL
if (object_columns == ['Cloud Cover', 'Season', 'Location', 'Weather Type'] and non_object_columns == ['Temperature', 'Humidity', 'Wind Speed', 'Precipitation (%)', 'Atmospheric Pressure', 'UV Index', 'Visibility (km)']):
  print(f"\033[32mTest Passed\033[0m")
else:
  print(f"\033[31mTest Failed\033[0m")

from sklearn.preprocessing import OrdinalEncoder, StandardScaler
from sklearn.compose import ColumnTransformer

# START CODE HERE
ordinal_encoder = OrdinalEncoder()
standard_scaler = StandardScaler()

column_transformer = ColumnTransformer(
    transformers=[
        ('ordinal_encoder', ordinal_encoder, object_columns),
        ('standard_scaler', standard_scaler, non_object_columns)
    ]
)

data_scaled_labeled = column_transformer.fit_transform(data)
# END CODE HERE

all_columns = object_columns + non_object_columns

# Create the new DataFrame
data_scaled_labeled = pd.DataFrame(data_scaled_labeled, columns=all_columns)

# DON'T EDIT THIS CELL
data_scaled_labeled_check = pd.read_csv("data_scaled_labeled_check.csv")
import numpy as np
data_scaled_labeled_values = np.sort(data_scaled_labeled.values,axis=0)
data_scaled_labeled_check_values = np.sort(data_scaled_labeled_check.values,axis=0)
if np.allclose(data_scaled_labeled_values, data_scaled_labeled_check_values, equal_nan=True):
  print(f"\033[32mTest Passed\033[0m")
else:
  print(f"\033[31mTest Failed\033[0m")

X = data_scaled_labeled.drop('Weather Type', axis=1)
y = data_scaled_labeled['Weather Type']

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.9, random_state=10)

# DON'T EDIT THIS CELL
if (len(X_train)==11880 and len(X_test)==1320):
  print(f"\033[32mTest Passed\033[0m")
else:
  print(f"\033[31mTest Failed\033[0m")

if (len(y_train)==11880 and len(y_test)==1320):
  print(f"\033[32mTest Passed\033[0m")
else:
  print(f"\033[31mTest Failed\033[0m")

X_train.head()

# START CODE HERE
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=500, random_state=10)
model.fit(X_train, y_train)
score = model.score(X_test, y_test)

# END CODE HERE

print("Accuracy:", score*100)

# DON'T EDIT THIS CELL
if (score>0.90):
  print(f"\033[32mTest Passed\033[0m")
else:
  print(f"\033[31mTest Failed\033[0m")

input_data = X_test.head(1)
prediction = model.predict(input_data)
print(prediction)