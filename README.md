⏰ Python Alarm Clock

A simple command-line alarm clock built with Python. The program allows you to set, view, start, cancel, and exit an alarm.

Features

Set an alarm using HH:MM format

View the currently set alarm

Wait for the alarm to trigger

Play an MP3 sound when the alarm goes off

Cancel an existing alarm

Exit the application

Handles invalid time formats

Handles Ctrl+C interruptions

Requirements

Python 3.x

playsound3

Installation

Clone or download the project, then navigate into the project directory:

cd alarm-clock


Create a virtual environment:

python -m venv venv


Activate the virtual environment.

macOS / Linux
source venv/bin/activate

Windows
venv\Scripts\activate


Install the dependency:

pip install playsound3

Project Structure
alarm-clock/
├── main.py
├── alarm.mp3
├── README.md
└── venv/


Make sure alarm.mp3 is in the same directory as main.py.

Usage

Run the program:

python main.py


You will see:

Alarm clock

1. Set Alarm
2. Show Alarm
3. Start Alarm
4. Cancel Alarm
5. Exit

Set an Alarm

Choose:

1


Then enter a time in 24-hour format:

enter alarm (HH:MM) 18:30

Show Alarm

Choose:

2


The program displays the currently configured alarm:

alarm is 18:30

Start Alarm

Choose:

3


The program waits until the configured time:

waiting for alarm....


When the time is reached:

ALARM 18:30


The alarm.mp3 file will then play.

Cancel Alarm

Choose:

4


The current alarm will be cancelled.

Exit

Choose:

5


The program exits with:

goodbye

Time Format

The alarm uses 24-hour time:

HH:MM


Examples:

07:30
12:00
18:45
23:59

Stopping the Alarm

You can press Ctrl+C while the program is waiting for the alarm to interrupt it.

Dependencies

This project uses:

datetime — for handling and comparing times

time — for the one-second polling interval

playsound3 — for playing the alarm sound

datetime and time are included with Python, so only playsound3 needs to be installed separately.

License

This project is open source and available for learning and personal use.
