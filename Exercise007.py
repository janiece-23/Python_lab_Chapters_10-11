from Exercise006 import word_distance
from Exercise005 import load_word_dict

if __name__ == '__main__':
    word_dict_path = 'files/word_dict.json'
    word_dict = load_word_dict(word_dict_path)
    for k, v in word_dict.items():
        if len(v) > 1: #These are all the words that will be anagrams
            for i in range( len( v ) ): #Should start with the first word in the list.
                for j in range( i + 1, len( v ) ): # Will compare words to each others, but not the word itself.
                    if word_distacne( v[i], v[j] ) == 2:
                        print( f'Metathesis: {v[j]}' )