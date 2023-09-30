black_list = ["¡Suscríbete!", "¡Adiós!", "Subtitles by Amara.org community"]


def is_blacklisted(text):
    for blacklisted in black_list:
        if blacklisted in text:
            return True
    return False
