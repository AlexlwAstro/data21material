"""
threes_fives_list = []
for i in range(1, 1000):
    if i%3 == 0 or i%5 == 0:
        threes_fives_list.append(i)

sum_of_3s5s = sum(threes_fives_list)
print(sum_of_3s5s)

current_index = 2
# initialise to third term's index in Fibonacci sequence
f_list = [1, 2]
f_sum_evens = 2
f_lt4m = True

while f_lt4m:
    i = current_index
    fn = f_list[i-1] + f_list[i-2]
    print(fn, f_list[i-1], f_list[i-2])
    current_index += 1
    if fn < 4000000:
        f_list.append(fn)

    if fn < 4000000 and (fn % 2) == 0:
        f_sum_evens += fn
    elif fn >= 4000000:
        print(f'stopped at {fn}, Fibonacci index {current_index}')
        break

print(f'last value = {f_list[-1]}')
print(f'\nsum of even values = {f_sum_evens} <-- FINAL ANSWER')
"""

"""
def find_primes(n, up_front_deletes=[], step_size=1):
    first_n_nums = list(range(1, n+1, step_size))
    print(type(first_n_nums))
    primes = []
    if len(up_front_deletes) > 0:
        for small_num in up_front_deletes:
            for integer in first_n_nums:
                if integer % small_num == 0:
                    first_n_nums.remove(integer)
                    print(f'Removing {integer} for division of {small_num}...')
        print(f'Reduced list for finding primes up to {n}:{len(first_n_nums)} in length')
    for integer in first_n_nums:
        prime = True
        for i in range(2, integer):
            if integer % i == 0:
                prime = False
        if prime:
            primes.append(integer)
    return primes

primes_below_twenty = find_primes(20)
primes_below_twenty.remove(1)
print(primes_below_twenty)
primes_below_two_million = find_primes(2000000, primes_below_twenty, 2)
"""
print(sum(primes_below_two_million))

#first_n_nums = range(1, 10+1,2)
#for i in first_n_nums:
#    print(i)




"""
print(primes)
primes_product = 1
for p_num in primes:
    primes_product = primes_product*p_num

#primes_product = int(primes_product/30)
print(primes_product)
factor_test = find_factors(primes_product)
print(factor_test)

test_num = 2520
first_20_not_evenly_div = True
while first_20_not_evenly_div:
    test_num = test_num + primes_product
    non_zero_remainder_count = 0
    for i in first_20_nums:
        if test_num % i != 0:
            non_zero_remainder_count += 1
    print(test_num, non_zero_remainder_count)
    if non_zero_remainder_count == 0:
        print(f'found the answer: {test_num}')
        first_20_not_evenly_div = False
        break
"""