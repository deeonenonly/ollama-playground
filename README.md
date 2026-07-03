# 🧠 Local LLM Playground

A lightweight Python application that interacts with a locally running Large Language Model (LLM) using **Ollama**.

This project was built to explore how local AI models can be integrated into Python applications without relying on cloud APIs. It serves as my first hands-on project with local LLMs and focuses on understanding inference, prompt handling, and application structure.

---

## ✨ Features

- 💬 Chat with a locally hosted LLM
- ⚡ Measure response generation time
- 📊 Display response statistics (words & characters)
- 🖥️ Clean terminal interface
- 🔒 Runs completely offline

---

## 🛠️ Tech Stack

- Python 3
- Ollama
- Qwen 3 4B
- VS Code
- Git & GitHub

---

## 📂 Project Structure

```
ollama-playground/
│
├── assets/
├── app.py
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

---

## 🚀 Getting Started

### 1. Install Ollama

Download and install Ollama from https://ollama.com

### 2. Pull the model

```bash
ollama run qwen3:4b
```

### 3. Clone this repository

```bash
git clone https://github.com/deeonenonly/ollama-playground.git
cd ollama-playground
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
python app.py
```

---

## 📷 Demo

*(screenshot to be added.)*

Example output:

```
==========================================
      Local LLM Playground v1.2
==========================================
Model  : qwen3:4b
Status : Ready
Type 'exit' to quit.
==========================================

User: explain hash maps in one line.

AI:
A hash map is a data structure that stores key-value pairs using a hash function to compute the index of each key in an array for fast lookups, insertions, and deletions.
------------------------------------------


Time taken    : 53.67 seconds
Words generated : 31
Characters      : 170

==========================================
```

---

## 📚 What I Learned

Through this project I learned:

- Setting up Ollama on Windows
- Running local open-source LLMs
- Building Python applications around AI models
- Measuring inference performance
- Basic prompt handling
- Git and GitHub workflow
- Organizing Python projects for maintainability

---

## 🔮 Planned Improvements

- Continuous chat mode
- Conversation history
- Streaming responses
- Model selection
- PDF question answering
- Retrieval-Augmented Generation (RAG)
- Streamlit web interface

---

## 🎯 Why I Built This

As I prepare for software engineering and AI-focused placements, I'm building a collection of small but complete projects to strengthen my understanding of modern AI development tools.

This repository is part of that learning journey.

---

## 📄 License

This project is licensed under the MIT License.

---

## 📈 Version History

### v1.2
- Improved terminal interface
- Added response statistics
- Introduced project constants
- Refactored code into functions

### v1.1
- Initial local LLM chat application