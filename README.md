---
title: Focus Env
emoji: 🧠
colorFrom: blue
colorTo: purple
sdk: docker
app_file: app.py
pinned: false
---

# Focus Management OpenEnv

## Description
This environment simulates student focus, energy, and distraction handling.

## Actions
- STUDY
- SCROLL
- BREAK
- IGNORE

## Observations
- focus
- energy
- tasks_left
- distraction

## Tasks
- Easy: 2 tasks
- Medium: 3 tasks
- Hard: 4 tasks

## Run
```bash
docker build -t focus-env .
docker run focus-env
