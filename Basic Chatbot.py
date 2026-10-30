
# CodeAlpha Python Programming Internship
# Task 4: Basic Chatbot

def chatbot():
    print("=" * 45)
    print("          WELCOME TO PYTHON CHATBOT")
    print("=" * 45)

    student_name = input("Enter student name: ").strip()

    if not student_name:
        student_name = "Student"

    print(f"\nHello, {student_name}!")
    print("I am a simple Python chatbot.")
    print("You can say hello, ask how I am, or say bye.")
    print("Type 'help' to see commands.\n")

    while True:
        user_message = input("You: ").strip().lower()

        if user_message in ["hello", "hi", "hey"]:
            print("Bot: Hi! Nice to meet you.")

        elif user_message in ["how are you", "how are you?"]:
            print("Bot: I'm fine, thanks! How can I help you?")

        elif user_message in ["your name", "what is your name",
                              "what is your name?"]:
            print("Bot: I am Python Chatbot.")

        elif user_message == "help":
            print("\nBot: Available commands:")
            print("- hello")
            print("- how are you")
            print("- your name")
            print("- help")
            print("- bye\n")

        elif user_message in ["thank you", "thanks"]:
            print("Bot: You're welcome!")

        elif user_message in ["bye", "exit", "quit"]:
            print(f"Bot: Goodbye, {student_name}! Have a nice day.")
            break

        elif user_message == "":
            print("Bot: Please type a message.")

        else:
            print("Bot: Sorry, I don't understand that message.")
            print("Bot: Type 'help' to see available commands.")


if __name__ == "__main__":
    chatbot()
