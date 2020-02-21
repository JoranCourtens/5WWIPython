def dubbels(lijst):
    dubbel = []
    for element in lijst:
        if lijst.count(element) > 1 and element not in dubbel:
            dubbel.append(element)
    return dubbel
