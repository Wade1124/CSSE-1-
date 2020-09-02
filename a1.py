"""
CSSE1001 Assignment 1
Semester 2, 2020
"""

from a1_support import*

def select_word_at_random(word_select):
    if word_select != 'FIXED' and word_select != 'ARBITRARY':
        return
    elif word_select == 'FIXED':
        words = load_words(word_select)
        index = random_index(words)
        word = words[index]
        return word
    elif word_select == 'ARBITRARY':
        words = load_words(word_select)
        index = random_index(words)
        word = words[index]
        return word

def create_guess_line(guess_no , word_length):
    tuple = GUESS_INDEX_TUPLE[word_length - 6]
    count = f'Guess {guess_no}' + WALL_VERTICAL
    for len in range(word_length):
        if tuple[guess_no - 1][0] <= len <= tuple[guess_no - 1][1]:
            count = count + ' ' + '*' + ' ' + WALL_VERTICAL
        else:
            count = count + ' ' + WALL_HORIZONTAL + ' ' + WALL_VERTICAL
    return count

def display_guess_matrix(guess_no, word_length, scores):
    if word_length == 8:
        print(' ' * 7 + '| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |')
        print(WALL_HORIZONTAL * (9 + 4 * word_length))
    elif word_length == 9:
        print(' ' * 7 + '| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |')
        print(WALL_HORIZONTAL * (9 + 4 * word_length))
    elif word_length == 7:
        print(' ' * 7 + '| 1 | 2 | 3 | 4 | 5 | 6 | 7 |')
        print(WALL_HORIZONTAL * (9 + 4 * word_length))
    else:
        print(' ' * 7 + '| 1 | 2 | 3 | 4 | 5 | 6 |')
        print(WALL_HORIZONTAL * (9 + 4 * word_length))
    for i in range (1,guess_no):
        print(create_guess_line(i, word_length) + '   ' + f'{scores[i-1]} Points')
    print(create_guess_line(guess_no, word_length))
    print(WALL_HORIZONTAL * (9 + 4 * word_length))

def compute_value_for_guess(word, start_index, end_index, guess):
    total_points = 0
    right_word = word[start_index: end_index + 1]
    for r in range(len(guess)):
        if guess[r] == right_word[r]:
            if guess[r] in VOWELS:
                total_points = total_points + 14
            else:
                total_points = total_points + 12
        elif guess[r] in right_word:
            total_points = total_points + 5
        return total_points

def main():
    print(WELCOME)
    while True:
        start = input(INPUT_ACTION)
        if start == 'h':
            print(HELP)
            break
        elif start == 'q':
            return
        elif start == 's':
            break
        else:
            print(INVALID)
            continue
    while True:
        word_select = str(input("Do you want a 'FIXED' or 'ARBITRARY' length word?: "))
        if word_select == 'FIXED' or word_select == 'ARBITRARY':
            load_words(word_select)
            word = select_word_at_random(word_select)
            print('Now try and guess the word, step by step!!')
            guess_no = 0
            scores = ()
            word_length = len(word)
            while guess_no < word_length:
                guess_no = guess_no + 1
                tuple = GUESS_INDEX_TUPLE[word_length - 6]
                start_index = tuple[guess_no -1][0]
                end_index = tuple[guess_no - 1][1]
                display_guess_matrix(guess_no, word_length, scores)
                if guess_no <= word_length - 1:
                    count = f'Guess {guess_no}'
                    guess = input('Now Enter ' + count + ': ')
                    score = compute_value_for_guess(word, start_index,end_index, guess)
                    scores = scores + (score, )
                else:
                    final_guess = input('Now enter your final guess. i.e. guess the whole world: ')
                    if final_guess == word:
                        print ('You have guessed the word correctly. Congratulations.')
                    else:
                        print('Your guess was wrong. The correct word was \ "' + word + '\"')
                        break
                    break
            break

if __name__ == "__main__":
    main()