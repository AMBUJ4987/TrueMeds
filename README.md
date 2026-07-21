# TrueMeds

An AI-assisted medicine verification platform that helps identify counterfeit, spurious, recalled, and Not of Standard Quality (NSQ) medicines by combining OCR, Computer Vision, and official regulatory databases.

---

## Overview

Counterfeit and substandard medicines continue to pose a significant threat to public health. Consumers often have no practical way to verify whether a medicine is genuine before consumption.

TrueMeds is an intelligent verification platform that extracts medicine information from package images, validates it against official CDSCO regulatory records, analyzes packaging integrity using computer vision, and generates a comprehensive verification report.

The platform is designed as an AI-powered decision support system and does not replace laboratory testing or regulatory inspection.

---

## Problem Statement

Develop an AI-powered medicine verification platform capable of assisting users in identifying counterfeit, recalled, and Not of Standard Quality (NSQ) medicines using computer vision, OCR, and official regulatory datasets.

---

# Current Progress

### Completed

- Regulatory dataset collection and preprocessing
- CDSCO NSQ dataset integration
- CDSCO Spurious Drug dataset integration
- CDSCO Drug Recall dataset integration
- Automated PDF-to-CSV extraction pipeline
- Dataset normalization and cleaning pipeline
- Master pharmaceutical verification database creation (700+ verified records)
- Risk classification pipeline

### In Progress

- OCR Pipeline
- Computer Vision Packaging Analysis
- Verification Engine
- Backend API Development

---

## Features

### Implemented

- Government regulatory database integration
- Automated PDF extraction and preprocessing
- Master medicine verification database
- Risk classification using regulatory alerts

### Planned

- Medicine image upload
- OCR extraction of:
  - Drug Name
  - Batch Number
  - Manufacturer
  - Manufacturing Date
  - Expiry Date
- Semantic medicine search
- AI-powered packaging anomaly detection
- Verification confidence scoring
- Community reporting
- Analytics dashboard

---

# System Architecture

```text
                    Medicine Image
                           │
                           ▼
              Image Preprocessing (OpenCV)
                           │
                           ▼
                 OCR Extraction (PaddleOCR)
                           │
                           ▼
              Structured Information Parsing
                           │
          ┌────────────────┴────────────────┐
          ▼                                 ▼
  CDSCO Regulatory Search          Semantic Drug Search
          └────────────────┬────────────────┘
                           ▼
            Gemini Vision Packaging Analysis
                           ▼
               AI Risk Assessment Engine
                           ▼
                Comprehensive Verification Report
```

---

## Verification Pipeline

1. User uploads a medicine package image.
2. Image preprocessing improves OCR readability.
3. PaddleOCR extracts textual information.
4. Drug information is parsed into structured fields.
5. Extracted information is verified against official CDSCO datasets.
6. Gemini Vision analyzes packaging quality and detects anomalies.
7. The Risk Assessment Engine combines all evidence.
8. A comprehensive verification report is generated.

---

## Tech Stack

### Frontend

- React.js
- Tailwind CSS

### Backend

- FastAPI
- Python

### Artificial Intelligence

- PaddleOCR
- Google Gemini Vision API
- OpenCV
- RapidFuzz (Fuzzy Matching)

### Database

- MongoDB

### Data Processing

- Pandas
- NumPy
- pdfplumber

---

## Dataset

The verification database has been constructed using publicly available CDSCO regulatory records.

### Sources

- CDSCO NSQ Drug Alerts
- CDSCO State NSQ Drug Alerts
- CDSCO Spurious Drug Alerts
- CDSCO Drug Recall Alerts

### Current Database

- 700+ normalized medicine records
- Automated PDF parsing pipeline
- Unified master verification database
- Regulatory risk classification

---

## Repository Structure

```text
TrueMeds/
│
├── frontend/
│
├── backend/
│
├── ai/
│   ├── ocr/
│   ├── vision/
│   └── risk_engine/
│
├── datasets/
│   ├── pdfs/
│   ├── csv/
│   └── master_final.csv
│
├── docs/
│
├── assets/
│
├── README.md
│
└── requirements.txt
```

---

## Development Roadmap

### Phase 1 — Data Engineering

- [x] CDSCO dataset collection
- [x] PDF parsing pipeline
- [x] Dataset normalization
- [x] Master verification database
- [x] Risk classification

### Phase 2 — AI Pipeline

- [ ] Image preprocessing
- [ ] PaddleOCR integration
- [ ] Information extraction
- [ ] Semantic medicine search
- [ ] Gemini Vision integration

### Phase 3 — Verification Engine

- [ ] Regulatory verification
- [ ] Packaging anomaly detection
- [ ] AI risk scoring
- [ ] Verification confidence generation

### Phase 4 — Application

- [ ] FastAPI backend
- [ ] React frontend
- [ ] Dashboard
- [ ] Community reporting

---

## Contributors

Team TrueMeds

---

## Disclaimer

TrueMeds is an AI-assisted medicine verification platform intended solely as a decision support system using publicly available regulatory information.

The platform does **not** certify the authenticity, efficacy, or safety of any pharmaceutical product and must not be considered a substitute for laboratory analysis, regulatory inspection, or professional medical advice.

---

## License

This project is being developed for Smart India Hackathon (SIH) and educational research purposes.
