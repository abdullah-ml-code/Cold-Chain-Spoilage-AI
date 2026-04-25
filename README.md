#  Smart Cold Chain: AI-Powered Spoilage Risk Predictor

![AI Accuracy](https://img.shields.io/badge/Model%20Accuracy-98%25-green)
![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Streamlit](https://img.shields.io/badge/Dashboard-Live-red)

##  Project Overview
Food waste during transit is a global challenge. This project leverages **Machine Learning** to predict spoilage risks in the cold chain logistics industry. By analyzing environmental and operational data, the system provides real-time alerts to prevent loss before it happens.

###  Key Features
- **High-Precision AI:** Achieved a **98% R2 Score** using the Random Forest algorithm.
- **Interactive Dashboard:** A live web-based interface for real-time risk simulation.
- **Data-Driven Insights:** Analyzes critical factors like temperature excursions, humidity, and door-opening events.
- **Mobile Responsive:** Designed to work perfectly on both desktop and mobile devices for field monitoring.

##  Machine Learning Pipeline
1. **Data Cleaning:** Handled missing values and outliers using statistical imputation.
2. **Feature Engineering:** Identified key correlations between ambient conditions and storage safety.
3. **Model Training:** Trained a robust **Random Forest Regressor** for non-linear relationship mapping.
4. **Serialization:** Deployed the model using `joblib` for instant inference.

##  Technology Stack
- **Data Science:** `Pandas`, `NumPy`, `Scikit-learn`
- **Visualization:** `Matplotlib`, `Seaborn`
- **Deployment:** `Streamlit`, `GitHub`, `Joblib`

##  How to Run Locally
1. Clone this repository.
2. Install requirements:
   ```bash
   pip install -r requirements.txt

run the dashboard
   streamlit run app.py