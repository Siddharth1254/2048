---
layout: default
title: "Project Overview"
nav_order: 2
---

# Project Overview
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Play the Game

The game is live and deployed on AWS Elastic Beanstalk:

**▶️ [Play 2048 Now!](http://2048-game-env.eba-5ysiifwf.eu-north-1.elasticbeanstalk.com/)**

Use the **arrow keys** to slide tiles. When two tiles with the same number collide, they merge!

---

## Motivation

This project was inspired by the UC Berkeley CS 61B course, where students implement the game 2048 to practice data structures and algorithms. We extended this idea by building a full-stack Python web application and deploying it on AWS, combining software development with cloud infrastructure skills.

## Goals

1. **Build** a fully playable 2048 game using Python and Flask
2. **Understand** the client-server architecture (frontend ↔ backend communication)
3. **Deploy** the application to AWS Elastic Beanstalk
4. **Document** the entire process as a learning resource

## How the Application Works

```
User presses arrow key
      ↓
JavaScript sends POST request to /move/<direction>
      ↓
Flask route calls game.move() with the direction
      ↓
Game logic updates the grid and score
      ↓
Flask returns new game state as JSON
      ↓
JavaScript updates the page with new tiles
```

## Project Structure

| Directory | Purpose |
|-----------|---------|
| `projects/2048-flask-game/` | Flask application source code |
| `docs/` | Documentation pages (this site) |
| `img/` | Images and animations |
