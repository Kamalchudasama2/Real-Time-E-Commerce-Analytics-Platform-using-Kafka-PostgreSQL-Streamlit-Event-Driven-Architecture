# Real-Time E-Commerce Analytics Platform

## Overview

A real-time event-driven data engineering project that simulates an e-commerce platform where customer orders are processed through Apache Kafka, stored in PostgreSQL, transformed through ETL pipelines, and visualized in a live analytics dashboard.

This project demonstrates modern data engineering concepts including streaming ingestion, event processing, data warehousing, analytics engineering, and real-time business intelligence.

---

## Architecture
<img width="1536" height="1024" alt="architecture" src="https://github.com/user-attachments/assets/fb34b72d-9d8a-47fa-be60-6c19a591aaf2" />


---

## Technology Stack

### Frontend

* Flask
* HTML
* CSS
* Bootstrap

### Streaming

* Apache Kafka
* Zookeeper

### Database

* PostgreSQL

### Data Engineering

* Python
* ETL Pipelines
* Data Validation
* Logging

### Analytics

* Streamlit
* Plotly
* Pandas

### Containerization

* Docker
* Docker Compose

---

## Features

### Customer Order Portal

* Place customer orders through web interface
* Event-driven order processing
* Kafka producer integration

### Real-Time Streaming

* Kafka topic-based messaging
* Consumer processing pipeline
* Fault-tolerant event handling

### Data Validation

* Mandatory field validation
* Price validation
* Quantity validation
* City validation

### Logging & Monitoring

* Pipeline logging
* Error handling
* Event tracking

### Analytics Dashboard

* Live order feed
* Revenue tracking
* Product performance
* City performance
* Revenue trends
* KPI monitoring

### Data Warehouse Layer

* Raw orders table
* Product sales aggregation
* City sales aggregation
* Daily sales aggregation

---

## Project Structure

real-time-ecommerce-pipeline/

├── producer/

├── database/

├── dashboard/

├── etl/

├── website/templates/

├── website/static/image

├── logs/

├── docker-compose.yml

└── README.md

---

## Dashboard Metrics

* Total Orders
* Total Revenue
* Average Order Value
* Revenue by City
* Revenue by Product
* Daily Revenue Trends
* Top Customers
* Recent Orders

---

## Business Impact

The platform simulates how modern organizations process customer transactions in real time and transform raw transactional data into actionable business insights.

---

## Future Enhancements

* Spark Streaming Integration
* Airflow Orchestration
* Cloud Deployment (AWS/Azure/GCP)
* Data Lake Integration
* Machine Learning Recommendations
* Real-Time Fraud Detection

---
# Clone repository

git clone url

cd real-time-ecommerce-pipeline

# Install dependencies

pip install -r requirements.txt

# Start Kafka & PostgreSQL

docker compose up -d

# Start Flask Website

python app.py

# Start Kafka Consumer

python database/postgres_consumer.py

# Run ETL

python etl/etl_pipeline.py

# Launch Dashboard

python -m streamlit run dashboard/app.py
