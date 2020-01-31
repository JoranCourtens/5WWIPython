def hint(geraden_woord, juiste_woord):
    hint = ''
    for letter in range(0, len(geraden_woord)):
        if geraden_woord[letter] in juiste_woord:
            if geraden_woord[letter] == juiste_woord[letter]:
                hint += geraden_woord[letter].upper()
            else:
                hint += geraden_woord[letter]
        else:
            hint += '.'

    return hint
