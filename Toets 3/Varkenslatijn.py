def verwijder_medeklinkers(oorspronkelijk_woord):
    woord_zonder_medeklinkers = ''
    i = 0
    while oorspronkelijk_woord[i] != 'a' and oorspronkelijk_woord[i] != 'e' and oorspronkelijk_woord[i] != 'o' and oorspronkelijk_woord[i] != 'u' and oorspronkelijk_woord[i] != 'i':
        woord_zonder_medeklinkers += ''
        i += 1
    woord_zonder_medeklinkers += oorspronkelijk_woord[i:]

    return woord_zonder_medeklinkers

def varkenslatijn(woord):
    if woord[0] == 'a' or woord[0] == 'i' or woord[0] == 'u' or woord[0] == 'e' or woord[0] == 'o':
        woord += 'ibus'
    elif woord[len(woord) - 1] == 'a' or woord[len(woord) - 1] == 'i' or woord[len(woord) - 1] == 'u':
        woord += 'nt'
    else:
        verwijder_medeklinkers(woord)
        woord += 'itum'
    woord.replace('j', 'i')
    woord.replace('y', 'z')
    return woord

def vertaal(zin):
    zin.strip()
    verwijder_medeklinkers(zin)
    varkenslatijn(zin)

    return zin


