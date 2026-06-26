# Ollama Playground

A simple Python application that connects to a locally running Large Language Model (LLM) using Ollama.

## Features

* Connects to a local Qwen 4B model
* Accepts user input from the terminal
* Sends prompts to the LLM
* Displays generated responses
* Measures response generation time

## Technologies Used

* Python
* Ollama
* Qwen 3 4B
* VS Code

## What I Learned

* Setting up Ollama locally
* Running open-source LLMs on personal hardware
* Creating Python applications that interact with AI models
* Measuring inference latency
* Understanding CPU/GPU model offloading

## Example

Question:
Explain hash maps in 3 sentences.

Response:
A hash map is a data structure that stores key-value pairs using a hash function to compute storage locations efficiently...

Response Time:
7.04 seconds

## Future Improvements

* Multi-turn chat support
* Conversation history
* PDF summarization
* Document question answering
* GUI using Streamlit

## How to Run

1. Install Ollama
2. Pull the model
   
   ollama run qwen3:4b

3. Install dependencies
   
   pip install ollama

4. Run the application
   
   python app.py
