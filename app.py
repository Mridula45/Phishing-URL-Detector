import streamlit as st
import pickle
import numpy as np
import re

# Load model
model = pickle.load(open("phishing_model.pkl", "rb"))

st.set_page_config(page_title="Phishing Detector", page_icon="🌐")

st.title("🌐 Phishing URL Detection System")
st.write("Enter a website URL to check if it is safe or phishing")

# Input
url = st.text_input("Enter Website URL")

# ---------------- FEATURE EXTRACTION ----------------
def extract_features(url):

    features = []

    # 1. IP address
    if re.search(r'\d+\.\d+\.\d+\.\d+', url):
        features.append(-1)
    else:
        features.append(1)

    # 2. URL length
    if len(url) < 54:
        features.append(1)
    elif 54 <= len(url) <= 75:
        features.append(0)
    else:
        features.append(-1)

    # 3. Shortening service
    if "bit.ly" in url or "tinyurl" in url:
        features.append(-1)
    else:
        features.append(1)

    # 4. @ symbol
    if "@" in url:
        features.append(-1)
    else:
        features.append(1)

    # 5. Double slash redirect
    if "//" in url[7:]:
        features.append(-1)
    else:
        features.append(1)

    return features

# ---------------- BUTTON ----------------
if st.button("Check URL"):

    if url.strip() == "":
        st.warning("⚠️ Please enter a URL")

    else:
        # Extract features
        features = extract_features(url)

        # Prepare model input
        total_features = model.n_features_in_

        full_input = np.ones((1, total_features))  # safe defaults
        full_input[0][:5] = features

        # Prediction
        prediction = model.predict(full_input)

        # Risk score
        risk_score = features.count(-1)

        # ---------------- FINAL LOGIC ----------------
        # Strong phishing rules
        if "@" in url or "bit.ly" in url or re.search(r'\d+\.\d+\.\d+\.\d+', url):
            st.error("🚨 Phishing Website Detected! (Critical Pattern)")

        elif risk_score >= 2:
            st.error("🚨 Phishing Website Detected!")

        elif prediction[0] == 1:
            st.success("✅ Legitimate Website")

        else:
            st.warning("⚠️ Suspicious Website")

        # Debug info (helps in viva)
        st.write("### 🔍 Debug Info")
        st.write("Extracted Features:", features)
        st.write("Risk Score:", risk_score)
        st.write("Model Prediction:", prediction[0])