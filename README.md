# 🎮 Project 2048

A full-stack Python implementation of the classic **2048** sliding puzzle game, built with **Flask** and deployed on **AWS Elastic Beanstalk**.

![2048 Game Demo](img/example-2048.gif)

**▶️ Play Now:** [2048-game-env.eba-5ysiifwf.eu-north-1.elasticbeanstalk.com](http://2048-game-env.eba-5ysiifwf.eu-north-1.elasticbeanstalk.com/)

**📖 Documentation:** [siddharth1254.github.io/2048](https://siddharth1254.github.io/2048/)

**💬 Feedback:** [Played the game? Share your thoughts here](https://docs.google.com/forms/d/e/1FAIpQLSdb99fJnHfl-7gU2Qvk3_c_Ubpp6UxszaKgWYjAfGTyzR2ZKw/viewform?usp=publish-editor)

---

## 📍 About

This project was inspired by the [UC Berkeley CS 61B](https://sp25.datastructur.es/projects/proj0/) course. We extended the idea by building a web application with Python and deploying it to AWS — combining software engineering with cloud infrastructure skills.

**My role:** Full-stack development — game logic, Flask backend, frontend rendering, and AWS deployment.

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Python 3, Flask |
| Frontend | HTML, CSS, JavaScript |
| Deployment | AWS Elastic Beanstalk |
| Documentation | Jekyll, GitHub Pages |

---

## 📂 Repository Structure

```
├── projects/2048-flask-game/   # Flask app source code
│   ├── application.py          # Flask routes (entry point)
│   ├── game.py                 # Core game logic
│   ├── requirements.txt        # Python dependencies
│   ├── templates/index.html    # Game page
│   └── static/                 # CSS + JavaScript
├── docs/                       # Documentation pages (Jekyll)
│   ├── build.md                # Game logic walkthrough
│   ├── game.md                 # Play instructions
│   └── aws.md                  # AWS deployment guide
├── img/                        # Images and GIFs
├── _config.yml                 # Jekyll site configuration
├── index.md                    # Site homepage
├── landing.md                  # Project overview page
├── 2048.md                     # Documentation section parent
├── Gemfile                     # Ruby/Jekyll dependencies
└── .gitignore                  # Git ignore rules
```

---

## 💻 Run Locally (Optional)

If you prefer to run the game on your own machine instead of the live version:

```bash
git clone https://github.com/Siddharth1254/2048.git
cd 2048/projects/2048-flask-game
pip install -r requirements.txt
python application.py
# Open http://127.0.0.1:5000
```

---

## 📖 Documentation

Visit the [live documentation site](https://siddharth1254.github.io/2048/) for:

- [Project Overview](https://siddharth1254.github.io/2048/landing.html) — Motivation and architecture
- [Build the Game](https://siddharth1254.github.io/2048/docs/build.html) — Game logic walkthrough
- [Play the Game](https://siddharth1254.github.io/2048/docs/game.html) — How to play
- [Host on AWS](https://siddharth1254.github.io/2048/docs/aws.html) — Deployment guide

---

## 📄 License

See [LICENSE](LICENSE).
