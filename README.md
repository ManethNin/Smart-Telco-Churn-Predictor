# Smart Telco Churn Predictor

A machine learning project to predict customer churn in telecommunications using various ML algorithms.

## Project Structure

- `EDA/` - Exploratory Data Analysis and data preprocessing
- `pipeline/` - Model training and validation pipelines
- `Production-Ready Telco Churn Predictor/` - Production-ready inference system
- `artifacts/` - Trained models and processed data

## Quick Start

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the production system:
   ```bash
   cd "Production-Ready Telco Churn Predictor"
   python pipelines/streaming_inference_pipeline.py
   ```

## Features

- Data preprocessing and feature engineering
- Multiple ML model comparison
- Hyperparameter tuning
- Production-ready inference pipeline
- Real-time churn prediction

## Models Used

- CatBoost
- Random Forest
- XGBoost
- Logistic Regression