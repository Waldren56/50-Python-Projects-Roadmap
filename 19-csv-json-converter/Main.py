import csv, json, os

def create_empty_csv(filename):
    """ If a file is empty, it fills it with temporary fields """
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow([
            "employee_id",
            "first_name",
            "last_name",
            "department",
            "position",
            "salary",
            "email"
        ])

def convert_csv_to_json(file_name):
    """ Converts a csv file to a json file """
    base = os.path.splitext(file_name)[0]
    output = base + '.json'

    with open(file_name, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        content = list(reader)

    with open(output, mode="w", encoding="utf-8") as json_file:
        json.dump(content, json_file, ensure_ascii=False, indent=4)

    print(json.dumps(content, ensure_ascii=False, indent=4))

def main():
    file_name = input('What .csv file do you want to convert?: ') + '.csv'

    if not os.path.exists(file_name):
        create_empty_csv(file_name)
        print('File not found — a template has been created. Fill it and run again.')
        return

    with open(file_name, 'r', encoding='utf-8') as f:
        content = list(csv.DictReader(f))

    if not content:
        print('The CSV file is empty — add some data and run again.')
        return

    convert_csv_to_json(file_name)

if __name__ == '__main__':
    main()