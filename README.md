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
├── Frontend/
│   ├── src/
│   │   ├── about.py          # UI component
│   │   └── styles.css        # Styling
│   ├── assets/
│   │   └── demo-video.mp4    # Video file
│   └── Watson_Chatbot/
│       ├── chatbot_interface.py
│       └── chatbot_logic.py
├── Modules/
│   ├── Analyzer.ipynb        # Medical report analysis
│   ├── qr_code.ipynb         # QR check-in system
│   ├── trend_analysis.ipynb  # Predictive analytics
│   └── voicetotext.ipynb     # Speech processing
├── Computer_Vision/
│   └── yolov8_clinic_counter.py
├── Documentation/
│   ├── sample_medical_report.pdf
│   └── user_guide.md
└── README.md                 # Main documentation (root level)


## Technologies & AI Models Used

* *IBM Granite Language Models (Granite-3B-Instruct, etc.)*
* *IBM Granite Vision Models*
* *IBM Granite Time-Series Models*
* *Watson Speech-to-Text (STT)*
* *YOLOv8 for visual patient flow estimation*
* *Streamlit (optional for UI prototyping)*
