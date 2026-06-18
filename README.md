# 🌐 Phishing URL Detection System

## 📌 Project Overview

The Phishing URL Detection System is a Machine Learning-based web application that identifies whether a website URL is legitimate or potentially phishing. The system analyzes various URL characteristics and uses a trained Random Forest model to predict the safety of a given URL.

The application provides real-time phishing detection through an interactive Streamlit interface, helping users avoid malicious websites and online scams.

---

## 🎯 Objectives

* Detect phishing websites using Machine Learning.
* Analyze URL characteristics to identify suspicious patterns.
* Provide real-time security recommendations to users.
* Improve awareness of phishing attacks and cyber threats.

---

## 🛠 Technologies Used

### Frontend

* Streamlit

### Backend

* Python

### Machine Learning

* Scikit-learn
* Random Forest Classifier

### Libraries

* Pandas
* NumPy
* Pickle
* Regular Expressions (re)

---

## 📂 Project Structure

```
Phishing-URL-Detection/
│
├── app.py
├── train_model.py
├── phishing_model.pkl
├── dataset.csv
├── README.md

```

---

## ⚙️ Working of the System

### Step 1: Data Collection

A phishing URL dataset is loaded from `dataset.csv`.

### Step 2: Data Preprocessing

* Removes unnecessary columns.
* Converts target labels:

  * `1` → Legitimate Website
  * `0` → Phishing Website

### Step 3: Model Training

A Random Forest Classifier is trained using the dataset.

```python
RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
```

The trained model is stored as:

```text
phishing_model.pkl
```

### Step 4: Feature Extraction

The system extracts security-related features from the entered URL.

| Feature               | Description                             |
| --------------------- | --------------------------------------- |
| IP Address Presence   | Detects direct IP usage in URL          |
| URL Length            | Checks whether URL length is suspicious |
| Shortened URL         | Detects services like bit.ly or tinyurl |
| @ Symbol              | Identifies URL redirection attempts     |
| Double Slash Redirect | Detects suspicious redirections         |

### Step 5: Prediction

The extracted features are passed to the trained model, which predicts:

* Legitimate Website
* Suspicious Website
* Phishing Website

---

## 🔍 Feature Extraction Logic

### 1. IP Address Detection

Example:

```text
http://192.168.1.1/login
```

URLs containing IP addresses are often suspicious.

---

### 2. URL Length Analysis

* Less than 54 characters → Safe
* 54–75 characters → Suspicious
* Greater than 75 characters → Risky

---

### 3. URL Shortening Detection

Examples:

```text
bit.ly
tinyurl.com
```

Shortened URLs may hide malicious destinations.

---

### 4. @ Symbol Detection

Example:

```text
http://google.com@malicious-site.com
```

Attackers use this technique to deceive users.

---

### 5. Double Slash Redirect Detection

Example:

```text
http://example.com//phishing
```

Multiple slashes may indicate redirection attempts.

---

## 🚨 Risk Assessment Logic

The application uses both:

1. Machine Learning Prediction
2. Rule-Based Security Checks

Critical phishing patterns:

* Presence of IP address
* URL shortening services
* Presence of '@' symbol

If any critical pattern is detected:

```text
🚨 Phishing Website Detected!
```

---

## 📊 Machine Learning Algorithm

### Random Forest Classifier

Random Forest is an ensemble learning algorithm that combines multiple decision trees and produces predictions through majority voting.

### Advantages

* High accuracy
* Handles large datasets
* Reduces overfitting
* Robust against noisy data

---

## ▶️ How to Run the Project

### Install Dependencies

```bash
pip install streamlit pandas numpy scikit-learn
```

### Train the Model

```bash
python train_model.py
```

### Run the Application

```bash
streamlit run app.py
```

---

## 📈 Applications

* Browser security tools
* Anti-phishing systems
* Cybersecurity awareness platforms
* Enterprise security monitoring
* Educational cybersecurity projects

---

## 🔮 Future Enhancements

* Domain age verification
* SSL certificate analysis
* WHOIS information lookup
* Deep Learning models
* Real-time URL reputation checking
* Browser extension integration

---

## ✅ Conclusion

The Phishing URL Detection System uses Machine Learning and URL feature analysis to identify malicious websites. By combining Random Forest classification with rule-based detection, the system provides an effective and user-friendly solution for phishing prevention and cyber security awareness.
