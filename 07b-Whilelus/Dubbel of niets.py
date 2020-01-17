#invoer
kapitaal_speler = int(input('Kapitaal speler: '))

#berekening
inzet_speler = 0
alles = kapitaal_speler
stop = 0
while kapitaal_speler > inzet_speler:
    inzet_speler = int(input('Inzet speler: '))
    if inzet_speler == 0:
        print('Je eindigt met {}'.format(kapitaal_speler))
    gekozen_kleur = str(input('Rood of zwart: '))
    gedraaid_kleur = str(input('Gedraaid kleur: '))
    if gekozen_kleur == gedraaid_kleur:
        kapitaal_speler = kapitaal_speler * 2
    elif gekozen_kleur != gedraaid_kleur:
        kapitaal_speler = kapitaal_speler - kapitaal_speler

print('Je kunt geen {} inzetten als je maar {} hebt.'.format(inzet_speler, kapitaal_speler))

...

