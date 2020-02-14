from math import sqrt
def binnen_of_buiten(middelpunt, co_cirkel, te_bepalen_co):
    straal = sqrt(pow(middelpunt[0] - co_cirkel[0], 2) + pow(middelpunt[1] - co_cirkel[1], 2))
    afstand_middelpunt_gegevenpunt = sqrt(pow(middelpunt[0] - te_bepalen_co[0], 2) + pow(middelpunt[1] - te_bepalen_co[1], 2))
    if straal == afstand_middelpunt_gegevenpunt:
        plaats = 'op'
    elif straal > afstand_middelpunt_gegevenpunt:
        plaats = 'binnen'
    else:
        plaats = 'buiten'
    afstand = afstand_middelpunt_gegevenpunt

    return (plaats, round(afstand, 4))

