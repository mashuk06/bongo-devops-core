# 🚀 GIT & GITHUB MASTERY - 10 MISSION-CRITICAL TASKS
**DevOps & Cloud Engineering Assignment** | *bongoDev*

Welcome to the **Git & GitHub Mastery** repository! This project documents the complete execution of 10 hands-on DevOps missions designed to build deep expertise in version control, branching strategies, commit hygiene, conflict resolution, and reflog recovery.

## 🎯 Overview & Mission Rules

> **Mentor Note:** In the real world, DevOps Engineers use Git to manage system performance and optimization. Every commit needs an explicit purpose and clean history.

* **Work in your own repository**
* **Commit clearly and frequently**
* **Verify with Git commands**
* **Push final history to GitHub**

---

## 🔷 Phase 1: The Foundations - Basic

### Task 01: The "First Impression"
**Goal:** Set up identity, initialize repository, and create initial setup commit.

```bash
# Set global identity
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Initialize repository
git init bongodev-repository
cd bongodev-repository

# Create initial README and commit
echo "# Git & GitHub Mastery - bongoDev" > README.md
git add README.md
git commit -m "chore: initial repository setup"

```

### Task 02: The "Safe Space"
Goal: Protect secrets and sensitive files using .gitignore.

```bash
# Create fake secret file
echo "DB_PASSWORD=SuperSecretPass123!" > .env

# Configure .gitignore
echo ".env" > .gitignore

# Verify git status ignores .env
git status
```


### Task 03: The "Parallel Universe"
Goal: Work on experimental features in an isolated branch without affecting main.


```bash
# Create and switch to feature branch
git checkout -b feature/system-optimization

# Add feature file
echo "Benchmarking latency and CPU utilization..." > kernel_tuning.txt
git add kernel_tuning.txt
git commit -m "feat: add kernel tuning documentation"

# Switch back to main (notice kernel_tuning.txt disappears from main workspace)
git checkout main

```bash

### Task 04: The "Selective Memory"
Goal: Stage and commit separate concerns into distinct, granular commits.

```bash

# Create two independent files
echo "UI/API configuration" > web_config.conf
echo "Database optimization settings" > db_config.conf

# Stage and commit web configuration
git add web_config.conf
git commit -m "feat(config): add web server configurations"

# Stage and commit database configuration separately
git add db_config.conf
git commit -m "feat(db): add database indexing and connection parameters"

```bash

### Task 05: The "Cloud Connection"
Goal: Connect local repository to GitHub remote and push main.

# Add GitHub remote repository link
git remote add origin [https://github.com/your-username/bongo-devops-core.git](https://github.com/your-username/bongo-devops-core.git)

# Set main branch and push
git branch -M main
git push -u origin main

```bash

##🔶 Phase 2: The Engineer's Workflow - Intermediate

### Task 06: The "History Detective"
Goal: Locate bug-introducing commits using git log and git blame.

```bash

# Search commit history or file line-by-line history
git log -p -S "port"
git blame <filename>

# Result: Identified Commit Hash, Author, and original Port configuration change!

```bash

### Task 07: The "Safety Net"
Goal: Handle context switching and hotfix requests using git stash.

```bash

# Work on feature branch
git checkout feature/system-optimization
echo "print('Optimizing algorithm...')" >> feature.py

# Hotfix arrives! Stash uncommitted changes
git stash save "WIP: system optimization logic"

# Switch to main and apply fix
git checkout main
echo "BUG_FIX=TRUE" > bugfix.py
git add bugfix.py
git commit -m "fix: resolve critical production bug in main"

# Return to feature branch and restore stashed work
git checkout feature/system-optimization
git stash pop


```bash

### Task 08: The "Clean Merge"
Goal: Keep commit history clean by squashing feature branch commits before merging.

```bash

# Make small commits on feature branch
git checkout feature/system-optimization
echo "step 1" >> optimization.txt && git commit -am "wip: step 1"
echo "step 2" >> optimization.txt && git commit -am "wip: step 2"
echo "step 3" >> optimization.txt && git commit -am "wip: step 3"

# Merge into main using squash
git checkout main
git merge --squash feature/system-optimization
git commit -m "feat: complete system performance optimization"

```bash

### Task 09: The "Conflict Resolution"
Goal: Intentionally generate and resolve a merge conflict.

```bash

# Modify line 1 of optimization.txt on main
git checkout main
echo "Server Config: Production Mode" > optimization.txt
git commit -am "conf: set production mode in main"

# Modify line 1 of optimization.txt on feature branch differently
git checkout feature/system-optimization
echo "Server Config: High Performance Tuning" > optimization.txt
git commit -am "conf: set high performance tuning in feature"

# Attempt merge to trigger conflict
git checkout main
git merge feature/system-optimization

# Resolve conflict manually by editing optimization.txt (removing <<<, ===, >>> markers)
# Save file, then finalize merge:
git add optimization.txt
git commit -m "fix(merge): resolve configuration conflict between main and feature"

```bash

### Task 10: The "Time Machine"
Goal: Recover lost work/commits after an accidental hard reset using git reflog.

```bash

# Perform hard reset (simulating loss)
git reset --hard HEAD~1

# Check reflog to find pre-reset commit hash
git reflog

# Restore repository state to exact commit hash before deletion
git reset --hard <commit-hash>

```bash
