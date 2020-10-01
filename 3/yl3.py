# juhuslikke täisarvude genereerimispakett
from random import randint
# sisestame soovitud täringu visete arv
soovitud_kord = int(input("Sisesta täringute arv: "))
# viskame täringut nii kaua, soovitud arv viske on tehtud
# selleks paneme korrad lugema
kord = 1
while(kord <= soovitud_kord):
    # teeme vise
    taring = randint(1, 6)
    # kontrollime, palju tuli
    print(taring)
    # liigume järgmisele visele
    kord += 1