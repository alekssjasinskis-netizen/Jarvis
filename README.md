# Jarvis

A custom voice assistant inspired by JARVIS from Marvel.

## Features

* Voice command recognition
* Continuous voice listening
* Task creation and saving to `todo-list.txt`
* Random music playback
* Browser launching
* Voice greeting
* System sound effects
* Startup and shutdown sounds

## Voice Commands

Currently supported commands:

* `hello jarvis` — voice greeting
* `jarvis task` — create a task
* `jarvis note` — create a note
* `play simple` — play random music
* `jarvis open browser` — open Opera GX
* `jarvis shut down` — shut down Jarvis
* `jarvis stand down` — shut down Jarvis

## Technologies

* Python
* SpeechRecognition
* Google Speech Recognition API
* Pygame

## Project Structure

```text
Jarvis/
├── JarvisSounds/       # System sound effects
├── musicPython/        # Music files
├── jarvis.py           # Main program
└── todo-list.txt       # Saved tasks
```

## Current Status

This project is currently in development. New features and improvements will be added over time.
