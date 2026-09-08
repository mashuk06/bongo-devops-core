# 🚀 GIT & GITHUB MASTERY - 10 MISSION-CRITICAL TASKS
**DevOps & Cloud Engineering Assignment** | *bongoDev*

Welcome to the **Git & GitHub Mastery** repository! This project documents the complete execution of 10 hands-on DevOps missions designed to build deep expertise in version control, branching strategies, commit hygiene, conflict resolution, and reflog recovery.

---

## 📌 Table of Contents
1. [Overview & Mission Rules](#-overview--mission-rules)
2. [Phase 1: The Foundations (Basic)](#-phase-1-the-foundations---basic)
   - [Task 01: The "First Impression" (Identity & Setup)](#task-01-the-first-impression-identity--setup)
   - [Task 02: The "Safe Space" (.gitignore)](#task-02-the-safe-space-gitignore)
   - [Task 03: The "Parallel Universe" (Branching)](#task-03-the-parallel-universe-branching)
   - [Task 04: The "Selective Memory" (Staging)](#task-04-the-selective-memory-staging)
   - [Task 05: The "Cloud Connection" (GitHub Remote)](#task-05-the-cloud-connection-github-remote)
3. [Phase 2: The Engineer's Workflow (Intermediate)](#-phase-2-the-engineers-workflow---intermediate)
   - [Task 06: The "History Detective" (Investigation)](#task-06-the-history-detective-investigation)
   - [Task 07: The "Safety Net" (Context Switching)](#task-07-the-safety-net-context-switching)
   - [Task 08: The "Clean Merge" (Squash Workflow)](#task-08-the-clean-merge-squash-workflow)
   - [Task 09: The "Conflict Resolution" (Communication)](#task-09-the-conflict-resolution-communication)
   - [Task 10: The "Time Machine" (Reflog Recovery)](#task-10-the-time-machine-reflog-recovery)
4. [Verification & Summary](#-verification--summary)

---

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
