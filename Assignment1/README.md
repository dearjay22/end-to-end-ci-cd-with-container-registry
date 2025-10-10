# Assignment 1 – End-to-End CI/CD with GitHub Actions and DockerHub  
**Student Name:** Jay Patel  
**Student ID:** 9062044  
**Reviewers:** @kakkarvarun, @aagamjhaveri(instructor)  

---

## 🧩 Project Overview
This project demonstrates a **complete CI/CD pipeline** using **GitHub Actions** for a simple **Python calculator application**.  
The pipeline covers every stage — build, test, containerization, security scan, and image publishing to DockerHub — while adhering to GitHub branching strategies and environment configurations.

It showcases DevOps principles such as **automation**, **environment segregation**, and **continuous feedback**, ensuring that tested, secure, and deployable images are always available.

---

## ⚙️ CI/CD Pipeline Overview

| Stage | Description | Tools Used |
|--------|--------------|-------------|
| **Build** | Installs dependencies and validates the source code. | GitHub Actions, Python |
| **Test** | Runs automated unit tests to verify logic correctness. | unittest |
| **Containerize** | Builds Docker image and tags it with commit SHA or `latest`. | Docker, GitHub Actions |
| **Security Scan** | Performs vulnerability scan using Trivy for HIGH/CRITICAL risks. | Trivy |
| **Publish** | Pushes the image to DockerHub (uses secrets for credentials). | DockerHub |
| **Environments** | Runs workflow based on branch → `develop` = dev, `release` = production. | GitHub Environments |

---

## 🐍 Application Details

**File:** `Calculator.py`  
A simple command-line calculator supporting:
- Addition  
- Subtraction  
- Multiplication  
- Division (with zero-division handling)

**Test File:** `Unit_Test/test_calculator.py`  
Verifies all core functions with `unittest`.

---

## 🧪 Unit Testing
All tests are executed automatically in the **Test stage**:
```bash
python -m unittest discover -s Unit_Test -p "test_*.py"
```
---

## 🌐 Registry Details
- **Registry:** [DockerHub – dearjay22](https://hub.docker.com/u/dearjay22)  
- **Repository:** `dearjay22/prog8860-calculator`  
- **Tag Format:** `${{ github.run_number }}` (Auto-increment per workflow run)

---

## 🧩 Run Container Locally

```bash
docker pull dearjay22/prog8860-calculator:<tag>
docker run -p 8080:8080 dearjay22/prog8860-calculator:<tag>
```