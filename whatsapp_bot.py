import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=['POST'])
def whatsapp_reply():
    # 1. Capture incoming message text and convert to lowercase
    incoming_msg = request.values.get('Body', '').lower().strip()
    
    response = MessagingResponse()
    msg = response.message()

    # 2. Check for morning greetings
    if "good morning" in incoming_msg or incoming_msg == "gm":
        msg.body("Good morning")
        return str(response)
        
    # 3. Check for night greetings
    elif "good night" in incoming_msg or incoming_msg == "gn":
        msg.body("Good night")
        return str(response)
        
    # 4. Ignore everything else completely
    else:
        return ""

if __name__ == "__main__":
    # Dynamically assigns the port required by cloud hosting
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)