
from flask import Flask, request
import json
import requests
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

slack_channel = os.getenv('SLACK_CHANNEL')

def send_slack_message(payload, webhook):
    return requests.post(slack_channel, json.dumps(payload))

@app.route('/notify', methods=['POST'])
def notify():
    payload = json.loads(request.data)
    if 'Type' in payload.keys():
        if 'spam' in str(payload['Type']).lower():
            email = payload['Email']
            message = f"New spam notification: {email}"
            try:
                text = f"Spam Notification alert by Nándor Csupor! email: {email}"
                payload = {"text": text}
                response = send_slack_message(payload, slack_channel)
                print(response)
                return 'Slack notification sent'
            except Exception as e:
                print(f"Error sending Slack notification: {e}")
                return 'Slack notification failed'
        else:
            return 'Payload not a spam notification'
    else:
        return 'Payload not a spam notification'