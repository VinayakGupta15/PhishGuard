# 🛡️ PhishGuard: Phishing Detection Chatbot
![alt test](/logo.webp)

## 🌟 **Overview**
The **PhishGuard: Phishing Detection Chatbot** is a Natural Language Processing (NLP) based project that analyzes incoming messages (emails, SMS, or social media messages) to identify potential phishing attempts. It utilizes advanced NLP techniques like text classification, sentiment analysis, and Named Entity Recognition (NER) to detect phishing patterns. Built with **Python** and **Streamlit**, this chatbot ensures real-time analysis and provides users with instant feedback on message safety.

---

## 🛠️ **Features**
- **Real-time Analysis**: Analyze messages as they arrive.
- **Phishing Pattern Recognition**: Detect common phishing tactics such as:
  - Urgent requests
  - Suspicious links/attachments
  - Grammatical errors
  - Impersonation attempts
- **User Education**: 
  - Feedback on the potential risk level of the message.
  - Tips on identifying and avoiding phishing scams.

---

## 🚀 **How It Works**
1. **Text Input**: The user inputs a message into the chatbot interface.
2. **Preprocessing**:
   - Tokenization and text cleaning.
   - TF-IDF vectorization for feature extraction.
3. **Intent Classification**:
   - A **Logistic Regression** model classifies the message as "Phishing" or "Not Phishing."
   - Sentiment Analysis detects urgency in the message.
   - NER identifies entities like URLs, email addresses, and sender names.
4. **Output**: 
   - Display a risk level (e.g., Low, Medium, High).
   - Provide tips to educate users on phishing scams.

---

## 📦 **Project Structure**
```
├── app.py                    # Main Streamlit app file
├── requirements.txt          # Python dependencies
├── data/
│   ├── phishing_dataset.csv  # Dataset used for training
├── models/
│   ├── logistic_model.pkl    # Trained Logistic Regression model
├── utils/
│   ├── preprocessing.py      # Data preprocessing functions
│   ├── ner_analysis.py       # NER and sentiment analysis functions
├── README.md                 # Project documentation
```

---

## 🔧 **Setup Instructions**
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/VinayakGupta15/PhishGuard.git
cd PhishGuard
```

### 2️⃣ Create and Activate a Virtual Environment
```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application
```bash
streamlit run app.py
```
### 🛠️ Troubleshooting

If you are using PowerShell, prefix the command with ```python -m```:
```bash
python -m streamlit run app.py
```
If you encounter permission errors, use:
```bash
python -m pip install streamlit --user
```

## 📊 **Dataset**
The project uses a dataset containing labeled phishing and legitimate messages. Each message is classified as:
- **Phishing**: Messages designed to steal personal information.
- **Not Phishing**: Legitimate and safe messages.

---

## 🧠 **Technical Details**
### **1. NLP Techniques**
- **Tokenization**: Breaks messages into individual words/tokens.
- **TF-IDF Vectorization**: Extracts important features from text.
- **NER (Named Entity Recognition)**: Identifies entities like URLs and sender names.
- **Sentiment Analysis**: Detects urgency in the message text.

### **2. Machine Learning**
- A **Logistic Regression Model** is trained to classify messages as:
  - **Phishing**
  - **Not Phishing**
- The model is saved as `logistic_model.pkl` and loaded into the Streamlit app.

### **3. Deployment**
The chatbot interface is built using **Streamlit**, ensuring a clean, responsive, and user-friendly experience.

---

## 🌐 **Using the Chatbot**
1. Input a message in the text box.
2. The chatbot will analyze the message and display:
   - **Risk Level** (e.g., Low, Medium, High).
   - Detailed explanations of why the message is flagged.
   - Educational tips on identifying phishing attempts.

---

## 🛠️ **Technologies Used**
- **Programming Language**: Python
- **Framework**: Streamlit
- **Machine Learning**: Logistic Regression
- **NLP Libraries**: NLTK, SpaCy, Scikit-learn
- **Deployment Environment**: Visual Studio Code

---

## 🤔 **Future Scope**
- Incorporate **Deep Learning** models like LSTMs or Transformers for better accuracy.
- Add multi-language support.
- Expand phishing tactics detection using advanced datasets.
- Integrate chatbot with messaging platforms (e.g., WhatsApp, Email clients).

---
