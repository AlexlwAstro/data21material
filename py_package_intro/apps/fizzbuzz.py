"""
 put class-formatted fizz buzz game here
 
 run 'pip install' in pycharm terminal when this is filled
"""


class FizzBuzz:
    def __init__(self, list_start, list_end):
        self.list_start = list_start
        self.list_end = list_end
        self.range_to_test = list(range(self.list_start, self.list_end + 1))

    def get_list_to_run(self):
        return self.range_to_test

    def get_fizzbuzz(self, rng, out_fb):
        for i in range(len(rng)):
            if (fb_range_to_run[i] % 3) == 0 and (fb_range_to_run[i] % 3) == 0:
                fizz_buzz_range[i] = 'FizzBuzz'
            elif (fb_range_to_run[i] % 3) == 0:
                fizz_buzz_range[i] = 'Fizz'
            elif (fb_range_to_run[i] % 5) == 0:
                fizz_buzz_range[i] = 'Buzz'
    def make_fizzbuzz_list(self):
        l_start = int(self.list_start)
        l_end = int(self.list_end)
        fb_range_to_run = self.range_to_test
        print(f'Your chosen range for fizzing/buzzing is:\n {fb_range_to_run}')
        fizz_buzz_range = fb_range_to_run.copy()

        print(f'Final FizzBuzz result for numbers between {l_start} and {l_end}:\n', fizz_buzz_range)
        return fizz_buzz_range


fb_to_print = FizzBuzz(1, 23)
fb_to_print.get_list_to_run()
fb_to_print.make_fizzbuzz_list()
