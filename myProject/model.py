import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
 
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import numpy as np

# Suppress warnings
import warnings
from sklearn.exceptions import DataConversionWarning

warnings.filterwarnings(action='ignore', category=UserWarning)
warnings.filterwarnings(action='ignore', category=DataConversionWarning)

# Load the data
stress = pd.read_csv("StressLevelDataset.csv")

# Split the data into features and target

X = stress.drop(["stress_level"], axis=1)
y = stress.stress_level
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

num_classes = len(set(y))

# Neural Network Architecture
model = Sequential()
model.add(Dense(128, input_dim=X_train.shape[1], activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(num_classes, activation='softmax'))

# Compile the Model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the Model
model.fit(X_train, tf.keras.utils.to_categorical(y_train, num_classes=num_classes), epochs=20, batch_size=32, validation_split=0.2)

# Evaluate the Model
y_pred_prob = model.predict(X_test)

# Calculate accuracy
y_pred_prob = model.predict(X_test)
y_pred = np.argmax(y_pred_prob, axis=1)  
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

def predict_stress_level(input_data):
    predicted_probabilities = model.predict(input_data)
    predicted_class = np.argmax(predicted_probabilities)
    
    return predicted_class

sample_input_data = np.array([[15, 8, 1, 15, 5, 3, 1, 4, 3, 1, 5, 4, 5, 2, 4, 5, 5, 5, 4, 4]])
predicted_stress_level = predict_stress_level(sample_input_data)
print("Predicted stress level:", predicted_stress_level)

#importing the model 
import pickle  
with open('modelAnn.pkl','wb') as file:
    pickle.dump(model,file)