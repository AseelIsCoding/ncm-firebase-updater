# -*- coding: utf-8 -*-
"""Buzz.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bhovy-WpJw75FdwEyFVnQIll2IBX2joI
"""

import requests
import firebase_admin
from firebase_admin import credentials, firestore

# Step 1: Load Firebase service account key
cred = credentials.Certificate("firebase_key.json")  # Make sure this file is in the same folder
firebase_admin.initialize_app(cred)
db = firestore.client()

# Step 2: Fetch JSON from NCM
url = "https://meteo.ncm.gov.sa/public/ews/latest.json"
response = requests.get(url)
alerts = response.json()

# Step 3: Upload alerts to Firestore
for alert in alerts:
    doc_id = str(alert["id"])  # Unique ID for each alert
    db.collection("ncm_alerts").document(doc_id).set(alert)

print("✅ NCM alerts uploaded to Firestore!")
