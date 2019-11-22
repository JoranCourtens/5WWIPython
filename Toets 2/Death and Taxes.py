#invoer
bruto_jaarsalaris = float(input('Geef bruto jaarsalaris: '))

#berekening

rsz_aftrek = (bruto_jaarsalaris / 100) * 13.07
belastingen_schijf_1 = ((4390 / 100) * 25)
print(belastingen_schijf_1)
belastingen_schijf_2 = (((bruto_jaarsalaris - rsz_aftrek - 10140.00) / 100) * 40)
print(belastingen_schijf_2)
belastingen_schijf_3 = (((bruto_jaarsalaris - rsz_aftrek - 23390.00) / 100) * 45)
print(belastingen_schijf_3)
belastingen_schijf_4 = (((bruto_jaarsalaris - rsz_aftrek - 40480.01) / 100) * 50)
print(belastingen_schijf_4)

if(bruto_jaarsalaris - rsz_aftrek) < 8860.00:
    voorheffing = 0.00
elif(bruto_jaarsalaris - rsz_aftrek) <= 13250.00:
    voorheffing = belastingen_schijf_1
elif(bruto_jaarsalaris - rsz_aftrek) <= 23390.00:
    voorheffing = belastingen_schijf_1 + belastingen_schijf_2
elif(bruto_jaarsalaris - rsz_aftrek) <= 40480.00:
    voorheffing = belastingen_schijf_1 + belastingen_schijf_2 + belastingen_schijf_3
else:
    voorheffing = belastingen_schijf_1 + belastingen_schijf_2 + belastingen_schijf_3 + belastingen_schijf_4
print(float(voorheffing))
