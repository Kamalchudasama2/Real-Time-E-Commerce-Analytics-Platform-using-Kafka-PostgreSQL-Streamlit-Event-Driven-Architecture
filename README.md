# Real-Time E-Commerce Analytics Platform

## Overview

A real-time event-driven data engineering project that simulates an e-commerce platform where customer orders are processed through Apache Kafka, stored in PostgreSQL, transformed through ETL pipelines, and visualized in a live analytics dashboard.

This project demonstrates modern data engineering concepts including streaming ingestion, event processing, data warehousing, analytics engineering, and real-time business intelligence.

---

## Architecture

Customer Website (Flask)

↓

Kafka Producer

↓

Kafka Topic (ecommerce_orders)

↓

Kafka Consumer

↓

PostgreSQL (Raw Orders)

↓

ETL Layer

↓

Analytics Tables

* city_sales
* product_sales
* daily_sales

↓

Streamlit Dashboard

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

├── templates/

├── static/

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
