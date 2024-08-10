from .exceptions import *
import random
# Complete with your own, just for fun :)
LIST_OF_WORDS = [
    "python",
    "algorithm",
    "hangman",
    "programming",
    "challenge",
    "development",
    "computer",
    "keyboard",
    "function",
    "variable",
    "syntax",
    "compile",
    "debug",
    "execute",
    "iteration",
    "recursion",
    "software",
    "hardware",
    "interface",
    "database"
]


def _get_random_word(list_of_words):
    if not list_of_words:   # Check if the list is empty or None
        raise InvalidListOfWordsException('List cannot be empty')
    
    return random.choice(list_of_words)



def _mask_word(word):
    if not word:  # Check if the word is empty or None
        raise InvalidWordException("Word cannot be empty")
    
    return '*' * len(word)

def _uncover_word(answer_word, masked_word, character):
    if not answer_word:
        raise InvalidWordException()

    if not character or len(character) > 1:
        raise InvalidGuessedLetterException()

    try:
        word = ''
        index = 0
        for char in answer_word.lower():
            if char == character.lower():
                word += char
            else:
                word += masked_word[index]
            index += 1
        if len(masked_word) != len(word):
            raise InvalidWordException()
        return word
    except InvalidWordException:
        raise InvalidWordException()



def guess_letter(game, letter):
    if len(letter) > 1 or not letter.isalpha():
        raise InvalidGuessedLetterException("The guessed letter must be a single alphabetical character.")
    
    letter = letter.lower()
    if letter in game['previous_guesses']:
        raise AlreadyGuessedLetterException("You have already guessed that letter.")
    
    game['previous_guesses'].append(letter)

    if letter in game['answer_word'].lower():
        game['masked_word'] = _uncover_word(game['answer_word'].lower(), game['masked_word'].lower(), letter)
        
        if game['masked_word'].lower() == game['answer_word'].lower():
            raise GameWonException("Congratulations, you've won the game!")
    else:
        game['remaining_misses'] -= 1
        
        if game['remaining_misses'] == 0:
            raise GameLostException("Game over! You've used all your guesses.")



def start_new_game(list_of_words=None, number_of_guesses=5):
    if list_of_words is None:
        list_of_words = LIST_OF_WORDS

    word_to_guess = _get_random_word(list_of_words)
    masked_word = _mask_word(word_to_guess)
    game = {
        'answer_word': word_to_guess,
        'masked_word': masked_word,
        'previous_guesses': [],
        'remaining_misses': number_of_guesses,
    }

    return game
