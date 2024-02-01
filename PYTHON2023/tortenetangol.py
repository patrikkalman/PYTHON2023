tortenet=[
    [
        1,  #történetszál sorszáma
        " ============================================================ \nEgy börtönben ébredtem fel mert cigány vagyok, de az egyik cigany haverom\nbecsempészett egy dobozt tele cuccokkal mit kéne használnom ahhoz hogy kiszabaduljak?\n ============================================================",#történetszál
        ["teleportáló","fúró", "lufi"],#választható cselekvések
        [2,3,4] #cselekvés sorszáma, hova ugorjon
    ],
    [
        2,  #történetszál sorszáma
        " ============================================================ \nKijutottál, de egy kocsi elé teleportáltál és elbaszott \n ============================================================",#történetszál
        ["vissza"],#választható cselekvések
        [1] #cselekvés sorszáma, hova ugorjon
    ],
 [
        4,  #történetszál sorszáma
        " ============================================================ \nMi a f*szt kezdesz egy lufival te barom állat?\n ============================================================",#történetszál
        ["vissza"],#választható cselekvések
        [1] #cselekvés sorszáma, hova ugorjon

    ],
     [
        3,  #történetszál sorszáma
        " ============================================================ \nLefurtad magad egy raktárba, az ajtó be van zárva de találsz egy két tárgyat a polcon, melyiket használod az ajtó kinyitásához?\n ============================================================",#történetszál
        ["feszítővas", "balta"],#választható cselekvések
        [5,6] #cselekvés sorszáma, hova ugorjon
    ],
     [
        6,  #történetszál sorszáma
        " ============================================================ \nTúl hangos voltál, az őrök meghalloták, meglátták a bőrszíned és lelőttek.\n ============================================================",#történetszál
        ["vissza"],#választható cselekvések
        [3] #cselekvés sorszáma, hova ugorjon
    ],
    [
        5,  #történetszál sorszáma
        " ============================================================ \n Felfeszíted az ajtót a feszítővassal, de szembe találod magad 1 őrrel? \n ============================================================",#történetszál
        ["elciganykodsz mellette", "harcolsz"],#választható cselekvése
        [7,8] #cselekvés sorszáma, hova ugorjon
    ],
    [
        8,  #történetszál sorszáma
        " ============================================================ \n Kiderült hogy fegyver van nála, azt lelőtt a villámba \n ============================================================",#történetszál
        ["vissza"],#választható cselekvése
        [5] #cselekvés sorszáma, hova ugorjon
    ],
    [
        7,  #történetszál sorszáma
        " ============================================================ \n Észrevétlenül elmész mellette de meglát egy cellából egy rab és be akar köpni, mit kéne tenned hogy kielégítsd? \n ============================================================",#történetszál
        ["Kiszabadítod", "elmész"],#választható cselekvése
        [9,10] #cselekvés sorszáma, hova ugorjon
    ],
     [
        9,  #történetszál sorszáma
        " ============================================================ \n Megpróbálod kiszbadítani de nem sikerül \n ============================================================",#történetszál
        ["benyulsz a cellába és megfojtod","elmész"],#választható cselekvése
        [11,10] #cselekvés sorszáma, hova ugorjon
    ],
     [
        10,  #történetszál sorszáma
        " ============================================================ \n Elkezd ordibálni az őröknek és elkapnak \n ============================================================",#történetszál
        ["vissza"],#választható cselekvése
        [7] #cselekvés sorszáma, hova ugorjon
    ],
     [
        11,  #történetszál sorszáma
        " ============================================================ \n Megfulladt de sietned kell mert az őrők meglátják \n ============================================================",#történetszál
        ["elveszed a cuccait", "keresed tovabb a kijaratot"],#választható cselekvése
        [12,13] #cselekvés sorszáma, hova ugorjon
    ],
    [
        12,  #történetszál sorszáma
        " ============================================================ \n Nem találsz nála semmit, és elkaptak \n ============================================================",#történetszál
        ["vissza"],#választható cselekvése
        [11] #cselekvés sorszáma, hova ugorjon
    ],
    [
        13,  #történetszál sorszáma
        " ============================================================ \n  megtalálod a kijáratot de be van zárva, látsz egy vonalas telefont \n ============================================================",#történetszál
        ["felhívod a cigány haverod", "felhívod a kedves édesanyádat","felhívod Gáspár Lacit"],#választható cselekvése
        [14,15,16] #cselekvés sorszáma, hova ugorjon
    ],
    [
        14,  #történetszál sorszáma
        " ============================================================ \n rájössz hogy a cigany is börtönbe van \n ============================================================",#történetszál
        ["vissza"],#választható cselekvése
        [13] #cselekvés sorszáma, hova ugorjon
    ],
 ]
