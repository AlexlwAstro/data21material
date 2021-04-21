ex_string = 'sdsujogsivsjds'
print(ex_string.index('s'))
print(ex_string[4])

string_searcher = 0
while string_searcher < len(ex_string):
    string_searcher = ex_string.find('s', string_searcher)
    if string_searcher == -1: # if at end of word
        break
    print(f'found at {string_searcher}')
    string_searcher += 1
