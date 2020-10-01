# küsime ringide arvu, mis janesed peavad läbi jooksma
ringide_arv = int(input("Sisesta ringide arv: "))
# ringliiklus hakkab pihta 1.st ringist
ringi_number = 1
# nii kaua kui ei jooksnud - porgandeid pole
porgandite_arv = 0
# nii kaua, kui jooksev ringi number on väiksem kui kogu ringide arv
while(ringi_number <= ringide_arv):
    # tuvastame, millise ringi hetkel jookseme
    print(ringi_number)
    # porgandeid saame ainult paarisnumbriga ringis
    if(ringi_number % 2 == 0):
        # uus porgandite arv on vana arv, mis oli ennem antud ringi
        # plus ringi number, kuna antakse sama palju poegandeid,
        # kui on ringi numbri väärtus
        porgandite_arv = porgandite_arv + ringi_number
        # väljastame endale, mitu porgandeid peame saama
        print("said " + str(ringi_number) + " porgandid")
        # kontrollime, kas hetkel meil on just nii palju kokku porgandeid
        print("kokku hetkel on " + str(porgandite_arv) + " porgandeid")
    # liigume järgmisele ringile - suurendame ringi number 1 võrra
    ringi_number += 1
# väljastame porgandite koguarv, kui kõik ringid on läbi joostud
print("porgandite koguarv " + str(porgandite_arv))