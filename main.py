import os
import random
import speech_recognition
import webbrowser

# Настройки


sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.8

# Команды

commands_dict = {
    "commands": {

        # Приветствие Jarvis
        "greeting": [
            "привет джарвис"
        ],

        # Создание новой задачи / заметки
        "create_task": [
            "джарвис задача",
            "джарвис заметка"
        ],

        # Запуск случайной музыки из папки musicPython
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

# Распознавание речи


def listen_command(mic):
    try:
        audio = sr.listen(source=mic)
        query = sr.recognize_google(
            audio_data=audio,
            language="ru-RU"
        ).lower()

        print("Распознано:", repr(query))

        return query

    except speech_recognition.UnknownValueError:
        return ""

    except speech_recognition.RequestError:
        return ""

# Функции команд

def greeting(mic):
    """
    Отвечает на приветствие пользователя.
    """
    return "здравствуйте милорд"


def create_task(mic):
    """
    Запрашивает у пользователя текст задачи
    и сохраняет её в todo-list.txt.
    """

    print("Какова задача милорд?")

    task = listen_command(mic)

    if not task:
        return

    with open("todo-list.txt", "a", encoding="utf-8") as f:
        f.write(f"{task}\n")

    print(f"Задача добавлена: {task}")

def open_browser(mic):
    os.startfile(
        r"C:\Users\User\AppData\Local\Programs\Opera GX\opera.exe"
    )

    return "Открываю Оперу"

def play_music(mic):
    """
    Выбирает случайный музыкальный файл
    из папки musicPython и запускает его.
    """

    files = os.listdir("musicPython")
    print("Файлы:", files)

    random_file = os.path.join(
        "musicPython",
        random.choice(files)
    )

    print("Выбран файл:", random_file)

    os.startfile(random_file)

    return f"Запускаю: {os.path.basename(random_file)}"
# Связь команд с функциями

functions = {
    "greeting": greeting,
    "create_task": create_task,
    "play_music": play_music,
    "open_browser": open_browser,
}
# Главная функция

def main():
    """
    Получает голосовую команду,
    определяет её назначение
    и запускает соответствующую функцию.
    """
    #говорит о запуске джарвиса

    with speech_recognition.Microphone(device_index=1) as mic:
        print("Калибровка...")
        sr.adjust_for_ambient_noise(mic, duration=0.5)

        print("Джарвис запущен")

        # Код для того чтобы программа не выключалась
        # и чтобы прослушывала постоянно

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
#Запуск программы

if __name__ == "__main__":
    main()
