import requests

url = "http://127.0.0.1:5000/notify"


spam_payload = {
    "RecordType": "Bounce",
    "Type": "SpamNotification",
    "TypeCode": 512,
    "Name": "Spam notification",
    "Tag": "",
    "MessageStream": "outbound",
    "Description": "The message was delivered, but was either blocked by the user, or classified as spam, bulk mail, or had rejected content.",
    "Email": "zaphod@example.com",
    "From": "notifications@honeybadger.io",
    "BouncedAt": "2023-02-27T21:41:30Z"
}

not_a_spam_payload = {
  "RecordType": "Bounce",
  "MessageStream": "outbound",
  "Type": "HardBounce",
  "TypeCode": 1,
  "Name": "Hard bounce",
  "Tag": "Test",
  "Description": "The server was unable to deliver your message (ex: unknown user, mailbox not found).",
  "Email": "arthur@example.com",
  "From": "notifications@honeybadger.io",
  "BouncedAt": "2019-11-05T16:33:54.9070259Z",
}

my_own_payload = {
    "Type" : "Custom PayloadSPAM",
    "Time": "Friday night",
    "state": "sitting at home",
    "desired_state": "party",
    "reason_for_not_going": "Who knows",
    "Email": "spambot942@spammer.com"
}

response = requests.post(url, json=my_own_payload)
print(response.text)



