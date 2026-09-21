# Real-Time Customer Feedback Analyzer (Domain-Agnostic ML Engine)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688?style=flat&logo=fastapi)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F89939?style=flat&logo=scikit-learn&logoColor=white)
![Pytest](https://img.shields.io/badge/Testing-Pytest-yellow?style=flat&logo=pytest)

A production-ready, low-latency microservice designed to ingest, process, and classify customer sentiment in real-time. Built with pure OOP principles, an abstracted configuration layer, and a high-performance FastAPI asynchronous interface.

---

## Architecture Overview
``` mermaid
flowchart TD
    A([Raw Input / API Request]) --> B
    
    subgraph Pipeline [TextPreprocessor Pipeline]
        B[Regex Normalization -> NLTK Stemming]
    end
    
    B --> C[FeatureExtractor: TF-IDF Transform]
    C --> D[ModelBuilder: Logistic Regression Inference]
    D --> E([JSON Response: Sentiment + Confidence Score])
```