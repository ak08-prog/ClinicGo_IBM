# ClinicGo – Smart Clinic Flow & Worker Efficiency System

**ClinicGo** is a modular AI-powered system designed to streamline patient flow, documentation, and staff efficiency in semi-urban and rural clinics using IBM Granite and Watson technologies.

> 🎯 **Hackathon Submission:** IBM Granite Hackathon 2025  
> 📌 **Theme:** SDG 8 – Decent Work and Economic Growth  
> 🧠 **Team ID:** KPRHX-1162


## 🔍 Problem Statement

In rural and semi-urban areas, clinics suffer from inefficient workflows, long wait times, unstructured records, and overburdened healthcare staff. **ClinicGo** solves this by automating appointment management, report summarization, voice-based consultation records, sentiment analysis, and workload forecasting — powered by Granite foundation models.


## 🚀 Key Features

- 📅 **Smart Appointments** – QR and IVR-based check-ins with real-time slot updates
- 📝 **Granite Medical Report Summarization** – Upload handwritten reports or scanned PDFs and get structured outputs
- 🗣 **Speech-to-Text + NLP Summaries** – Voice consultations are auto-transcribed and converted to clinical summaries
- 📈 **Load Forecasting** – Predicts patient inflow using time-series modeling (Granite)
- ❤ **Patient Feedback Sentiment Analysis**
- 💬 **Doctor Collaboration Chatrooms** – Auto-summarized insights with disease tagging

---

## 🧠 IBM Resources Used

| IBM Technology      | Use Case                                                                 |
|---------------------|--------------------------------------------------------------------------|
| Watsonx.ai (Granite Language) | Summarization, Q&A, medical structuring |
| Watson Speech-to-Text | Converts consultation audio to text                                     |
| Granite Vision Model | Understands scanned documents and handwritten reports                  |
| Granite Time-Series Model | Predicts patient traffic for staffing                              |
| Granite Guardian | Ensures data privacy and bias monitoring                                 |
| IBM Cloud Functions | Handles backend logic and scheduling                                     |
| IBM Cloudant | Stores patient and feedback records securely                                    |
| IBM App ID | Authentication and secure access                                                  |

---

## 📁 Project Structure

bash
ClinicGo/
├── static/                      # Frontend assets (images, styles)
├── templates/                   # HTML templates for web views
├── app.py                       # Main Flask backend application
├── routes/                      # Backend routes and API endpoints
├── ibm_services/                # IBM SDK and Watson integrations
│   ├── granite_nlp.py           # Summarization, Q&A
│   ├── speech_to_text.py       # Watson STT integration
│   ├── vision_model.py         # Granite document analysis
│   └── time_series_forecast.py # Patient load forecasting
├── requirements.txt             # Python dependencies
└── README.md                    # Project description (you are here)
`

---

## 🧪 Setup Instructions

1. Clone the repo:

   bash
   git clone https://github.com/yourusername/clinicgo.git
   cd clinicgo
   

2. Install dependencies:

   bash
   pip install -r requirements.txt
   

3. Add your IBM credentials in `.env` or a config file for:

   * Watsonx.ai / Granite models
   * IBM Cloudant DB
   * Watson STT
   * App ID (optional for secure login)

4. Run the app:

   bash
   python app.py
   

5. Open in browser:
   `http://localhost:5000`

---

## 📷 Architecture Overview

![System Diagram](./static/clinicgo-architecture.jpg)
*Figure: ClinicGo System Flow using Granite + Watson + IBM Cloud*

---

## 🌍 SDG Impact: Decent Work & Economic Growth

ClinicGo directly supports **UN SDG 8** by:

* Reducing healthcare worker fatigue
* Enabling task automation in low-tech environments
* Providing reliable care workflows and affordable access
* Enhancing staff collaboration and data handling



🔗 **Submission ID**: KPRHX-1162
📬 For inquiries: \[[email@example.com](mailto:email@example.com)]

---



Let me know if you'd like me to customize it further (like using your real filenames or adding screenshots). Would you like a downloadable README.md file or commit-ready GitHub folder setup as well?
```
