def get_words(filename):
    with open(filename, encoding="utf8") as file:
        text = file.read()
    text = text.replace("\n", " ").replace(",", "").replace(":", "").replace("...", "")
    text = text.lower()
    return text