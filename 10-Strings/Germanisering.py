def germaniseer(zin):
    nieuwe_zin = ''
    for i in range(0, len(zin)):
        if zin[i] == ' ':
            nieuwe_zin += ' ' + zin[i + 1].upper()
        elif zin[i - 1] != ' ':
            nieuwe_zin += zin[i]

    return nieuwe_zin


