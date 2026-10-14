#!/usr/bin/env python3
# Simple College Library Chatbot
# Copilot: Add an "available" field to each book.
# Mark three books as available and two as borrowed
books = [
    {"title": "Harry Potter and the Philosopher's Stone", "author": "J. K. Rowling", "available": True},
    {"title": "The Hobbit", "author": "J. R. R. Tolkien", "available": True},
    {"title": "The Diary of a Young Girl", "author": "Anne Frank", "available": True},
    {"title": "Charlotte's Web", "author": "E. B. White", "available": False},
    {"title": "The Little Prince", "author": "Antoine de Saint-Exupéry","available": False}
]
# Copilot: Update the chatbot so it tells the user whether
# a book is available, borrowed, or not in the library.
# Only use information from the books list.

def find_book_by_query(query: str):
    q = query.lower()
    for book in books:
        if book["title"].lower() in q:
            return book
    return None


def main():
    print("Welcome to the School Library Chatbot!")
    print("Ask about a book, or type 'exit' to stop.")

    while True:
        try:
            question = input("\nYou: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nChatbot: Goodbye!")
            break

        if question.lower() == "exit":
            print("Chatbot: Goodbye!")
            break

        found_book = find_book_by_query(question)

        if found_book:
            if found_book.get("available"):
                print(f"Chatbot: Yes, '{found_book['title']}' is available.")
            else:
                print(f"Chatbot: '{found_book['title']}' is currently borrowed.")
        else:
            print("Chatbot: That book is not available in our library.")


if __name__ == "__main__":
    main()
