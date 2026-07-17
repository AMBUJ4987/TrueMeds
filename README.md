# TrueMeds

AI-powered medicine verification platform that helps users identify counterfeit, recalled, and substandard medicines using OCR, Computer Vision, and official regulatory databases.

---

## Overview

Counterfeit and substandard medicines remain a significant public health concern, posing serious risks to patient safety and treatment outcomes. Consumers often have no reliable way to verify whether the medicine they purchase is genuine.

**TrueMeds** aims to bridge this gap by providing an AI-assisted verification platform that analyzes medicine packaging, extracts important information using OCR, cross-checks it against official government drug safety databases, and generates an authenticity confidence score.

The platform is designed as an intelligent decision-support tool rather than a replacement for pharmaceutical testing.

---

## Problem Statement

Develop an AI-powered medicine verification platform capable of assisting users in identifying counterfeit, recalled, and Not of Standard Quality (NSQ) medicines by combining computer vision, OCR, and official regulatory datasets.

---

## Features

- Medicine image upload
- OCR-based extraction of:
  - Drug Name
  - Batch Number
  - Manufacturer
  - Manufacturing Date
  - Expiry Date
- AI-powered packaging anomaly detection
- Cross-verification with CDSCO NSQ & Spurious Drug Alerts
- Recall and regulatory alert detection
- Authenticity confidence scoring
- Community reporting of suspicious medicines *(Planned)*
- Analytics dashboard *(Planned)*

---

## System Workflow

```text
Medicine Image
       │
       ▼
OCR Extraction
       │
       ▼
Information Parsing
       │
       ▼
Government Database Verification
       │
       ▼
Vision AI Packaging Analysis
       │
       ▼
Risk Assessment Engine
       │
       ▼
Authenticity Report
```

---

## Tech Stack

### Frontend
- React.js
- Tailwind CSS

### Backend
- FastAPI
- Python

### AI & Machine Learning
- Google Gemini Vision API
- PaddleOCR / EasyOCR
- OpenCV

### Database
- MongoDB

### Data Sources
- CDSCO NSQ Drug Alerts
- CDSCO Spurious Drug Alerts
- CDSCO Drug Recall Alerts
- OpenFDA (Optional)

---

## Project Structure

```
TrueMeds/
│
├── frontend/
├── backend/
├── ai/
├── datasets/
├── docs/
├── assets/
├── models/
├── README.md
└── requirements.txt
```

---

## Project Goals

- Improve consumer awareness regarding counterfeit medicines.
- Simplify medicine verification using AI.
- Integrate trusted government drug safety data.
- Provide a scalable foundation for healthcare safety applications.

---

## Roadmap

- [ ] OCR Pipeline
- [ ] CDSCO Database Integration
- [ ] Vision AI Packaging Analysis
- [ ] Risk Scoring Engine
- [ ] Frontend Dashboard
- [ ] Community Reporting
- [ ] Analytics Dashboard

---

## Contributors

Team TrueMeds

---

## Disclaimer

TrueMeds is an AI-assisted verification platform intended to support users using publicly available regulatory information. The platform does **not** certify the authenticity or safety of medicines and should not be considered a substitute for laboratory testing, regulatory inspection, or professional medical advice.
