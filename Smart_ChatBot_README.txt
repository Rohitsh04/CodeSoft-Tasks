Smart ChatBot

A simple voice- and text-enabled chatbot with a modern PyQt5 GUI.
This chatbot can:
- Respond to predefined queries
- Fetch brief Wikipedia summaries for unknown questions
- Take voice input using your microphone
- Reply with voice output using text-to-speech (TTS)

------------------------------------------------------------
Features
------------------------------------------------------------
- GUI-based — Built using PyQt5 with a clean dark theme.
- Text & Voice Input — Type or speak your queries.
- Voice Output — Bot replies are read aloud using pyttsx3.
- Wikipedia Integration — Automatically fetches short summaries for general knowledge queries.
- Rule-based Responses — Quick answers for common greetings and phrases.

------------------------------------------------------------
Requirements
------------------------------------------------------------
Install dependencies via pip:
    pip install PyQt5 wikipedia pyttsx3 SpeechRecognition

For voice input to work, you also need:
    pip install pyaudio
Note: On some systems, pyaudio installation may require additional setup.
      Windows users can install precompiled wheels from:
      https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio

------------------------------------------------------------
How to Run
------------------------------------------------------------
1. Save the script as chatbot_codsoft_01.py.
2. Run it using:
       python chatbot_codsoft_01.py
3. The chatbot window will open.
4. Type a message in the input box and press Send, or click the 🎙️ button to speak.
5. The chatbot will respond in text and voice.

------------------------------------------------------------
Project Structure
------------------------------------------------------------
chatbot_codsoft_01.py   # Main chatbot script with GUI, voice I/O, and Wikipedia integration

------------------------------------------------------------
How It Works
------------------------------------------------------------
1. Predefined Rules — Checks if the input contains a known phrase (e.g., "hello", "bye").
2. Wikipedia Fallback — If no match, fetches a short summary from Wikipedia.
3. Voice Output — Uses pyttsx3 to speak the reply aloud.
4. GUI Flow — Messages appear in a chat display, with delays for a natural feel.

------------------------------------------------------------
Example Usage
------------------------------------------------------------
You: Hello
Bot: Hi there! How can I assist you today?

You: Who is Albert Einstein?
Bot: Albert Einstein was a German-born theoretical physicist who developed the theory of relativity...
     (spoken aloud)

------------------------------------------------------------
Future Improvements
------------------------------------------------------------
- Add chatbot memory for contextual conversations
- Integrate with GPT-based AI models
- Improve Wikipedia search for better accuracy
- Add multi-language support

------------------------------------------------------------
License
------------------------------------------------------------
This project is open-source and free to use for learning and personal projects.
