# 🌦️ Weather Dashboard

A production-ready **3-Tier Weather Dashboard** built using **React, Flask, PostgreSQL, Docker, and GitHub Actions CI/CD**.

This project demonstrates modern Full Stack and DevOps practices, making it an excellent portfolio project for DevOps and Cloud Engineer roles.

---

# 📌 Features

- Search weather by city
- Display:
  - 🌍 City & Country
  - 🌡 Temperature
  - 💧 Humidity
  - 🌥 Weather Condition
  - 🌬 Wind Speed
  - 🌤 Weather Icon
- Store search history in PostgreSQL
- Responsive React UI
- Flask REST API
- Dockerized application
- Multi-stage Docker build
- GitHub Actions CI Pipeline

---

# 🏗 3-Tier Architecture

```
                User
                  │
                  ▼
        React Frontend (Nginx)
                  │
            HTTP REST API
                  │
                  ▼
           Flask Backend API
                  │
            PostgreSQL Database
```

---

# 📁 Project Structure

```
weather-dashboard/
│
├── frontend/
│   ├── package.json
│   ├── Dockerfile
│   ├── nginx.conf
│   ├── public/
│   │   └── index.html
│   └── src/
│       ├── index.js
│       ├── App.js
│       ├── api.js
│       └── App.css
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│
├── docker-compose.yml
├── .env.example
├── .gitignore
├── README.md
└── .github/
    └── workflows/
        └── ci.yml
```

---

# 🛠 Tech Stack

## Frontend

- React 18
- Axios
- CSS3

## Backend

- Python 3.12
- Flask
- Flask-CORS

## Database

- PostgreSQL 16

## DevOps

- Docker
- Docker Compose
- GitHub Actions
- Nginx

---

# ⚙️ Environment Variables

Copy

```bash
cp .env.example .env
```

Update your API key.

```
OPENWEATHER_API_KEY=YOUR_API_KEY

DB_HOST=postgres
DB_PORT=5432
DB_NAME=weather
DB_USER=postgres
DB_PASSWORD=password
```

---

# 🚀 Running the Project

Clone repository

```bash
git clone https://github.com/fahadkh14/weather-dashboard.git

```

Move into project

```bash
cd weather-dashboard
```

Create environment file

```bash
cp .env.example .env
```

Start containers

```bash
docker compose up --build
```

Run in background

```bash
docker compose up -d
```

Stop project

```bash
docker compose down
```

---

# 🌐 Application URLs

Frontend

```
http://localhost:3000
```

Backend

```
http://localhost:5000
```

Health Check

```
http://localhost:5000/health
```

Weather API

```
http://localhost:5000/weather?city=Delhi
```

Search History

```
http://localhost:5000/history
```

---

# 🐳 Docker Containers

Start

```bash
docker compose up --build
```

View running containers

```bash
docker ps
```

View logs

```bash
docker compose logs
```

Stop

```bash
docker compose down
```

Remove volumes

```bash
docker compose down -v
```

---

# 📦 Docker Images

Build frontend

```bash
docker build -t weather-frontend ./frontend
```

Build backend

```bash
docker build -t weather-backend ./backend
```

---

# 🔄 CI/CD Pipeline

GitHub Actions automatically performs:

- Checkout Repository
- Install Node Packages
- Build React Application
- Install Python Packages
- Verify Flask Code
- Build Docker Images
- Validate Docker Compose

Pipeline triggers on:

- Push
- Pull Request

---

# 📡 API Endpoints

## Health

```
GET /health
```

## Weather

```
GET /weather?city=Delhi
```

## History

```
GET /history
```

---

# 💾 Database

Database

```
PostgreSQL
```

Table

```
weather_history
```

Columns

- id
- city
- country
- temperature
- humidity
- weather
- searched_at

---

# 🔒 Security

- Environment Variables
- Docker Networking
- PostgreSQL Health Check
- CORS Enabled
- No Hardcoded API Keys

---

# 📈 Future Improvements

- Kubernetes Deployment
- Helm Charts
- Redis Cache
- JWT Authentication
- Prometheus Monitoring
- Grafana Dashboard
- HTTPS with Nginx
- GitHub Container Registry
- Terraform Deployment
- AWS EKS

---

# 👨‍💻 Author

Your Name

GitHub

```
https://github.com/yourusername
```

LinkedIn

```
https://linkedin.com/in/yourprofile
```

---

# ⭐ Support

If you found this project useful,

⭐ Star the repository on GitHub.

---

# 📜 License

This project is licensed under the MIT License.
