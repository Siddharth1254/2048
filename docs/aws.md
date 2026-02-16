---
layout: default
title: "Host on AWS"
parent: "2048"
nav_order: 3
---

# Host on AWS
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Overview

This guide walks you through deploying the 2048 Flask game to AWS Elastic Beanstalk (EB). Elastic Beanstalk handles provisioning, load balancing, and scaling automatically — you just upload your code.

## Prerequisites

- An [AWS account](https://aws.amazon.com/)
- AWS CLI installed and configured (`aws configure`)
- EB CLI installed (`pip install awsebcli`)

## Deployment Steps

### 1. Navigate to the Flask project

```bash
cd projects/2048-flask-game
```

### 2. Initialize Elastic Beanstalk

```bash
eb init
```

When prompted:
- Choose your **region**
- Create a new application (e.g., `2048-game`)
- Select **Python** as the platform (Python 3.11 or later)
- Say **No** to CodeCommit if asked

### 3. Create an environment and deploy

```bash
eb create 2048-game-env
```

This automatically:
- Provisions an EC2 instance
- Installs dependencies from `requirements.txt`
- Starts the Flask app via `application.py`

Deployment takes a few minutes. You'll see progress in your terminal.

### 4. Open your live app

```bash
eb open
```

This opens the deployed game in your default browser.

## Updating After Changes

After making code changes, deploy the update with:

```bash
eb deploy
```

## Monitoring

Check your environment's health and logs:

```bash
eb status
eb logs
```

## Cleaning Up

To avoid ongoing AWS charges, terminate the environment when you're done:

```bash
eb terminate 2048-game-env
```

## Why Elastic Beanstalk?

| Feature | Benefit |
|---------|---------|
| Managed infrastructure | No need to configure servers manually |
| Auto-scaling | Handles traffic spikes automatically |
| Easy deployment | Single command (`eb deploy`) to update |
| Beginner-friendly | Great introduction to AWS services |
