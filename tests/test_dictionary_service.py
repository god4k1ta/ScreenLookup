from dictionary.service import lookup_dictionary_word
from core.models import DictionaryEntry


data = lookup_dictionary_word("present")

assert isinstance(data, DictionaryEntry)
assert data.word == "present"

print("All dictionary service tests passed.")