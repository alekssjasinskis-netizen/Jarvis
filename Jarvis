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
            "hello jarvis"
        ],

        # Create a new task / note
        "create_task": [
            "jarvis task",
            "jarvis note"
        ],

        # Play random music from the musicPython folder
        "play_music": [
            "I simple",
            "jarvis awp"
        ],

        "open_browser": [
            "jarvis open browser",
            "open browser",
            "launch browser"
        ]
    }
}


# Speech recognition


def listen_command():
    """
    Listens to speech through the microphone and converts it into text.
    Returns the recognized command as a string.
    """

    try:
        with speech_recognition.Microphone(device_index=1) as mic:
            sr.adjust_for_ambient_noise(
                source=mic,
                duration=0.5
            )

            print("Speak...")
            audio = sr.listen(source=mic)

        query = sr.recognize_google(
            audio_data=audio,
            language="en-US"
        ).lower()

        print("Recognized:", repr(query))

        return query

    except speech_recognition.UnknownValueError:
        print("I didn't understand what you said")
        return ""

    except speech_recognition.RequestError as error:
        print("Google connection error:", error)
        return ""


# Command functions

def greeting():
    """
    Responds to the user's greeting.
    """
    return "Greetings, my lord"


def create_task():
    """
    Asks the user for the task
    and saves it to todo-list.txt.
    """

    print("What is the task, my lord?")

    task = listen_command()

    if not task:
        return

    with open("todo-list.txt", "a", encoding="utf-8") as f:
        f.write(f"{task}\n")

    print(f"Task added: {task}")


def open_browser():
    os.startfile(
        r"C:\Users\User\AppData\Local\Programs\Opera GX\opera.exe"
    )

    return "Opening Opera"


def play_music():
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


# Mapping commands to functions

functions = {
    "greeting": greeting,
    "create_task": create_task,
    "play_music": play_music,
    "open_browser": open_browser,
}


# Main function

def main():
    """
    Receives a voice command,
    determines its purpose
    and launches the corresponding function.
    """

    query = listen_command()

    for command_name, phrases in commands_dict["commands"].items():

        if query in phrases:

            result = functions[command_name]()

            if result:
                print(result)

            return

    print("I don't know such a command")


# Run the program

if __name__ == "__main__":
    main()
```
