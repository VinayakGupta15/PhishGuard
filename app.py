import streamlit as st
import joblib
import requests  # Add this import for making HTTP requests

# Load model and vectorizer
model = joblib.load('phishing_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

# App title and description
st.title("Phishing Detection Chatbot")
st.write("Enter a message to analyze if it's a phishing attempt or not.")

# User input
user_input = st.text_area("Message:", height=100)

if st.button("Analyze"):
    if user_input.strip():
        # Preprocess input and predict
        input_vectorized = vectorizer.transform([user_input])
        prediction = model.predict(input_vectorized)[0]
        risk = "Phishing" if prediction == 1 else "Not Phishing"
        
        # Display result
        st.subheader("Analysis Result")
        st.write(f"Risk Level: **{risk}**")
        
        if prediction == 1:
            st.warning("This message might be a phishing attempt! Be cautious.")
            st.write("""**Tips:** - Avoid clicking unknown links. - Verify the sender's details. - Be wary of urgent requests.""")
        else:
            st.success("This message seems safe.")
    else:
        st.error("Please enter a valid message.")

# Feedback collection
if st.button("Submit Feedback"):
    feedback = {
        "message": user_input,
        "helpful": st.selectbox("Was this helpful?", ["yes", "no"])
    }
    response = requests.post('http://localhost:5000/feedback', json=feedback)
    st.success(response.json().get("message"))

# Fetch educational content
if st.button("Get Educational Content"):
    response = requests.get('http://localhost:5000/education')
    content = response.json()
    st.subheader(content['title'])
    st.write(content['description'])
    for tip in content['tips']:
        st.write(f"- {tip}")