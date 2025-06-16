# Flask Prediction App

This is a Flask web application that provides prediction functionality based on user input. The application is designed to be simple and user-friendly, allowing users to easily interact with the prediction model.

## Project Structure

```
flask-prediction-app
├── app.py                # Main application file
├── requirements.txt      # Dependencies for the application
├── templates             # HTML templates
│   └── index.html       # User interface for input and output
├── static                # Static files
│   └── style.css        # CSS styles for the application
└── README.md             # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd flask-prediction-app
   ```

2. **Create a virtual environment (optional but recommended):**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```
   python app.py
   ```

5. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:5000`.

## Usage

- Input your data in the provided fields on the homepage.
- Click the submit button to get predictions based on your input.
- The predictions will be displayed on the same page.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements for the project.