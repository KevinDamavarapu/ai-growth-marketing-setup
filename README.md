# AI Tools Setup & Workflow Documentation

## Objective

The goal of this project is to set up and explore an AI-assisted development environment using Cursor IDE, Claude Code, and Codex, while documenting the setup process, challenges faced, and key observations.

---

## Tools Used

- Cursor IDE
- Claude Code (Anthropic)
- Codex (OpenAI)
- GitHub

---

## Setup Process

### 1. Installing Cursor IDE

- Downloaded Cursor from the official website
- Installed and launched the application
- Logged in using GitHub

**Observation:**
The installation was straightforward, but it was not immediately clear that the downloaded application itself functions as the IDE, as there is no explicit confirmation step.

---

### 2. Authentication Issue During Login

While connecting GitHub to Cursor, a verification code was sent via email.

**Issue:**
Initially accessed the verification code from a mobile device and entered it into the app. This resulted in an error stating that verification must be completed from the same browser session.

**Solution:**
Retried the process and accessed the email from the same browser session on the laptop. This resolved the issue and GitHub was successfully connected.

**Insight:**
Cursor enforces session-based authentication, requiring the verification flow to remain within the same environment.

---

### 3. Opening the Repository in Cursor

- Created a GitHub repository: `ai-growth-marketing-setup`
- Attempted to open it directly in Cursor but found no direct option

**Issue:**
Cursor does not provide a direct way to open repositories from a GitHub URL.

**Solution:**
Cloned the repository locally using GitHub Desktop and then opened the folder in Cursor.

**Insight:**
Cursor operates on local file systems, requiring an understanding of Git workflows (clone → open locally).

---

### 4. Creating Initial Project Structure

- Opened the repository in Cursor
- Observed that the repository appeared empty
- Created a `README.md` file manually

**Insight:**
An empty repository can feel confusing in the IDE since no files are visible initially, even though the repo is correctly loaded.

---

### 5. Installing Claude Code Extension

- Opened Extensions panel in Cursor
- Searched for "Claude Code"

**Issue:**
Multiple similarly named extensions appeared, creating ambiguity

**Solution:**
Selected the official extension published by Anthropic

**Observation:**
The extension installed successfully without requiring explicit login or onboarding steps

---

### 6. Testing Claude Code Functionality

- Used the AI agent panel to query the project

**Observation:**
The AI attempted to inspect the repository by executing commands such as:
- `ls`
- `git status`

These required manual approval before execution.

**Insight:**
Cursor uses a controlled execution model where AI actions require user permission, ensuring transparency and security.

---

### 7. Installing Codex Extension

- Searched for "Codex" in Extensions

**Issue:**
Multiple results appeared, including unrelated or deprecated tools

**Solution:**
Selected the official "Codex – OpenAI’s coding agent" extension

**Observation:**
The extension installed without requiring additional authentication

---

## Key Learnings

- AI-assisted development tools require active human oversight and verification
- Tool selection requires careful validation of sources (official vs third-party extensions)
- Cursor integrates AI as an agent capable of interacting with the file system and executing commands
- Understanding Git workflows is essential for working with modern development tools
- Many tools assume prior knowledge, making initial onboarding less intuitive for new users

---

## Conclusion

This setup process demonstrated how modern AI-native development environments function, particularly how tools like Cursor integrate AI agents into coding workflows. The experience highlighted the importance of independent problem-solving, careful observation, and adaptability when working with new and evolving tools.