from flask import Flask, request, jsonify

app = Flask(__name__)

# Store feedback in a list (for demonstration purposes)
feedback_data = []

@app.route('/feedback', methods=['POST'])
def collect_feedback():
    data = request.json
    feedback_data.append(data)  # Store feedback
    return jsonify({"message": "Feedback received!"}), 200

@app.route('/education', methods=['GET'])
def get_education_content():
    content = {
        "title": "Phishing Awareness",
        "description": "Learn how to recognize phishing attempts and stay safe online.",
        "tips": [
            "Never click on links in unsolicited emails.",
            "Verify the sender's email address.",
            "Look for spelling and grammatical errors in messages.",
            "Use two-factor authentication whenever possible."
        ]
    }
    return jsonify(content), 200

if __name__ == '__main__':
    app.run(debug=True)
