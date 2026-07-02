import json, os
import sys
from datetime import datetime, date

FILE_PATH = 'data.json'

def read_json():
    try:
        with open(FILE_PATH, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        write_json([])
        return []

def write_json(data):
    with open(FILE_PATH, "w") as f:
        json.dump(data, f, indent=4)

def ask_event_name():
    while True:
        event_name = input('Enter event name: ')

        if not event_name.strip():
            print('Event name cannot be empty\n')
            continue

        return event_name

def ask_date():
    while True:
        event_date = input('Please enter the date to remind ( DD/MM/YYYY ): ')

        if event_date.strip() == '':
            print('Date must not be empty\n')
            continue

        try:
            today = datetime.today().date()

            object_date = datetime.strptime(event_date, '%d/%m/%Y').date()

            if object_date < today:
                print('Date is in the past, please enter a valid date\n')
                continue
            else:
                print('Date is today\n' if object_date == today
                      else f'You entered the date {event_date}\n')
                return event_date
        except ValueError:
            print('Date format is wrong, please use DD/MM/YYYY format\n')

def save_json(eventname, date):
    events = read_json()

    events.append({
        "eventname": eventname,
        "date": date
    })

    write_json(events)
    print("Event successfully added to JSON list!\n")

def read_event():
    events = read_json()

    today = date.today()

    if not events:
        print("No events recorded yet.\n")
        return

    print('\n=== YOUR EVENTS ===')
    for index, event in enumerate(events, start=1):
        print(f'{index}. {event["eventname"]}: {event["date"]}', end=' ')

        event_date = datetime.strptime(event["date"], '%d/%m/%Y').date()
        delta = event_date - today
        if delta.days == 0:
            print('— TODAY')
        elif delta.days > 0:
            print(f'— {delta.days} days left')
        else:
            print(f'— passed {abs(delta.days)} days ago')
    print('===================\n')

def add_event():
    event_name = ask_event_name()
    event_date = ask_date()

    save_json(eventname=event_name, date=event_date)

def delete_event_by_name():
    if not os.path.exists(FILE_PATH) or os.path.getsize(FILE_PATH) == 0:
        print('No events to delete.\n')
        return

    eventname = ask_event_name()

    data = read_json()

    for contact in data:
        if contact['eventname'] == eventname:
            confirm = input('Are you sure you want to remove this event? (y/n): ')

            if confirm.lower() == 'y':
                data.remove(contact)
                write_json(data)
                return

    print('Event not found.\n')

def update_event():
    update = input('Search for the date by it\'s name: ')

    events_list = read_json()

    for e in events_list:
        if e['eventname'] == update:
            new_date = ask_date()

            e["date"] = new_date
            write_json(events_list)
            print('Event successfully updated!\n')
            return

    print('Event name does not match!\n')

def main():
    while True:
        print('1. Check events status')
        print('2. Add event')
        print('3. Delete event')
        print('4. Update event')
        print('5. Quit')

        menu = input('Enter your choice: ')

        if menu.strip() == '':
            print('Please select an option\n')
            continue

        if menu == '1':
            read_event()
        elif menu == '2':
            add_event()
        elif menu == '3':
            delete_event_by_name()
        elif menu == '4':
            update_event()
        elif menu == '5':
            sys.exit('Program exited with code 0')
        else:
            print('Please select an option\n')

if __name__ == '__main__':
    main()