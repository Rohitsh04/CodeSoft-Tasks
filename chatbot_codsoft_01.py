import sys
import wikipedia
import pyttsx3
import speech_recognition as sr
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QTextBrowser, QLineEdit, QPushButton)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QIcon

# ========== Voice Output Engine ==========
engine = pyttsx3.init()
engine.setProperty('rate', 160)
engine.setProperty('volume', 1.0)

def speak_text(text):
    engine.say(text)
    engine.runAndWait()

# ========== Wikipedia Fetcher ==========
def get_wikipedia_summary(query):
    try:
        summary = wikipedia.summary(query, sentences=2)
        return summary
    except:
        return "I'm not sure about that. Please try rephrasing your question."

# ========== Voice Input ==========
def get_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        return text
    except:
        return "Sorry, I couldn't understand. Please type."

# ========== Chatbot Logic ==========
def get_bot_response(user_input):
    user_input = user_input.lower()

    rules = {
        "hello": "Hi there! How can I assist you today?",
        "how are you": "I'm just code, but I'm functioning well!",
        "your name": "I'm your smart chatbot!",
        "bye": "Goodbye! Have a great day!"
    }

    for key in rules:
        if key in user_input:
            return rules[key]

    summary = get_wikipedia_summary(user_input)
    return summary

# ========== Main GUI App ==========
class ChatBotUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Smart ChatBot")
        self.setGeometry(200, 200, 480, 600)
        self.setStyleSheet("background-color: #1e1e1e; color: white; border-radius: 20px;")

        layout = QVBoxLayout()

        # Chat history
        self.chat_display = QTextBrowser()
        self.chat_display.setStyleSheet("padding: 15px; font-size: 16px; border-radius: 10px;")
        layout.addWidget(self.chat_display)

        # Input + Buttons
        input_layout = QHBoxLayout()
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Type your message or press 🎤...")
        self.input_field.setStyleSheet("padding: 10px; font-size: 16px; border-radius: 10px;")
        input_layout.addWidget(self.input_field)

        self.send_btn = QPushButton("Send")
        self.send_btn.clicked.connect(self.send_message)
        input_layout.addWidget(self.send_btn)

        self.mic_btn = QPushButton("🎙️")
        self.mic_btn.clicked.connect(self.mic_input)
        input_layout.addWidget(self.mic_btn)

        layout.addLayout(input_layout)
        self.setLayout(layout)

    def send_message(self):
        user_text = self.input_field.text()
        if user_text:
            self.chat_display.append(f"<p style='color: lightgreen'><b>You:</b> {user_text}</p>")
            self.input_field.clear()
            QTimer.singleShot(600, lambda: self.bot_reply(user_text))

    def mic_input(self):
        user_text = get_voice_input()
        self.chat_display.append(f"<p style='color: lightgreen'><b>You:</b> {user_text}</p>")
        QTimer.singleShot(600, lambda: self.bot_reply(user_text))

    def bot_reply(self, user_text):
        response = get_bot_response(user_text)
        self.chat_display.append(f"<p style='color: lightblue'><b>Bot:</b> {response}</p>")
        speak_text(response)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    bot_window = ChatBotUI()
    bot_window.show()
    sys.exit(app.exec_())
