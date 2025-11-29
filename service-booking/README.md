# Service Booking System (Flask + Firestore)  

A simple backend system to manage services and bookings using **Flask** and **Google Firestore**.  
Users can view available services, select time slots, and book them. Duplicate bookings are prevented.  

---

## Features ✅

- View available services and their time slots  
- Book a slot for a service  
- Prevent duplicate bookings for the same slot  
- Store bookings in Firestore with structured data  
- Lightweight backend with minimal setup  

---

## Tech Stack 🛠

- **Backend**: Flask (Python)  
- **Database**: Firestore (Firebase)  

---

## Firestore Structure 📂

### Collection: `services`
| Document ID | Fields |
|------------|--------|
| `haircut` | `name: "Haircut"`<br>`slots: ["10:00","11:00","12:00"]` |

### Collection: `bookings`
| Document ID | Fields |
|------------|--------|
| `haircut_11:00` | `service_id: "haircut"`<br>`slot: "11:00"`<br>`user_name: "Yukthi"` |

---

## Setup Instructions ⚡

1. **Clone the repository / create project folder**  

```bash
git clone <your-repo-url>
cd service-booking
# 1️⃣ Create virtual environment
python -m venv venv

# Activate virtual environment
# Linux / Mac
source venv/bin/activate
# Windows
venv\Scripts\activate

# 2️⃣ Install dependencies
pip install -r requirements.txt

# 3️⃣ Add Firebase credentials
# Place your firebase_config.json in the project root
# This file is generated from Firebase → Project Settings → Service Accounts → Generate Key

# 4️⃣ Run Flask server
python app.py

# Server will run at:
# http://127.0.0.1:5000/
