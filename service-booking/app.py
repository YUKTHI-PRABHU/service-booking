from flask import Flask, request, jsonify
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials, firestore

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains (frontend access)

# Initialize Firebase
cred = credentials.Certificate("firebase_config.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Get all services and slots
@app.route('/services', methods=['GET'])
def get_services():
    services = db.collection('services').stream()
    data = {}
    for s in services:
        data[s.id] = s.to_dict()
    return jsonify(data)

# Book a slot
@app.route('/book', methods=['POST'])
def book_slot():
    data = request.get_json()
    service_name = data.get('service')
    slot_time = data.get('slot')
    user_name = data.get('user')

    if not service_name or not slot_time or not user_name:
        return jsonify({"error": "Missing data"}), 400

    # Check if slot is already booked
    booked_slots = db.collection('bookings')\
                     .where('service', '==', service_name)\
                     .where('slot', '==', slot_time).stream()
    if any(booked_slots):
        return jsonify({"error": "Slot already booked"}), 400

    # Add booking
    db.collection('bookings').add({
        "service": service_name,
        "slot": slot_time,
        "user": user_name
    })

    return jsonify({"message": "Booking confirmed!"})

if __name__ == '__main__':
    app.run(debug=True)
