import time
from datetime import datetime
from playsound3 import playsound

ALARM_SOUND = "alarm.mp3"

def parse_time(value):
    try:
        alarm_time = datetime.strptime(value.strip(), "%H:%M")
        return alarm_time.strftime("%H:%M")
    except ValueError:
        raise ValueError("Invalid format")

def set_alarm():
    while True:
        value = input("enter alarm (HH:MM)")
        try:
            return parse_time(value)
        except ValueError as error:
            print(error)

def show_alarm(alarm_time):
    if alarm_time:
        print(f"alarm is {alarm_time}")
    else:
        print("No alarm")

def wait_for_alarm(alarm_time):
    print("waiting for alarm....")
    while True:
        current_time = datetime.now().strftime("%H:%M")
        if current_time == alarm_time:
            print(f"ALARM {alarm_time}")
            try:
                playsound(ALARM_SOUND)
            except Exception as error:
                print(f"{error}")

            return
        time.sleep(1)


def main():
    alarm_time = None
    print("Alarm clock")

    while True:
        print("1. Set Alarm")
        print("2. Show Alarm")
        print("3. Start Alarm")
        print("4. Cancel Alarm")
        print("5. Exit")

        choice = input("Enter menu choice ").strip()

        if choice == "1":
            alarm_time = set_alarm()
            print(f"alarm is set for {alarm_time}.")
        elif choice == "2":
            show_alarm(alarm_time)
        elif choice == "3":
            if alarm_time is None:
                print("No alarm found")
                continue

            try:
                wait_for_alarm(alarm_time)
                alarm_time = None
            except KeyboardInterrupt:
                print("Alarm cancelled")
        elif choice == "4":
            if alarm_time is None:
                print("No alarm found")
            else:
                print(f"alarm at {alarm_time} cancelled")
                alarm_time = None
        elif choice == "5":
            print("goodbye")
            break;
        else:
            print("invalid option")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Goodbye")