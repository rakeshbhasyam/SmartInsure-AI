# 🏥 SmartInsure-AI

A machine learning-powered insurance premium prediction API that helps determine insurance premium categories based on user demographics, lifestyle factors, and location data.

## 🚀 Features

- **AI-Powered Predictions**: Uses a trained machine learning model to predict insurance premium categories
- **Comprehensive Input Validation**: Validates user input with Pydantic models
- **Risk Assessment**: Automatically calculates BMI and lifestyle risk factors
- **City Tier Classification**: Categorizes cities into tiers (1, 2, 3) for location-based pricing
- **Confidence Scoring**: Provides prediction confidence and probability distributions
- **RESTful API**: Clean FastAPI-based REST endpoints
- **Docker Support**: Containerized for easy deployment
- **Health Monitoring**: Built-in health check endpoint

## 📊 Model Details

- **Model Type**: Classification model (pickle format)
- **Version**: 1.0.0
- **Input Features**: BMI, age group, lifestyle risk, city tier, income, occupation
- **Output**: Premium category prediction with confidence scores

## 🛠️ Technology Stack

- **Backend**: FastAPI
- **ML Framework**: scikit-learn
- **Data Validation**: Pydantic
- **Containerization**: Docker
- **Language**: Python 3.11

## 📋 Prerequisites

- Python 3.11+
- Docker (optional)

## 🚀 Quick Start

### Option 1: Using Docker (Recommended)

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/SmartInsure-AI.git
   cd SmartInsure-AI
   ```

2. **Build and run with Docker**
   ```bash
   docker build -t smartinsure-ai .
   docker run -p 8000:8000 smartinsure-ai
   ```

### Option 2: Local Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/SmartInsure-AI.git
   cd SmartInsure-AI
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**

   **Option A: Run both FastAPI and Streamlit together (Recommended)**
   ```bash
   python run_app.py
   ```
   This will start both the FastAPI backend and Streamlit frontend automatically.

   **Option B: Run FastAPI only**
   ```bash
   uvicorn app:app --host 0.0.0.0 --port 8000 --reload
   ```

   **Option C: Run Streamlit frontend only**
   ```bash
   streamlit run frontend.py
   ```

## 📡 API Endpoints

### Base URL
```
http://localhost:8000
```

### Endpoints

#### 1. Home
- **GET** `/`
- **Description**: Welcome message
- **Response**:
  ```json
  {
    "message": "Insurance Premium Prediction API"
  }
  ```

#### 2. Health Check
- **GET** `/health`
- **Description**: API health status and model information
- **Response**:
  ```json
  {
    "status": "OK",
    "version": "1.0.0",
    "model_loaded": true
  }
  ```

#### 3. Predict Premium
- **POST** `/predict`
- **Description**: Predict insurance premium category
- **Request Body**:
  ```json
  {
    "age": 30,
    "weight": 70.5,
    "height": 1.75,
    "income_lpa": 8.5,
    "smoker": false,
    "city": "Mumbai",
    "occupation": "private_job"
  }
  ```
- **Response**:
  ```json
  {
    "response": {
      "predicted_category": "Medium",
      "confidence": 0.8432,
      "class_probabilities": {
        "Low": 0.01,
        "Medium": 0.84,
        "High": 0.15
      }
    }
  }
  ```

## 📝 Input Parameters

| Parameter | Type | Description | Constraints |
|-----------|------|-------------|-------------|
| `age` | integer | User's age | 0 < age < 120 |
| `weight` | float | User's weight in kg | weight > 0 |
| `height` | float | User's height in meters | 0 < height < 2.5 |
| `income_lpa` | float | Annual salary in LPA | income_lpa > 0 |
| `smoker` | boolean | Smoking status | true/false |
| `city` | string | City name | Any valid city name |
| `occupation` | string | User's occupation | See valid options below |

### Valid Occupations
- `retired`
- `freelancer`
- `student`
- `government_job`
- `business_owner`
- `unemployed`
- `private_job`

### City Tiers
The API automatically categorizes cities into tiers:

**Tier 1 Cities**: Mumbai, Delhi, Bangalore, Chennai, Kolkata, Hyderabad, Pune

**Tier 2 Cities**: Jaipur, Chandigarh, Indore, Lucknow, Patna, Ranchi, Visakhapatnam, Coimbatore, and 40+ other cities

**Tier 3 Cities**: All other cities

## 🧮 Computed Features

The API automatically calculates these features from your input:

- **BMI**: `weight / (height²)`
- **Age Group**: 
  - `young` (< 25)
  - `adult` (25-44)
  - `middle_aged` (45-59)
  - `senior` (60+)
- **Lifestyle Risk**:
  - `high`: Smoker with BMI > 30
  - `medium`: Smoker OR BMI > 27
  - `low`: Non-smoker with BMI ≤ 27
- **City Tier**: 1, 2, or 3 based on city classification

## 📁 Project Structure

```
SmartInsure-AI/
├── app.py                 # FastAPI application
├── frontend.py            # Streamlit frontend interface
├── run_app.py             # Startup script for both services
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker configuration
├── config/
│   └── city_tier.py      # City tier definitions
├── model/
│   ├── model.pkl         # Trained ML model
│   └── predict.py        # Prediction logic
└── schema/
    ├── user_input.py     # Input validation schema
    └── prediction_response.py  # Response schema
