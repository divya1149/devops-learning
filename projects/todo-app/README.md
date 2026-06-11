&#x20;To-Do App with Flask + MySQL + Nginx 🐳



What is this project?

A To-Do web app built with Python Flask, connected to a 

MySQL database, with Nginx as a reverse proxy.

All 3 services run together using Docker Compose.



Project Architecture

Browser → Nginx (port 80) → Flask App (port 5000) → MySQL (port 3306)



&#x20;What I learned

\- How Nginx works as a reverse proxy

\- How to run 3 containers together with Docker Compose

\- How to connect Flask app to MySQL database

\- How Docker networking works between containers

\- How Docker volumes save data permanently



&#x20;Technologies Used

\- Python

\- Flask

\- MySQL

\- Nginx

\- Docker

\- Docker Compose



&#x20;Project Structure

todo-app/

├── app.py

├── Dockerfile

├── docker-compose.yml

├── requirements.txt

└── nginx/

&#x20;   └── nginx.conf



&#x20;How to run this project



Step 1 - Clone the repo

git clone git@github.com:divya1149/devops-learning.git



Step 2 - Go to project folder

cd devops-learning/projects/todo-app



Step 3 - Start all containers

docker compose up --build



Step 4 - Open in browser

http://localhost



&#x20;API Endpoints

| Endpoint | Method | Description |

|----------|--------|-------------|

| / | GET | Check if app is running |

| /todos | GET | Get all todos |

| /todos | POST | Add a new todo |



&#x20;Date

11 June 2026

