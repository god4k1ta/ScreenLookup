from dictionary.parser import parse_dictionary_entry


data = {
    "entry": {
        "word": "present",
        "phonetics": {
            "uk": {
                "text": "ˈprez(ə)nt; prɪˈzent",
                "audio": "/api/v1/dictionary/audio?accent=uk&word=present",
            },
            "us": {
                "text": "ˈprez(ə)nt; prɪˈzent",
                "audio": "/api/v1/dictionary/audio?accent=us&word=present",
            },
        },
        "english_definitions": [
            {
                "part_of_speech": "n.",
                "definition": "the period of time that is happening now",
                "examples": [
                    "She is living in the present."
                ],
            },
            {
                "part_of_speech": "v.",
                "definition": "to give something to someone",
            },
        ],
    }
}


dictionary_entry = parse_dictionary_entry(data)


assert dictionary_entry.word == "present"

assert dictionary_entry.phonetics.uk.text == "ˈprez(ə)nt; prɪˈzent"
assert dictionary_entry.phonetics.uk.audio == "/api/v1/dictionary/audio?accent=uk&word=present"

assert dictionary_entry.phonetics.us.text == "ˈprez(ə)nt; prɪˈzent"
assert dictionary_entry.phonetics.us.audio == "/api/v1/dictionary/audio?accent=us&word=present"

assert len(dictionary_entry.definitions) == 2

assert dictionary_entry.definitions[0].part_of_speech == "n."
assert dictionary_entry.definitions[0].definition == "the period of time that is happening now"
assert dictionary_entry.definitions[0].examples == [
    "She is living in the present."
]

assert dictionary_entry.definitions[1].part_of_speech == "v."
assert dictionary_entry.definitions[1].definition == "to give something to someone"
assert dictionary_entry.definitions[1].examples == []

print("All dictionary parser tests passed.")