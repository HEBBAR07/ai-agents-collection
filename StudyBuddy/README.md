# StudyBuddy

StudyBuddy is a simple command-line study assistant that helps students learn core computer science concepts, revise key topics, and test themselves with quick multiple-choice questions.

## Features

- Explains topics such as Python, Java, databases, AI, operating systems, and data structures
- Shows a list of available study topics
- Gives random study tips
- Runs a multiple-choice quiz
- Provides the correct answer and explanation after each question
- Keeps the interaction simple and beginner-friendly

## Supported Topics

- Python
- Java
- Database
- AI
- Operating System
- Data Structure

## How to Run

1. Open a terminal in the StudyBuddy folder.
2. Run the script:

   ```bash
   python studyBuddy.py
   ```

3. Use commands such as:
   - `help` to see available actions
   - `quiz` or `mcq` to start a quiz
   - `tip` or `study plan` for a study suggestion
   - `exit` to quit the chatbot

## Example Interaction

```text
You: help
StudyBuddy: You can ask me to explain Python, Java, AI, DBMS, OS, or data structures.

You: quiz
StudyBuddy: Which language is commonly used for AI?
A. Python
B. HTML
C. CSS
D. SQL
Your answer (A/B/C/D): A
Correct! Well done!
```

## Technologies Used

- Python 3
- Standard Python library only

## Notes

This project is rule-based and uses predefined content rather than an AI model or external API.