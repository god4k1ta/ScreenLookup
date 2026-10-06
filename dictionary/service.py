from dictionary.api import lookup_word
from dictionary.parser import parse_dictionary_entry


def lookup_dictionary_word(word):
    data = lookup_word(word)
    dictionary_entry = parse_dictionary_entry(data)
    return dictionary_entry