import csv
"""
with open('user_details.csv', 'r') as input_file:
    csv_reader = csv.reader(input_file, delimiter=',')
    print(type(csv_reader))
    iterable_csv = iter(csv_reader)
    next(iterable_csv)
    for row in iterable_csv:
        print(row)
"""


def extract_user_details(csv_name='user_details.csv'):
    try:
        with open(csv_name, 'r') as input_file:
            csv_reader = csv.reader(input_file, delimiter=',')
            csv_read_list = list(iter(csv_reader))
    except FileNotFoundError:
        print('Error! File not found!')
    return csv_read_list


def transform_user_details(iterable_csv):
    # only save first name, last name and email address
    #iterable_csv =
    name_email_list = []
    # next(iterable_csv)
    csv_iterator = 0
    for line in iterable_csv:
        if csv_iterator == 0:
            firstname_index = line.index('firstName')
            lastname_index = line.index('lastName')
            email_index = line.index('email')
        else:
            name_email_list.append(f'{line[firstname_index]},{line[lastname_index]},{line[email_index]}')
        csv_iterator += 1
    return name_email_list


def load_user_detail_to_file(input_list, output_file='new_details.txt'):
    with open(output_file, 'w') as fw_out:
        fw_out.writelines(f'{row}\n' for row in input_list)

# extract
user_details_reader_list = extract_user_details()

# transform & print for confirmation
user_names_emails_list = transform_user_details(user_details_reader_list)
for item in user_names_emails_list:
    print(item)

# load to an output .txt file
load_user_detail_to_file(user_names_emails_list)
