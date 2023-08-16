print('Választás')
print('1. feladat: adatok beolvasása fájlból')

adatok = []
f = open('szavazatok.txt', 'r')
for sor in f:
        sor = sor.strip().split()
        adatok.append(sor)
f.close()


print('2. feladat: hány képviselójelölt indult a választáson?')
n = len(adatok)
print('A helyhatósági választáson ',n, ' képviselőjelölt indult.')


print('3. feladat: szavazatok száma')

def beker():
    veznev = input('Kérem a jelölt vezetéknevét! ')
    kernev = input('Kérem a jelölt keresztnevét! ')
    val = False
    
    for sor3 in adatok:
        if sor3[2] == veznev and sor3[3] == kernev:
            print(veznev,kernev,'nevű képviselőjelölt ',sor3[1],' darab szavazatot kapott.')
            val = True
        if val == False:
            print('Ilyen nevű képviselőjelölt nem szerepel a nyilvántartásban.')


print('4. feladat: hányan vettek részt a választáson? ')
db4 = 0
for sor4 in adatok:
    db4 += int(sor4[1])
print('A választáson',db4,'állampolgár, a jogosultak', round(db4/12345*100,2),'%-a vett részt.')

print('5. feladat: a pártokra leadott szavazatok százalékos megoszlása')
dbgyep, dbhep, dbtisz, dbzep, dbftl = 0, 0, 0, 0, 0
for sor5 in adatok:
    if sor5[4] == 'GYEP':
        dbgyep += int(sor5[1])
    if sor5[4] == 'HEP':
        dbhep += int(sor5[1])
    if sor5[4] == 'TISZ':
        dbtisz += int(sor5[1])
    if sor5[4] == 'ZEP':
        dbzep += int(sor5[1])
    if sor5[4] == '-':
        dbftl += int(sor5[1])
print('Gyümölcsevők pártja= ', round(dbgyep/db4*100, 2),'%')
print('Húsevők pártja= ', round(dbhep/db4*100, 2),'%')
print('Tejivók szövetsége= ', round(dbtisz/db4*100, 2),'%')
print('Zöldségevők pártja= ', round(dbzep/db4*100, 2),'%')
print('Független jelöltek= ', round(dbftl/db4*100, 2),'%')

print('6. feladat: melyik jelölt kapta a legtöbb szavazatot?')

def main():
    max6 = 0
    for sor6 in adatok:
        if int(sor6[1]) > max6:
            max6 = int(sor6[1])
    for sor6 in adatok:
        if max6 == int(sor6[1]):
            if sor6[4] == '-':
                print(sor6[2], sor6[3], 'független')
            else:
                print(sor6[2], sor6[3],sor6[4])

main()
            
            
            
print('7. feladat: az egyes választókerületekben kik lettek a képviselők?')
g = open('kepviselok.txt', 'w')
for i in range(8):
    max7 = 0
    vnev = adatok[0][2]
    knev = adatok[0][3]
    part = adatok[0][4]
    for sor8 in adatok:
        if int(sor8[0]) == i and int(sor8[1]) > max7:
            vnev = sor8[2]
            knev = sor8[3]
            part = sor8[4]
    if part != '-':
        sorom = str(i+1) + ' ' + vnev + ' ' + knev + ' ' + part + '\n'
    else:
        sorom = str(i+1) + ' ' + vnev + ' ' + knev + ' ' + 'független' + '\n'
    g.write(sorom)
g.close()




  
