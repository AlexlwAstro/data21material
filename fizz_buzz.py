list_start = input('Where do you want to start your Fizzing and Buzzing list from?\n')
list_end = input(f'Starting from {list_start}, up to which number (inclusive) do you want to test for Fizzing and Buzzing?\n')
range_to_test = list(range(int(list_start), int(list_end)+1))
print(f'Your chosen range is:\n {range_to_test}')

fizz_buzz_range = range_to_test.copy()
print('Here is your range - all fizzing, all buzzing!')
print('numbers','Fizzbuzz')
for i in range(len(range_to_test)):
    if (range_to_test[i] % 3) == 0 and (range_to_test[i] % 3) == 0:
        fizz_buzz_range[i] = 'FizzBuzz'
    elif (range_to_test[i] % 3) == 0:
        fizz_buzz_range[i] = 'Fizz'
    elif (range_to_test[i] % 5) == 0:
        fizz_buzz_range[i] = 'Buzz'
    print(range_to_test[i], fizz_buzz_range[i])

# ----- reformat into function
list_start = input('Where do you want to start your Fizzing and Buzzing list from?\n')
list_end = input(f'Starting from {list_start}, up to which number (inclusive) do you want to test for Fizzing and Buzzing?\n')
def FizzBuzz(list_start,list_end):
    range_to_test = list(range(int(list_start), int(list_end) + 1))
    fizz_buzz_range = range_to_test.copy()
    for num in range(len(range_to_test)):
        if (range_to_test[num] % 3) == 0 and (range_to_test[num] % 3) == 0:
            fizz_buzz_range[num] = 'FizzBuzz'
        elif (range_to_test[num] % 3) == 0:
            fizz_buzz_range[num] = 'Fizz'
        elif (range_to_test[num] % 5) == 0:
            fizz_buzz_range[num] = 'Buzz'
    return fizz_buzz_range


fb_to_print = FizzBuzz(10,23)
print(fb_to_print)

print("2")