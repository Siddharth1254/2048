---
layout: default
title: "Play the Game"
parent: "2048"
nav_order: 2
---

# Play the Game
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Running Locally

### 1. Clone the repository

```bash
git clone https://github.com/Siddharth1254/2048.git
cd 2048/projects/2048-flask-game
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start the server

```bash
python application.py
```

### 4. Open the game

Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

## How to Play

- Use the **arrow keys** to slide tiles in any direction
- When two tiles with the **same number** touch, they merge (e.g., 2+2=4, 4+4=8)
- Reach the **2048** tile to win
- The game ends when no more moves are possible

![2048 gameplay](/img/example-2048.gif)

## Game Controls

| Key | Action |
|-----|--------|
| ↑ Arrow | Move tiles up |
| ↓ Arrow | Move tiles down |
| ← Arrow | Move tiles left |
| → Arrow | Move tiles right |
| New Game button | Reset the board |
