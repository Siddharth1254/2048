---
title: Home
layout: home
nav_order: 1
---

# 🎮 Project 2048

Welcome! This project is a **full-stack Python implementation** of the classic 2048 sliding puzzle game, built with Flask and deployed on AWS Elastic Beanstalk.

![2048 Game Demo]({{ '/img/example-2048.gif' | relative_url }}){: .game-preview }

---

## ▶️ Play Now

[🎮 Play 2048 Live!](http://2048-game-env.eba-5ysiifwf.eu-north-1.elasticbeanstalk.com/){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }
[View Source Code](https://github.com/Siddharth1254/2048/tree/main/projects/2048-flask-game){: .btn .fs-5 .mb-4 .mb-md-0 }

---

## 💬 Give Us Your Feedback

We'd love to hear what you think! Whether it's a bug, a suggestion, or just a ⭐ — your feedback helps us improve.

[📝 Played the game? Share your thoughts here](https://docs.google.com/forms/d/e/1FAIpQLSdb99fJnHfl-7gU2Qvk3_c_Ubpp6UxszaKgWYjAfGTyzR2ZKw/viewform?usp=publish-editor){: .btn .btn-purple .fs-5 .mb-4 .mb-md-0 }

---

## 📍 Explore the Project

| | Section | What's Inside |
|---|---------|---------------|
| 📖 | [Project Overview](landing.html) | Motivation, goals, and architecture |
| 🔨 | [Build the Game](docs/build.html) | Step-by-step guide to the game logic |
| ▶️ | [Play the Game](docs/game.html) | How to play and game controls |
| ☁️ | [Host on AWS](docs/aws.html) | Deploy to AWS Elastic Beanstalk |

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| **Backend** | Python 3 + Flask |
| **Frontend** | HTML, CSS, JavaScript |
| **Deployment** | AWS Elastic Beanstalk |
| **Documentation** | Jekyll + GitHub Pages |

---

## 💻 Run Locally (Optional)

If you'd like to run the game on your own machine:

```bash
git clone https://github.com/Siddharth1254/2048.git
cd 2048/projects/2048-flask-game
pip install -r requirements.txt
python application.py
```

Then open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.
