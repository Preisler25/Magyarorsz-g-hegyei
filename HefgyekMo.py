class Hegyek:
    def __init__(self, list):
        self.csucs_nev = list[0]
        self.hegyseg_nev = list[1]
        self.magassag = int(list[2])

def makingObjects():
    list = []
    temp = importFromTXT()
    for i in range(1, len(temp)):
        list.append(Hegyek(temp[i].split(";")))
    return list

def importFromTXT():
    f = open("hegyekMo.txt", "r", encoding="UTF8").read()
    lines = f.split("\n")
    return lines

def formatHM(txt):
    temp = str(txt)[1:-1]
    temp = temp.split(",")
    for i in temp:
        i = i.strip()
        i = i.replace("'", "")
        nev = i.split(":")[0]
        magassag = i.split(":")[1]
        print(f"\t{nev} -{magassag} db")


def feladat4(list):
    temp = 0
    for i in list:
        temp += i.magassag
    return temp/len(list)

def feladat5(list):
    for i in range(len(list)-1):
        for j in range(i+1, len(list)):
            if list[i].magassag < list[j].magassag:
                csere = list[i]
                list[i] = list[j]
                list[j] = csere
    
    print(f"\tNév: {list[0].csucs_nev}\n\tHegység: {list[0].hegyseg_nev}\n\tMagasság: {list[0].magassag} m")

def feladat6(list, num):
    for i in list:
        if i.hegyseg_nev == "Börzsöny" and i.magassag > num:
            return f"van {num}m-nél magasabb hegycsúcs a Börzsönyben"
    return f"nincs {num}m-nél magasabb hegycsúcs a Börzsönyben"

def feladat7(list):
    temp = 0
    for i in list:
        if i.magassag*3.280839895 > 3000:
            temp += 1
    return temp

def feladat8(list):
    hegy_map = dict()
    for i in list:
        if i.hegyseg_nev in hegy_map:
            hegy_map[i.hegyseg_nev] += 1
        else:
            hegy_map[i.hegyseg_nev] = 1
    formatHM(hegy_map)

def feladat9(list):
    temp = []
    fejlec = "hegycsúcs neve;Magasság láb"
    for i in list:
        if i.hegyseg_nev == "Bükk-vidék":
            temp.append(f"{i.csucs_nev};{round(i.magassag*3.280839895, 1)}\n")
    f = open("bukk-videk.txt", "w", encoding="UTF8")
    for i in temp:
        f.write(i)
    f.close()


def main():
    main_list = makingObjects()
    print(f"3. feladat: Hegycsúcsok száma: {len(main_list)} db")
    print(f"4. feladat: Hegycsúcsok átlag magassága: {feladat4(main_list)} m")
    print(f"5. feladat: A legmagasabb hegycsúcs adatai:")
    feladat5(main_list)
    user_magassag = int(input(f"6. feladat: Kérek egy magasságot:"))
    print(feladat6(main_list, user_magassag))
    print(f"7. feladat: 3000 lábnál magasabb hegycsúcsok száma: {feladat7(main_list)}")
    print(f"8. feladat: Hegység statisztika:")
    feladat8(main_list)
    feladat9(main_list)
main()


