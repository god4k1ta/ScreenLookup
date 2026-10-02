from dictionary.api import lookup_word


data = lookup_word("present")

assert isinstance(data, dict)
assert data["found"] is True
assert "entry" in data
assert data["entry"]["word"] == "present"

print("All dictionary API tests passed.")