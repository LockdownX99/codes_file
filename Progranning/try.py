from flask import Flask,request,jsonify

app = Flask(__name__)

# This is Sophia's core logic
@app.route('/chat', methods=['POST'])
def chat():
    user_data = request.json
    user_message = user_data.get("message", "").lower()
    
    # Simple logic for now - we can add real AI later!
    if "hello" in user_message:
        response = "Hello Sk Miraj Ali! How can I help you today?"
    elif "who are you" in user_message:
        response = "I am Sophia, your AI assistant."
    else:
        response = "That's interesting! Tell me more."
    
    return jsonify({"reply": response})

if __name__ == "__main__":
    # We use 0.0.0.0 so you can access it from your mobile browser
    app.run(host='0.0.0.0', port=5000, debug=True)
