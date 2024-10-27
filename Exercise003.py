letters = 'abcdefghijklmnopqrstuvwxyz'
numbers = range( len( letters ) )
letter_map = dict( zip( letters, numbers ) )

def shift_word(word, shift):
    ciphertext = ''
    for l in word:
        l_index = (letter_map[l] + shift) % len(letters)
        ciphertext += letters[l_index]
    return ciphertext

if __name__ == '__main__':

    print(shift_word('cheer', 7))
    print(shift_word('melon', 16))
