# SMS Spam Classifier

This project is a web application for classifying SMS messages as spam or not spam using a machine learning model. The application is built using Streamlit, a Python library for creating web applications, and a pre-trained machine learning model.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Model Training](#model-training)
- [License](#license)

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/devsujal/sms-spam-classifier.git
   cd sms-spam-classifier
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Ensure you have the NLTK data required:
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')
   nltk.download('punkt_tab')
   ```

5. Place the pre-trained model files (`vectorizer.pkl` and `model.pkl`) in the root directory of the project.

## Usage

To run the application, use the following command:
```bash
streamlit run app.py
```

This will start a local web server and open the application in your default web browser. You can then enter an SMS message in the text area and click the "Predict" button to see if the message is classified as spam or not spam.

## Project Structure

The project consists of the following files:

- `sms_spam_classifier_demo.py`: The main application file containing the Streamlit code.
- `vectorizer.pkl`: The pre-trained TfidfVectorizer object.
- `model.pkl`: The pre-trained machine learning model.
- `requirements.txt`: A file listing the required Python packages.

## Model Training

The machine learning model used in this project was trained using the following steps:

1. **Data Preprocessing**: The text data was preprocessed by converting to lowercase, tokenizing, removing stop words and punctuation, and stemming.
2. **Vectorization**: The preprocessed text was converted to numerical features using TfidfVectorizer.
3. **Model Training**: A machine learning algorithm was trained on the vectorized data to classify messages as spam or not spam.

The trained `TfidfVectorizer` and model were saved using `pickle` and loaded in the Streamlit application.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.