import pyttsx3
import tkinter as tk
from tkinter.simpledialog import askstring
from tkinter import messagebox

def speak_with_emotion(engine, text, emotion):
    emotions = {
        "happy": "I'm feeling ecstatic! " + text,
        "sad": "I'm feeling a bit down. " + text,
        "angry": "I'm quite angry right now! " + text,
        "surprised": "Wow, that's surprising! " + text,
        "whisper": "I'll tell you a secret: " + text.lower()
    }

    if emotion.lower() in emotions:
        engine.say(emotions[emotion.lower()])
    else:
        engine.say("I'm not sure how to express that emotion. " + text)

    engine.runAndWait()

def main():
    engine = pyttsx3.init()

    root = tk.Tk()
    root.title("Creative Text-to-Speech Converter")

    label = tk.Label(root, text="Welcome to the Creative Text-to-Speech Converter", font=("Helvetica", 18, "bold"))
    label.pack(pady=30)

    text = askstring("Input", "What would you like me to say:")
    emotion = askstring("Input", "How would you like me to say it (happy, sad, angry, surprised, whisper):")

    speak_with_emotion(engine, text, emotion)

    engine.stop()

    result_label = tk.Label(root, text="Speech complete. Have a great day!", font=("Helvetica", 14))
    result_label.pack(pady=20)

    ok_button = tk.Button(root, text="OK", command=root.destroy, width=10, font=("Helvetica", 14))
    ok_button.pack(pady=30)

    root.mainloop()

if __name__ == "__main__":
    main()
