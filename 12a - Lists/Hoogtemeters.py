def hoogtemeters(lijst):
    hoogtemeters = []
    for element in range(len(lijst) - 1):
        if lijst[element] > lijst[element + 1]:
            hoogtemeters.append(-(lijst[element] - lijst[element + 1]))
        else:
            hoogtemeters.append(abs(lijst[element] - lijst[element + 1]))
    return hoogtemeters

def dalen_en_stijgen(lijst):
    stijgen = 0
    dalen = 0
    for element in lijst:
        if element > 0:
            stijgen += element
        else:
            dalen += element

    return (abs(dalen), stijgen)
