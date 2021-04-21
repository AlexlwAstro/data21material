# Determine if a word or phrase is an isogram.
#
# An isogram (also known as a "nonpattern word") is a word or phrase without a repeating letter,
# however spaces and hyphens are allowed to appear multiple times.
#
# Examples of isograms:
#
# lumberjacks
# background
# downstream
# six-year-old
#
# The word isograms, however, is not an isogram, because the s repeats.

# think about using 'strip' and 'replace'
word_to_test = '  something...'
print(f'testing : \'{word_to_test}\'')
only_alphas = word_to_test.strip()
for nth_character in only_alphas:
    if not nth_character.isalpha():
        only_alphas = only_alphas.replace(nth_character, '')

print(f'alphabetic characters in \'{word_to_test}\' ---> \'{only_alphas}\'')
isogram_status = 'an isogram'
letter_count = 0
while isogram_status == 'an isogram':
    for nth_alpha in only_alphas:
        letter_count += 1
        only_alphas.count(nth_alpha)
        print(only_alphas.count(nth_alpha))
        if only_alphas.count(nth_alpha) > 1:
            isogram_status = 'NOT an isogram'
    if letter_count == len(only_alphas):
        print(f'reached end of the alphas after {letter_count} letters')
        break

print(f'{word_to_test} is {isogram_status}')

#----- function-fromat rewrite
def string_prep_for_isogram(word_to_test):
    print(f'testing : \'{word_to_test}\'')
    only_alphas = word_to_test.strip()
    for nth_character in only_alphas:
        if not nth_character.isalpha():
            only_alphas = only_alphas.replace(nth_character, '')
    print(f'alphabetic characters in \'{word_to_test}\' ---> \'{only_alphas}\'')
    return only_alphas

def isogram_test(word_to_test):
    only_alphas = string_prep_for_isogram(word_to_test)
    isogram_status = True
    isogram_print_string = 'an isogram'
    letter_count = 0
    while isogram_status:
        for nth_alpha in only_alphas:
            letter_count += 1
            only_alphas.count(nth_alpha)
            print(only_alphas.count(nth_alpha))
            if only_alphas.count(nth_alpha) > 1:
                isogram_status = False
                isogram_print_string = 'NOTan isogram'
        if letter_count == len(only_alphas):
            print(f'reached the end of the alphas after {letter_count} letters')
            break
    print(f'{word_to_test} is {isogram_print_string}')
    return isogram_status