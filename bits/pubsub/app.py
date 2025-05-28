from flask import Flask, render_template, request, redirect
from flask_pymongo import PyMongo
from azure.messaging.webpubsubservice import WebPubSubServiceClient

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/Learn"
db = PyMongo(app).db

@app.route('/')

def index():
    return "Hello, World!"

@app.route('/notification-send', methods=['POST'])
def login():
    data = request.get_json()
    print("Received JSON:", data)
    amount = data.get("amt")
    termination_id = data.get("tmt_id")
    db.inventory.insert_one({"amount":amount, 
            "termination_id":termination_id})
    message = {"amount":amount, 
            "termination_id":termination_id}
    connection_string = 'Endpoint=https://koili-iot.webpubsub.azure.com;AccessKey=4cUcrZ0LFoOPq0Hsksh85qBjBFXrrDYbNIKKj9zzEBvL3YE3hOKBJQQJ99BBACGhslBXJ3w3AAAAAWPSMlmy;Version=1.0;'
    hub_name = 'Hubs'
    service = WebPubSubServiceClient.from_connection_string(connection_string, hub=hub_name)
    import pdb; pdb.set_trace();
    res = service.send_to_all(message, content_type='application/json')
    
    return "Successful"

@app.route("/usr/<string:usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

if __name__ == "__main__":
    app.run(debug=True)
