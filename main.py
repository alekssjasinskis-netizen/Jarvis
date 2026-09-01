```python
import os
import random
import speech_recognition
import webbrowser

# Settings

sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.8

# Commands

commands_dict = {
    "commands": {

        # Jarvis greeting
        "greeting": [
            "привет джарвис"
        ],

        # Create a new task / note
        "create_task": [
            "джарвис задача",
            "джарвис заметка"
        ],

        # Play random music from the musicPython folder
        "play_music": [
            "я simple",
            "джарвис awp"
        ],

        "open_browser": [
            "джарвис открой браузер",
            "открой браузер",
            "запусти браузер"
        ]
    }
}

# Speech recognition

def listen_command(mic):
    try:
        audio = sr.listen(source=mic)

        query = sr.recognize_google(
            audio_data=audio,
            language="ru-RU"
        ).lower()

        print("Recognized:", repr(query))

        return query

    except speech_recognition.UnknownValueError:
        return ""

    except speech_recognition.RequestError:
        return ""

# Command functions

def greeting(mic):
    """
    Responds to a greeting.
    """
    return "Hello, my lord"


def create_task(mic):
    """
    Asks the user for a task
    and saves it to todo-list.txt.
    """

    print("What is the task, my lord?")

    task = listen_command(mic)

    if not task:
        return

    with open("todo-list.txt", "a", encoding="utf-8") as f:
        f.write(f"{task}\n")

    print(f"Task added: {task}")


def open_browser(mic):
    os.startfile(
        r"C:\Users\User\AppData\Local\Programs\Opera GX\opera.exe"
    )

    return "Opening Opera"


def play_music(mic):
    """
    Selects a random music file
    from the musicPython folder and launches it.
    """

    files = os.listdir("musicPython")

    random_file = os.path.join(
        "musicPython",
        random.choice(files)
    )

    os.startfile(random_file)

    return f"Playing: {os.path.basename(random_file)}"


# Map commands to functions

functions = {
    "greeting": greeting,
    "create_task": create_task,
    "play_music": play_music,
    "open_browser": open_browser,
}


# Main function

def main():
    """
    Listens for voice commands,
    determines their purpose,
    and executes the corresponding function.
    """

    # Announces that Jarvis has started

    with speech_recognition.Microphone(device_index=1) as mic:
        print("Calibrating...")
        sr.adjust_for_ambient_noise(mic, duration=0.5)

        print("Jarvis started")

        # Keeps the program running
        # and continuously listens for commands

        while True:
            query = listen_command(mic)

            if not query:
                continue

            for command_name, phrases in commands_dict["commands"].items():
                if query in phrases:
                    result = functions[command_name](mic)

                    if result:
                        print(result)

                    break


# Run the program

if __name__ == "__main__":
    main()
```
