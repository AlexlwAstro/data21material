# cinema tickets - users input their name and age
# # code checks input for feasibility
# # produce age restrictions

# dictionary of ratings (values) and the unaccompanied-age thresholds (keys)
uk_film_age_ratings = {
    0: 'U',
    8: 'PG',
    12: '12A',
    15: '15',
    18: '18'
}
# initialise boolean check for name, age while loops
name_check = True
age_check = True

while name_check:
    name_input = input("What is your name?\n")
    # check that the name input string contains only alphabetical characters
    if name_input.isalpha():
        name_check = False
        break
    print(f"Sorry! \'{name_input}\' is not a valid name! Please try again.")

while age_check:
    age_input = input("How old are you, in years?\n")
    # check that the age input string contains only numeric characters, is positive
    # and does not exceed the longest-known human lifespan
    if age_input.isnumeric() and (int(age_input) >= 0) and (int(age_input) < 125):
        age_check = False
        age_input = int(age_input)
        break
    print(f"Sorry! \'{age_input}\' is not a valid or feasible age! Please type in your age in whole years.")

uppermost_age_limit = 0
# sort (integer) keys from lowest to highest
for key_age in sorted(uk_film_age_ratings.keys()):
    if age_input >= key_age:
        # overwrite age limit with higher value if condition fulfilled
        uppermost_age_rating = key_age
uppermost_age_rating = uk_film_age_ratings[uppermost_age_limit]

print(f"You're {age_input} years old, so you can buy tickets for films rated up to and including \'{uppermost_age_rating}\', {name_input}!")


""" CODE-DUMPING COMMENT - IGNORE THIS!
if age_input >= 18:
    print(f"You're {age_input}, so you can buy tickets for any film here, {name_input}!")
elif age_input >= 15:
    print(f"You're {age_input}, so you can buy tickets for films rated up to and including \'15\', {name_input}!")
elif age_input >= 12:
    print(f"You're {age_input}, so you can buy tickets for films rated up to and including \'12A\', {name_input}!")
elif age_input >= 8:
    print(f"You're {age_input}, so you can buy tickets for films rated up to and including \'PG\', {name_input}!")
else:
    print(f"Sorry, {name_input}! {age_input}-year-olds are too young to buy tickets for age-restricted films here! \
    You can still get tickets for \'U\' movies though!")
"""