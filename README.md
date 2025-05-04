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
├── Analyzer.ipynb             # Lab report summarization and Q&A
├── qr_code.ipynb              # QR-code based check-in system
├── trend_analysis.ipynb       # Predictive traffic/load analytics
├── voicetotext.ipynb          # Watson STT for transcription
├── yolov8_clinic_counter.py   # YOLOv8-based patient crowd estimator
├── watson_chatbot.rar         # Custom chatbot with Watson Assistant
├── sample_medical_report.pdf  # Example document for testing AI analyzer
├── Frontend/                  # UI components and media files
│   ├── LICENSE
│   ├── output (2).mp4
│   └── ...


## Technologies & AI Models Used

* *IBM Granite Language Models (Granite-3B-Instruct, etc.)*
* *IBM Granite Vision Models*
* *IBM Granite Time-Series Models*
* *Watson Speech-to-Text (STT)*
* *YOLOv8 for visual patient flow estimation*
* *Streamlit (optional for UI prototyping)*
