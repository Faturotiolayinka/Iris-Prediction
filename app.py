from flask import Flask, render_template, request
import numpy as np
import joblib  # Assuming you are using joblib to load your prediction model

app = Flask(__name__)

# Load your prediction model (update the path as necessary)
model = joblib.load('path/to/your/model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from the form
    input_data = request.form.get('input_data')  # Adjust based on your form input names
    # Preprocess the input data as necessary
    processed_data = np.array([[float(x) for x in input_data.split(',')]])  # Example for CSV input

    # Make prediction
    prediction = model.predict(processed_data)

    return render_template('index.html', prediction=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)