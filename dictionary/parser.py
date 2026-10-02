from core.models import (
    Pronunciation,
    Phonetics,
    Definition,
    DictionaryEntry,
)


def parse_dictionary_entry(data):
    entry = data["entry"]

    word = entry["word"]

    uk_data = entry["phonetics"]["uk"]
    us_data = entry["phonetics"]["us"]

    uk = Pronunciation(
        text=uk_data["text"],
        audio=uk_data["audio"],
    )

    us = Pronunciation(
        text=us_data["text"],
        audio=us_data["audio"],
    )

    phonetics = Phonetics(
        uk=uk,
        us=us,
    )

    definitions = []

    for definition_data in entry["english_definitions"]:
        definition = Definition(
            part_of_speech=definition_data["part_of_speech"],
            definition=definition_data["definition"],
            examples=definition_data.get("examples", []),
        )

        definitions.append(definition)

    return DictionaryEntry(
        word=word,
        phonetics=phonetics,
        definitions=definitions,
    )