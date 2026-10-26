# Smart Campus Helpdesk Chatbot

## Hands-On Assignment 3 – Python Q&A Chatbot

### Project Overview

The Smart Campus Helpdesk Chatbot is a simple terminal-based application developed using Python, Django, and ChatterBot.

The main purpose of this project is to help students find basic information about campus services. Students can ask questions about class schedules, academic advising, library facilities, technical support, and other university-related activities.

The chatbot uses sample conversations for training and provides responses based on the questions entered by the user.

### Technologies Used

| Technology | Version | Purpose |
|---|---|---|
| Python | 3.12.3 | Main programming language |
| Django | 4.2.30 | Project setup and configuration |
| ChatterBot | 1.2.8 | Chatbot development and training |
| spaCy | 3.8.16 | Natural language processing |
| SQLite | Built-in | Conversation data storage |
| VS Code | Installed version | Code development and testing |

### Project Features

- Answers basic campus-related questions.
- Provides information about academic services.
- Responds to questions about class schedules and student portals.
- Uses ChatterBot's ListTrainer for training.
- Supports continuous conversations through the terminal.
- Handles empty user input.
- Allows users to end the conversation by entering `exit`.

### Project Structure

```text
Smart_Campus_Chatbot/
│
├── campus_chatbot/
│   └── campus_chatbot.py
│
├── campus_project/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
├── README.md
└── .gitignore
```

### Installation and Setup

**Step 1: Clone the GitHub repository**

```bash
git clone https://github.com/YOUR_USERNAME/Smart-Campus-Helpdesk-Chatbot.git
cd Smart-Campus-Helpdesk-Chatbot
```

**Step 2: Create a virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Step 3: Install the required libraries**

```bash
python -m pip install -r requirements.txt
```

**Step 4: Install the spaCy English language model**

```bash
python -m spacy download en_core_web_sm
```

**Step 5: Apply Django database migrations**

```bash
python manage.py migrate
```

**Step 6: Run the chatbot**

```bash
python campus_chatbot/campus_chatbot.py
```

### How the Chatbot Works

The application starts by creating a chatbot using the ChatterBot library.

I used ListTrainer to train the chatbot with sample questions and answers related to campus services.

When a student enters a question, the chatbot processes the input and selects a suitable response from the trained conversations.

The conversation continues until the user enters `exit`.

### Sample Conversation

The following is an example of the expected chatbot interaction:

```text
SMART CAMPUS HELPDESK CHATBOT

Ask questions about campus services.
Type 'exit' to end the conversation.

Student: Hello
Bot: Hello! Welcome to the Campus Helpdesk.

Student: Where can I find my class schedule?
Bot: You can view your class schedule in your student portal.

Student: How can I contact my academic advisor?
Bot: You can check your student portal for academic advising contact details.

Student: Thank you
Bot: You're welcome! Have a great day.

Student: exit
Bot: Thank you for using Campus Helpdesk!
```

Actual chatbot responses may vary depending on the training data.

### Testing

The application can be tested through the VS Code terminal using the following scenarios:

- Greeting questions
- Academic advising questions
- Student portal and class schedule questions
- Campus services questions
- Empty user input
- Exit command

### Challenges and Learning

During this project, I learned how to configure a Python environment and work with Django and ChatterBot.

I also understood the importance of training conversations and how they help a chatbot provide suitable responses.

This project provided practical experience with Python programming, natural language processing, and terminal-based applications.

### Future Improvements

In the future, the chatbot can be improved by adding more campus-related questions, connecting it to updated university information, and developing a web interface.

### Conclusion

The Smart Campus Helpdesk Chatbot demonstrates how Python and ChatterBot can be used to create a simple conversational application.

This project helped me understand the basic process of chatbot development, including training, user input processing, and response generation.

### Author

**Student Name:** Sarath Bontha

**Assignment:** Hands-On Assignment 3

**Project:** Smart Campus Helpdesk Chatbot Using Python