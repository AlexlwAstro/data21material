def open_and_print_file(file='order.txt'):
    try:
        with open(file, "r") as file_to_open:
            for line in file_to_open.readlines():
                print(line.rstrip('\n'))
    except FileNotFoundError as err_msg:
        print('Error! File not found! Do something about it!')
        print(err_msg)
    except FileExistsError:
        print('Error! File already exists!')
    finally:
        print("Executed Order 66")


def write_to_file(order_list, file='order.txt'):
    try:
        with open(file, "a") as writing_file:
            writing_file.writelines('\n' + i for i in order_list)
    except FileNotFoundError as err_msg:
        print('Error! File not found! Do something about it!')
        print(err_msg)


new_lines_list = ['A', 'bunch', 'of', 'new', 'lines']
open_and_print_file()
write_to_file(new_lines_list)
