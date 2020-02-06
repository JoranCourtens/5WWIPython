def splits(getal):
    stap = 0
    for i in str(getal):
        stap += 1
        if stap == 1:
            getal_1 = i
        elif stap == 2:
            getal_2 = i
        elif stap == 3:
            getal_3 = i
        else:
            getal_4 = i
    return int(getal_1), int(getal_2), int(getal_3), int(getal_4)


def oplopende_cijfers(getal_1, getal_2, getal_3, getal_4):
    kleinste_cijfer = min(getal_1, getal_2, getal_3, getal_4)
    kleinste_middelste_cijfer = min(max(getal_1, getal_2), max(getal_1, getal_3), max(getal_1, getal_4), max(getal_2, getal_3), max(getal_2, getal_4), max(getal_3, getal_4))
    grootste_cijfer = max(getal_1, getal_2, getal_3, getal_4)
    grootste_middelste_cijfer = getal_1 + getal_2 + getal_3 + getal_4 - kleinste_cijfer - kleinste_middelste_cijfer - grootste_cijfer
    return int(kleinste_cijfer), int(kleinste_middelste_cijfer), int(grootste_middelste_cijfer), int(grootste_cijfer)


def op_af_getallen(kleinste_cijfer, kleinste_middelste_cijfer, grootste_middelste_cijfer, grootste_cijfer):
    oplopend_getal = '{}{}{}{}'.format(kleinste_cijfer, kleinste_middelste_cijfer, grootste_middelste_cijfer, grootste_cijfer)
    aflopend_getal = '{}{}{}{}'.format(grootste_cijfer, grootste_middelste_cijfer, kleinste_middelste_cijfer, kleinste_cijfer)
    return oplopend_getal, aflopend_getal


def verschil(aflopend_getal, oplopend_getal):
    verschil = max(int(oplopend_getal), int(aflopend_getal)) - min(int(oplopend_getal), int(aflopend_getal))
    return str(verschil)


...

