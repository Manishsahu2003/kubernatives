# 🚀 Flask App Deployment with CI/CD using Jenkins, Docker, and Kubernetes

This project demonstrates how to build, containerize, and deploy a simple Python Flask application using a CI/CD pipeline powered by *GitHub, **Jenkins, **Docker, and **Kubernetes*.

---

## 📌 Project Workflow

1. ✅ *Developed a Flask-based Python Application*
2. 📄 *Created a Dockerfile* to containerize the application
3. ⬆ *Pushed source code to GitHub*
4. 🔄 *Jenkins* automates:
   - Cloning code from GitHub
   - Building the Docker image
   - Pushing the image to *Docker Hub*
5. ☸ *Kubernetes* handles:
   - Pulling the Docker image from Docker Hub
   - Creating *Pods* and *Deployments*
   - Exposing the app on *Port 5000*
   - Scaling the app using *replicas*

---

## 🔧 Tech Stack Used

- 🐍 Python (Flask)
- 🐳 Docker
- 🧪 Jenkins
- 🗂 GitHub
- ☸ Kubernetes (kubectl & deployment YAML)
- 🐙 Docker Hub

---

## 🗂 Project Structure

```bash
.
├── app.py                 # Flask application file
├── Dockerfile             # For building Docker image
├── jenkinsfile            # CI/CD pipeline (optional if scripted)
├── deployment.yaml        # Kubernetes deployment config
└── README.md              # Project documentation
