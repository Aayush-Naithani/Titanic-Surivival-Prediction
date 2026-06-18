# 🚢 Titanic Survival Prediction using Decision Tree

A Machine Learning web application that predicts whether a passenger would have survived the Titanic disaster based on passenger details such as age, gender, ticket class, fare, embarkation port, and family information.

## 🌐 Live Demo

**Live Application:**
https://titanic-surivival-prediction-render.onrender.com

---

## 📌 Project Overview

The Titanic Survival Prediction project uses a **Decision Tree Classifier** to predict passenger survival. The model is trained on the famous Titanic dataset and deployed as a web application using **Flask** and **Render**.

Users can enter passenger details through an interactive web interface and receive an instant survival prediction.

---

## 🎯 Objective

To build and deploy a machine learning model capable of predicting passenger survival on the Titanic using historical passenger data.

---

## 📊 Dataset Features

The model uses the following features:

* Pclass (Passenger Class)
* Sex (Gender)
* Age
* SibSp (Number of Siblings/Spouses Aboard)
* Parch (Number of Parents/Children Aboard)
* Fare
* Embarked (Port of Embarkation)

### Target Variable

* Survived

  * 1 → Survived
  * 0 → Did Not Survive

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Scikit-Learn
* Flask
* Pickle

### Machine Learning

* Decision Tree Classifier

### Deployment

* Render

---

## 🔄 Machine Learning Pipeline

### Data Preprocessing

* Missing value imputation using SimpleImputer
* One-Hot Encoding for categorical variables
* Feature Scaling using MinMaxScaler
* Feature Selection using SelectKBest (Chi-Square Test)

### Model Training

* Decision Tree Classifier

### Evaluation

* Train-Test Split
* Accuracy Score

---

## 🚀 Project Structure

```text
Titanic-Survival-Prediction/
│
├── static/
│
├── templates/
│   └── index.html
│
├── app.py
├── model.pkl
├── pipe.pkl
├── requirements.txt
├── Procfile
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Aayush-Naithani/Titanic-Survival-Prediction.git
```

### Navigate to Project Folder

```bash
cd Titanic-Survival-Prediction
```

### Create Virtual Environment

```bash
python -m venv myenv
```

### Activate Environment

#### Windows

```bash
myenv\Scripts\activate
```

#### Linux / Mac

```bash
source myenv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

---

## 📈 Workflow

1. User enters passenger details.
2. Flask receives the input.
3. Data passes through the preprocessing pipeline.
4. Decision Tree model predicts survival.
5. Result is displayed on the web page.

---

## 🔮 Future Improvements

* Random Forest Classifier
* XGBoost Classifier
* Model Comparison Dashboard
* Enhanced UI/UX
* Feature Importance Visualization
* Docker Deployment

---

## 👨‍💻 Author

**Aayush Naithani**

* Senior Analyst | Data Analytics Enthusiast
* Skilled in Python, SQL, Power BI, Machine Learning, and Data Visualization

---

## ⭐ If you found this project useful, consider giving it a star on GitHub!


