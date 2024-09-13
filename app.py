# app.py
from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd

app = Flask(__name__)

# Load the models
rf_label_model = joblib.load('rf_label_model.pkl')
rf_cat_model = joblib.load('rf_cat_model.pkl')

# Load the dataset to get attack category names
train_data = 'C:/Users/01-132202-013/Downloads/Datasets/dataset/UNSW_NB15_training-set.csv'
df = pd.read_csv(train_data)
attack_category_names = df['attack_cat'].astype('category').cat.categories.tolist()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Ensure all required fields are present
        required_fields = ['proto', 'service', 'state', 'spkts', 'dpkts', 'sbytes', 'dbytes', 'rate']
        data = {field: request.form.get(field) for field in required_fields}
        
        if not all(data.values()):
            return jsonify({'error': 'Missing form data'}), 400
        
        # Convert to proper types
        data['spkts'] = float(data['spkts'])
        data['dpkts'] = float(data['dpkts'])
        data['sbytes'] = float(data['sbytes'])
        data['dbytes'] = float(data['dbytes'])
        data['rate'] = float(data['rate'])
        
        # Convert to DataFrame
        input_df = pd.DataFrame([data])
        
        # Preprocessing and prediction
        label_pred = rf_label_model.predict(input_df)[0]
        cat_pred = rf_cat_model.predict(input_df)[0]
        
        # Convert numerical category to name
        cat_pred_name = attack_category_names[cat_pred]
        
        return jsonify({
            'label': 'Normal' if label_pred == 0 else 'Attack',
            'attack_category': cat_pred_name
        })
        
    except ValueError as e:
        return jsonify({'error': f'Value error: {str(e)}'}), 400
    except KeyError as e:
        return jsonify({'error': f'Missing key: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': f'Unexpected error: {str(e)}'}), 400

if __name__ == '__main__':
    app.run(debug=True)
