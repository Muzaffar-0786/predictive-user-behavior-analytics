# Predictive User Behavior Analytics MVP

A production-ready FastAPI microservice designed to analyze user behavioral metrics, evaluate churn risks, and automate targeted retention strategies.

This MVP processes user engagement data, applies rule-based churn analysis, and stores analytical insights to support data-driven customer relationship management.

---

## 🚀 Current Capabilities

### ⚡ API Architecture
- Built using **FastAPI** for fast and lightweight backend API development.
- Clean routing structure with separated application components.

### 🗄️ Database Integration
- Uses **SQLAlchemy ORM** for database operations.
- Currently powered by **SQLite** for storing user behavior analytics logs.
- Supports persistent storage of churn analysis results.

### 📊 Churn Risk Analysis
- Implements a rule-based heuristic system to evaluate user churn probability.
- Automatically categorizes users into:
  - **HIGH Risk**
  - **MEDIUM Risk**
  - **LOW Risk**

- Generates targeted retention suggestions based on behavioral metrics.

### 🐳 Containerization Ready
- Includes a Docker configuration for consistent application deployment.
- Designed for easy migration to cloud environments.

---

# 📁 Project Structure

```text
project/
│
├── auth.py              # Reserved for future authentication infrastructure
├── database.py          # SQLAlchemy engine and database session configuration
├── Dockerfile           # Docker application deployment configuration
├── .env                 # Environment variable configuration
├── main.py              # FastAPI application entry point
├── models.py            # SQLAlchemy ORM database models
├── requirements.txt     # Python package dependencies
├── routes.py            # API endpoint definitions
└── schemas.py           # Pydantic request and response validation schemas
```

---

# 🔌 API Endpoints

## Analyze User Behavior

```
POST /analytics/analyze
```

### Functionality:
- Accepts user activity metrics.
- Calculates churn risk.
- Generates retention recommendations.
- Stores analytics data in the database.

---

## Get Analytics Logs

```
GET /analytics/logs
```

### Functionality:
- Retrieves stored user behavior analytics records.

---

## Health Check

```
GET /health
```

### Functionality:
- Provides service availability status for monitoring and deployment platforms.

---

# 🛠️ Technology Stack

### Backend
- Python
- FastAPI
- SQLAlchemy
- Pydantic

### Database
- SQLite

### Deployment
- Docker
- Uvicorn

---

# 🚀 Future Architecture Roadmap

The following features are planned for future versions as this MVP evolves into a more advanced analytics platform.

---

## 📊 1. Advanced Machine Learning Prediction Pipeline

### Planned Improvements:

- Replace current rule-based churn analysis with trained Machine Learning models.
- Explore models such as:
  - XGBoost
  - LightGBM
  - Scikit-learn classifiers

- Introduce feature engineering and historical behavior analysis to improve prediction accuracy.

---

## 🛡️ 2. Authentication & Authorization Layer

### Planned Improvements:

- Implement JWT-based authentication.
- Add OAuth2 security workflows.
- Introduce Role-Based Access Control (RBAC).
- Separate permissions for administrators, engineers, and API consumers.

---

## 📈 3. Analytics Dashboard

### Planned Improvements:

- Build interactive analytics dashboards.
- Visualize:
  - User engagement trends
  - Churn patterns
  - Retention improvements

### Possible Technologies:
- Streamlit
- React Dashboard

---

# ⚙️ Local Development Setup

## 1. Clone Repository

```bash
git clone <repository-url>
```

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

## 3. Configure Environment Variables

Create a `.env` file:

```env
PORT=8000
DATABASE_URL=sqlite:///./churn_analytics.db
ENVIRONMENT=production
```

## 4. Run Application

```bash
uvicorn main:app --reload
```

Application will start at:

```
http://127.0.0.1:8000
```

Interactive API Documentation:

```
http://127.0.0.1:8000/docs
```

---

# 📌 Project Status

**Current Version:** 1.0.0  
**Stage:** Minimum Viable Product (MVP)

The current system focuses on reliable API architecture, database persistence, and rule-based churn analytics while maintaining a scalable foundation for future AI-driven improvements.

---

# 📄 License

This project is currently intended for learning, experimentation, and future development purposes.
