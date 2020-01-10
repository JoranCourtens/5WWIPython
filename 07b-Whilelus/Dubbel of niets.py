#invoer
kapitaal_speler = int(input('Kapitaal speler: '))

#berekening
inzet_speler = 0
while kapitaal_speler > inzet_speler:
    inzet_speler = input('Inzet speler: ')
    if inzet_speler == 'alles':
        inzet_speler = kapitaal_speler
    elif inzet_speler == 'stop':
        print('Je eindigt met {}'.format(kapitaal_speler))
    gekozen_kleur = str(input('Rood of zwart: '))
    gedraaid_kleur = str(input('Gedraaid kleur: '))
    if gekozen_kleur == gedraaid_kleur:
        kapitaal_speler = kapitaal_speler * 2
    elif gekozen_kleur != gedraaid_kleur:
        kapitaal_speler = kapitaal_speler - kapitaal_speler
    ...

