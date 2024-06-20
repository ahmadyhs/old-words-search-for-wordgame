from sqlalchemy import null, true
from sympy import false

def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words

def words_list(show_all_absolute_word, show_potential, show_potential_list, min, max) :
    english_words = load_words()

    possible_word = ''
    letters_needed = ''
    longest_abs_word = ''
    longest_abs_len = 0
    abs_word_list = []
    longest_pot_word = ''
    longest_pot_len = 0
    pot_word_list = []
    letters_list = []

    letters_list = list(input('\nletters list : '))

    for word in english_words:
        if len(word) >= min and len(word) <= max  :
            letters_combination = letters_list.copy()
            for letter in word :
                i = 0
                while i < len(letters_combination) :
                    if letter == letters_combination[i] :
                        possible_word += letter
                        letters_combination.pop(i)
                        break
                    i += 1

                    if i == len(letters_combination) - 1 :
                        letters_needed += letter

            if len(letters_needed) == 0 :
                if len(longest_abs_word) <= len(possible_word):
                    longest_abs_word = possible_word
                    longest_abs_len = len(possible_word)
                    abs_word_list += [[possible_word, len(possible_word)]]
                    
            elif len(letters_needed) <= 2 and show_potential == true :
                if len(longest_pot_word) <= len(word):
                    longest_pot_word = word
                    longest_pot_len = len(word)
                    pot_word_list += [[word, len(word), letters_needed]]
            
            possible_word = letters_needed = ''
    
    if show_all_absolute_word == true :
        limit = len(abs_word_list)
        i = 0
        print('\n\n----------ALL POSSIBLE WORDS----------\n')
        while i < limit :
            if abs_word_list[i][1] == longest_abs_len or abs_word_list[i][1] == longest_abs_len - 1 or abs_word_list[i][1] == longest_abs_len - 2:
                print(abs_word_list[i][0], '\tlength = ', abs_word_list[i][1])
            i += 1

    if show_potential == true and show_potential_list == true :
        limit = len(pot_word_list)
        i = 0
        print('\n----------ALL POTENTIAL WORDS----------\n')
        while i < limit :
            if pot_word_list[i][1] == longest_pot_len :
                print(pot_word_list[i][0], '\tlength = ', pot_word_list[i][1], '\tneed = ',pot_word_list[i][2])
            i += 1
    
    print('\nLongest absolute word = ',longest_abs_word, '\nlength = ', len(longest_abs_word))
    if show_potential == true :
        print('\nLongest potential word = ',longest_pot_word, '\nlength = ', len(longest_pot_word))
            
# MAIN #            

show_all_absolute_word = true
show_potential = true
show_potential_list = false
minimum_length = 6
maximum_length = 16

print('\n\n----------WORD COMBINATION FINDER----------\n')
stat = true
while stat == true :
    words_list(show_all_absolute_word, show_potential, show_potential_list, minimum_length, maximum_length)
    stat = input('\ncontinue? (y/n) ')
    if stat == 'y' : stat = true
    else : stat = false