```

## 🧪 Testing the API

### Using curl

```bash
# Health check
curl -X GET "http://localhost:8000/health"

# Make a prediction
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "age": 30,
    "weight": 70.5,
    "height": 1.75,
    "income_lpa": 8.5,
    "smoker": false,
    "city": "Mumbai",
    "occupation": "private_job"
  }'
```

### Using Python requests

```python
import requests

# Health check
response = requests.get("http://localhost:8000/health")
print(response.json())

# Make a prediction
data = {
    "age": 30,
    "weight": 70.5,
    "height": 1.75,
    "income_lpa": 8.5,
    "smoker": False,
    "city": "Mumbai",
    "occupation": "private_job"
}

response = requests.post("http://localhost:8000/predict", json=data)
print(response.json())
```

## 🔧 Development

### Adding New Cities

To add new cities to the tier system, edit `config/city_tier.py`:

```python
# Add to tier_1_cities for metropolitan cities
tier_1_cities.append("NewCity")

# Add to tier_2_cities for major cities
tier_2_cities.append("AnotherCity")
```

### Model Updates

To update the ML model:

1. Replace `model/model.pkl` with your new trained model
2. Update `MODEL_VERSION` in `model/predict.py`
3. Test the new model thoroughly
4. Update this README if input/output format changes

## 🐳 Docker Commands

```bash
# Build image
docker build -t smartinsure-ai .

# Run container
docker run -p 8000:8000 smartinsure-ai

# Run in background
docker run -d -p 8000:8000 --name smartinsure smartinsure-ai

# View logs
docker logs smartinsure

# Stop container
docker stop smartinsure
```

## 🚀 Running the Application

### Using run_app.py (Easiest Method)

The `run_app.py` script provides the easiest way to run both services:

```bash
python run_app.py
```

**What this script does:**
- ✅ Starts FastAPI backend on `http://127.0.0.1:8000`
- ✅ Starts Streamlit frontend on `http://127.0.0.1:8501`
- ✅ Automatically handles service initialization
- ✅ Provides clear status messages and URLs
- ✅ Graceful shutdown with Ctrl+C

**Services will be available at:**
- 🌐 **FastAPI Backend**: http://127.0.0.1:8000
- 🎨 **Streamlit Frontend**: http://127.0.0.1:8501
- 📚 **API Documentation**: http://127.0.0.1:8000/docs

## 📊 API Documentation

Once the server is running, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
  

## 🙏 Acknowledgments

- Built with [FastAPI](https://fastapi.tiangolo.com/)
- Machine learning powered by [scikit-learn](https://scikit-learn.org/)
- Data validation with [Pydantic](https://pydantic-docs.helpmanual.io/)

---

**Made with ❤️ for smarter insurance predictions**
