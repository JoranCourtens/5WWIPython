def is_palindroom(woord):
    n = 1
    for i in range(0, len(woord)):
        if woord[i] == woord[i + (len(woord) - n)]:
            n += 2
            i += 1
            if i == len(woord):
                return True
        else:
            return False
