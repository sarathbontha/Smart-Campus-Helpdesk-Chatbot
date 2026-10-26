
"""
Smart Campus Helpdesk Chatbot
Hands-On Assignment 3

A terminal chatbot that answers common campus questions.
"""

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


def create_chatbot():
    """Create and train the campus helpdesk chatbot."""

    chatbot = ChatBot(
        "Campus Helpdesk Assistant",
        storage_adapter="chatterbot.storage.SQLStorageAdapter",
        database_uri="sqlite:///campus_chatbot.sqlite3",
        logic_adapters=[
            "chatterbot.logic.BestMatch"
        ]
    )

    trainer = ListTrainer(chatbot)

    # Sample campus-related questions and answers.
    # These are demonstration answers, not official university policies.
    campus_conversations = [
        ["Hello", "Hello! Welcome to the Campus Helpdesk."],
        ["What can you help me with?",
         "I can answer basic questions about campus services."],
        ["How can I contact my academic advisor?",
         "You can check your student portal for academic advising contact details."],
        ["Where can I find my class schedule?",
         "You can view your class schedule in your student portal."],
        ["How can I reset my student password?",
         "Please use the password reset option on your university login page."],
        ["How can I access the library?",
         "Check the university library website for access information and opening hours."],
        ["Where can I find campus events?",
         "You can check the university events calendar."],
        ["How do I contact technical support?",
         "Please contact your university IT helpdesk for technical support."],
        ["How can I check my grades?",
         "You can check your grades through the student portal."],
        ["Thank you", "You're welcome! Have a great day."],
        ["Goodbye", "Goodbye! All the best with your studies."]
    ]

    # Train the chatbot with each question-answer pair.
    for conversation in campus_conversations:
        trainer.train(conversation)

    return chatbot


def main():
    """Run the chatbot in the terminal."""

    chatbot = create_chatbot()

    print("===================================")
    print(" SMART CAMPUS HELPDESK CHATBOT")
    print("===================================")
    print("Ask questions about campus services.")
    print("Type 'exit' to end the conversation.")

    while True:
        user_input = input("\nStudent: ").strip()

        # Exit the chatbot when requested.
        if user_input.lower() in ["exit", "quit"]:
            print("Bot: Thank you for using Campus Helpdesk!")
            break

        # Prevent empty questions.
        if not user_input:
            print("Bot: Please enter your question.")
            continue

        try:
            # Generate a response using trained conversations.
            response = chatbot.get_response(user_input)
            print("Bot:", response)

        except Exception as error:
            print("Bot: Sorry, something went wrong.")
            print("Error details:", error)


if __name__ == "__main__":
    main()
