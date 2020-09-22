# kasutaja sisend
nimi = input("Sisestage oma nimi: ")
lubatud_kiirus = int(input("Sisestage lubatud kiirus km/h: "))
tegelik_kiirus = int(input("Sisestage tegelik kiirus km/h: "))
# arvutused
trahv = (tegelik_kiirus - lubatud_kiirus) * 3
# arvestame, et üle 190 ei oleks
trahv = min(trahv, 190)
# väljastus
print(nimi + ", kiiruse ületamise eest on teie trahv " + str(trahv) + " eurot.")