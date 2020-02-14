def roteer(woord, aantal):
    n = 0
    nieuw_woord = ''
    while aantal >= len(woord):
        aantal -= len(woord)
    for i in range(len(woord)):
        if aantal < (len(woord) - i):
            nieuw_woord += woord[i + aantal]
        else:
            nieuw_woord += woord[i - aantal + woord[n]]
            n += 1


    return nieuw_woord

