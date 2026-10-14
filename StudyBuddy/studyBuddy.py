
import random

print("=" * 40)
print("       WELCOME TO STUDYBUDDY")
print("       Your Personal Study Assistant")
print("=" * 40)

topics = {
    "python": (
        "Python is a high-level programming language. "
        "It is easy to learn and is used in AI, web development, "
        "automation, and data science."
    ),
    "java": (
        "Java is an object-oriented programming language. "
        "It runs on the Java Virtual Machine (JVM) and is used "
        "to build web, desktop, and enterprise applications."
    ),
    "database": (
        "A database is an organized collection of data. "
        "DBMS software helps users store, retrieve, update, "
        "and manage data. Examples include MySQL and Oracle."
    ),
    "ai": (
        "Artificial Intelligence (AI) is a branch of computer "
        "science that enables machines to perform tasks such "
        "as learning, reasoning, and understanding language."
    ),
    "operating system": (
        "An Operating System (OS) manages computer hardware "
        "and software resources. Examples are Windows, Linux, "
        "and Android."
    ),
    "data structure": (
        "A data structure organizes data for efficient use. "
        "Examples include arrays, linked lists, stacks, queues, "
        "trees, and graphs."
    )
}

mcqs = [
    {
        "question": "Which language is commonly used for AI?",
        "options": ["A. Python", "B. HTML", "C. CSS", "D. SQL"],
        "answer": "A",
        "explanation": "Python has many AI and machine learning libraries."
    },
    {
        "question": "Which data structure follows LIFO?",
        "options": ["A. Queue", "B. Stack", "C. Graph", "D. Tree"],
        "answer": "B",
        "explanation": "LIFO means Last In, First Out. A stack follows this rule."
    },
    {
        "question": "Which of these is a DBMS?",
        "options": ["A. MySQL", "B. HTML", "C. CSS", "D. Python"],
        "answer": "A",
        "explanation": "MySQL is a relational database management system."
    }
]

study_tips = [
    "Study for 25 minutes and take a 5-minute break.",
    "Practice questions instead of only reading notes.",
    "Revise important topics before sleeping.",
    "Break large topics into small, manageable sections.",
    "Explain what you learned in your own words."
]


def show_help():
    print("\nYou can ask me to:")
    print("- Explain Python, Java, AI, DBMS, OS, or data structures")
    print("- Ask for study tips")
    print("- Take an MCQ quiz")
    print("- Show available topics")
    print("- Type 'exit' to quit")


def explain_topic(message):
    for topic, explanation in topics.items():
        if topic in message:
            print(f"\nStudyBuddy: {explanation}")
            return True
    return False


def take_quiz():
    question = random.choice(mcqs)

    print("\nStudyBuddy:", question["question"])
    for option in question["options"]:
        print(option)

    answer = input("Your answer (A/B/C/D): ").strip().upper()

    if answer == question["answer"]:
        print("Correct! Well done!")
    else:
        print("Not quite. Correct answer:", question["answer"])

    print("Explanation:", question["explanation"])


print("\nType 'help' to see what I can do.")

while True:
    user_message = input("\nYou: ").strip().lower()

    if user_message == "exit":
        print("StudyBuddy: Good luck with your studies. Goodbye!")
        break

    elif user_message == "help":
        show_help()

    elif "topic" in user_message and (
        "show" in user_message or "list" in user_message
    ):
        print("\nAvailable topics:")
        for topic in topics:
            print("-", topic.title())

    elif "quiz" in user_message or "mcq" in user_message:
        take_quiz()

    elif "tip" in user_message or "study plan" in user_message:
        print("\nStudyBuddy:", random.choice(study_tips))

    elif not user_message:
        print("StudyBuddy: Please type a question.")

    elif not explain_topic(user_message):
        print(
            "\nStudyBuddy: I don't know that topic yet. "
            "Try Python, Java, AI, database, operating system, "
            "or data structure. Type 'help' for options."
        )
