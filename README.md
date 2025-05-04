# ClinicGo – Smart Clinic Flow & Worker Efficiency System

ClinicGo is an AI-powered platform built to streamline patient management, enhance staff productivity, and digitize operations in small and rural clinics. This repository contains modules that leverage IBM Granite models, Watson services, and open-source AI tools to enable intelligent, low-bandwidth healthcare delivery.

## Key Features

* *QR-Based Smart Check-In System*
* *Medical Report Summarization with IBM Granite*
* *Voice-to-Text Medical Note Automation*
* *Real-Time Queue & Load Forecasting*
* *Sentiment-Based Feedback Analysis*
* *Secure Internal Chat with Summary Support*
* *Visual Patient Counter (YOLOv8)*

## Folder Structure


ClinicGo/
├── Frontend/                   # Frontend interface files
│   ├── about.py           # Main UI component
│    |── demo-video.mp4     # Example: output (2).mp4
│
├── Watson_Chatbot/            # Chatbot components
│   ├── chatbot_interface.py
│   
│
├── Analyzer.ipynb             # Medical report analysis notebook
├── qr_code.ipynb              # QR check-in system notebook
├── trend_analysis.ipynb       # Predictive analytics notebook
├── voicetotext.ipynb          # Speech-to-text processing
├── yolov8_clinic_counter.py   # Vision-based patient counter
├── sample_medical_report.pdf  # Test document
└── README.md                  # Project documentation


## Technologies & AI Models Used

* *IBM Granite Language Models (Granite-3B-Instruct, etc.)*
* *IBM Granite Vision Models*
* *IBM Granite Time-Series Models*
* *Watson Speech-to-Text (STT)*
* *YOLOv8 for visual patient flow estimation*
* *Streamlit (optional for UI prototyping)*
