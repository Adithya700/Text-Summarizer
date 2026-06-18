# AI Text Summarizer using Gemini API

A simple AI-powered text summarization application built using Python and Google's Gemini API. The program accepts a piece of text and generates a concise summary while preserving the original meaning and removing unnecessary details.

---

## Features

* Generate summaries using Google's Gemini API
* Maintain the key ideas and meaning of the text
* Produce concise summaries under 100 words
* Secure API key management using environment variables
* Exception handling for API errors
* Simple and easy-to-understand implementation

---

## Technologies Used

* Python 3
* Google Gemini API
* python-dotenv
* Environment Variables (`.env`)

---

## Project Structure

```text
Text_Summarizer/
│
├── summarizer.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## How It Works

1. The user provides a piece of text.
2. A prompt is constructed with summarization instructions.
3. The Gemini API generates a concise summary.
4. The summarized text is returned to the user.

---

## Code Flow

```text
Input Text
     ↓
Create Prompt
     ↓
Send Request to Gemini API
     ↓
Generate Summary
     ↓
Return Summary
```

---

## Example

### Input

```text
Artificial Intelligence is a branch of computer science that enables machines to perform tasks that typically require human intelligence, such as learning, reasoning, problem-solving, and decision-making.
```

### Output

```text
Artificial Intelligence is a field of computer science that enables machines to perform tasks requiring human-like intelligence, including learning, reasoning, and decision-making.
```

---
<img width="1067" height="846" alt="Screenshot 2026-06-18 124751" src="https://github.com/user-attachments/assets/3b41498a-411c-4d78-961f-495814bc700b" />


## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/Text_Summarizer.git
cd Text_Summarizer
```

### Create a Virtual Environment

```bash
python -m venv .venv
```

### Activate the Virtual Environment

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install google-genai python-dotenv
```

---

## Environment Variables

Create a `.env` file in the project directory:

```text
GEMINI_API_KEY=your_gemini_api_key
```

The API key is loaded securely using:

```python
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
```

---

## Running the Program

```bash
python summarizer.py
```

---

## Learning Objectives

This project was developed to practice:

* Integrating external AI APIs
* Prompt engineering
* Secure API key management using environment variables
* Exception handling
* Building AI-powered Python applications
* Working with natural language processing tasks such as text summarization

---

## Author

**Adithya K.S.**

This project was created as a practice project to gain hands-on experience with Google's Gemini API and build a simple AI-powered text summarization application.
