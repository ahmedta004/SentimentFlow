
# SentimentFlow

**SentimentFlow** is a highly scalable, real-time Natural Language Processing (NLP) pipeline designed to classify text sentiment with sub-millisecond latency. Built with a strictly modular, **domain-agnostic architecture**, it can seamlessly adapt to any text dataset (Telecom, E-commerce, Reviews) without altering the core engine.

Powered by **FastAPI** for asynchronous high-performance routing and **Scikit-Learn** for lightweight, memory-efficient machine learning, this project demonstrates production-ready engineering practices including scope protection, data leakage prevention, and clean OOP design.

###  Key Architectural Features:

-   **Real-Time Inference:** Utilizes FastAPI's ASGI framework and startup-event model loading to ensure zero disk I/O during client requests.
    
-   **Domain-Agnostic Pipeline:** Completely decoupled Text Preprocessor and Feature Extractor, allowing for immediate retraining on new datasets.
    
-   **Memory & Compute Efficient:** Employs TF-IDF Vectorization and Logistic Regression optimized for sparse matrices to maintain low RAM consumption.
    
-   **Data Validation:** Integrates Pydantic schemas to strictly validate incoming JSON payloads and prevent server crashes.
  
