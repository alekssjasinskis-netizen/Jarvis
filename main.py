import os
import random
import speech_recognition
import pygame
import webbrowser

pygame.mixer.init()

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
            "play music",
            "jarvis play music"
        ],

        # Open browser
        "open_browser": [
            "jarvis open browser",
            "open browser",
            "launch browser"
        ],

        # Shut down Jarvis
        "shutdown": [
            "jarvis shut down",
            "jarvis stop",
            "jarvis go offline"
        ]
    }
}


# Speech recognition

def listen_command(mic):
    try:
        audio = sr.listen(source=mic)

        query = sr.recognize_google(
            audio_data=audio,
            language="en-US"
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
    Responds to the user's greeting.
    """
    return "Hello, my lord."


def create_task(mic):
    """
    Asks the user for the task text
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

    return "Opening Opera."


def play_music(mic):
    """
    Selects a random music file
    from the musicPython folder and launches it.
    """

    files = os.listdir("musicPython")

    print("Files:", files)

    random_file = os.path.join(
        "musicPython",
        random.choice(files)
    )

    print("Selected file:", random_file)

    os.startfile(random_file)

    return f"Playing: {os.path.basename(random_file)}"


def play_sound(filename):
    file = os.path.join("JarvisSounds", filename)

    if not os.path.exists(file):
        print(f"Sound file not found: {file}")
        return

    pygame.mixer.music.load(file)
    pygame.mixer.music.play()


# Connect commands to functions

functions = {
    "greeting": greeting,
    "create_task": create_task,
    "play_music": play_music,
    "open_browser": open_browser,
    "shutdown": None,
}


# Main function

def main():
    """
    Receives a voice command,
    determines its purpose,
    and runs the corresponding function.
    """

    # Announces that Jarvis is starting

    with speech_recognition.Microphone(device_index=1) as mic:
        print("Calibrating...")

        sr.adjust_for_ambient_noise(mic, duration=0.5)

        print("Jarvis started.")

        play_sound("loadingEnd.mp3")

        # Keep the program running
        # and listen continuously

        while True:
            query = listen_command(mic)

            if query in commands_dict["commands"]["shutdown"]:
                print("Jarvis shutting down.")
                break

            if not query:
                continue

            for command_name, phrases in commands_dict["commands"].items():

                if query in phrases:

                    if command_name == "shutdown":
                        break

                    result = functions[command_name](mic)

                    if result:
                        print(result)

                    break


# Run the program

if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("\nJarvis has been shut down.")
```
