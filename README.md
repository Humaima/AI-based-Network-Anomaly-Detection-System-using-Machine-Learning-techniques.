# AI-based-Network-Anomaly-Detection-System-using-Machine-Learning-techniques.
This project implements an AI-based Network Anomaly Detection System using machine learning techniques to identify and predict potential security threats and anomalies in network traffic. The system is built using the UNSW-NB15 dataset, which includes various network traffic features such as protocols, services, packet sizes, and byte counts. 
![Screenshot 2024-09-10 013204](https://github.com/user-attachments/assets/83b4f64c-6b8f-4a60-96d0-291007c97515)
# Dataset
The UNSW-NB15 dataset is utilized for training and testing the model. This dataset includes various attributes related to network traffic, such as:
1. Protocols (e.g., TCP, UDP)
2. Services (e.g., HTTP, FTP)
3. Packet Sizes (e.g., number of bytes)
4. Traffic Features (e.g., source bytes, destination bytes, number of packets)

# Machine Learning Model
The core of the anomaly detection system is built around the Random Forest model, which is a powerful ensemble learning technique. Here’s how it is employed:
# Random Forest Model
Random Forest is an ensemble learning method that constructs multiple decision trees during training and outputs the mode of the classes (classification) or mean prediction (regression) of the individual trees.
# Advantages:
- Handles large datasets with higher dimensionality efficiently.
- Robust to overfitting due to its ensemble nature.
- Provides feature importance scores, which can help in understanding the significance of various network features in anomaly detection.
![Screenshot 2024-09-10 014502](https://github.com/user-attachments/assets/d479563b-70cd-48b4-b44b-6b6a40f9b324)
![Screenshot 2024-09-10 014332](https://github.com/user-attachments/assets/9ccbd45c-7392-4bbf-8529-16efd9c345be)
# Implementation
# Data Preprocessing:
1. Cleaning: Handle missing values and outliers.
2. Feature Encoding: Convert categorical features into numerical representations.
3. Normalization: Scale features to ensure uniformity and improve model performance.
# Model Training:
- Split the dataset into training and testing sets.
- Train the Random Forest model on the training set, optimizing hyperparameters such as the number of trees, tree depth, and minimum samples split.
# Evaluation:
- Evaluate the model's performance using metrics such as accuracy, precision, recall, and F1 score.
- Perform cross-validation to ensure the model's robustness and generalization capability.
# Anomaly Detection:
Use the trained Random Forest model to predict anomalies in new network traffic data.
Flag suspicious activities and generate alerts based on the model's predictions.
# Visualization:
Provide visualizations such as confusion matrices and feature importance charts to interpret the model's performance and insights.
Benefits
# Scalability: 
Capable of handling large datasets and complex features.
# Accuracy: 
Effective in identifying anomalies and reducing false positives due to the ensemble approach.
# Interpretability: 
Feature importance scores offer insights into which network features are critical for detecting anomalies.
