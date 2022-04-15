# Sozdat spisok (supermarket), sostoyashhij iz slovarej (tovary). Slovari dolzhny soderzhat kak minimum 5 polej
# (naprimer, nomer, naimenovanie, otdel prodazhi, ...). V spisok dobavit xotya by 10 slovarej.
# Konstrukciya vida:
# market = [{"id":123456, "product":"coca-cola 0.5", "department": "drinks", ...} , {...}, {...}, ...].
# Realizovat funkcii:
# – vyvoda informacii o vsex tovarax;
# – vyvoda informacii o tovare po vvedennomu s klaviatury nomeru;
# – vyvoda kolichestva tovarov, prodayushhixsya v opredelennom otdele;
# – obnovlenii vsej informacii o tovare po vvedennomu nomeru;
# – udalenii tovara po nomeru.
# Provesti testirovanie funkcij.


import traceback


def info():
    print("ID    | Tovar              | Kategoriya  | Cena  | Kolichestvo  ")
    for i in range(len(market)):
        print('{: <5}'.format(market[i]["id"]), end=" | ")
        print('{: <18}'.format(market[i]["product"]), end=" | ")
        print('{: <10}'.format(market[i]["department"]), end=" | ")
        print('{: <5}'.format(market[i]["cost"]), end=" | ")
        print('{: <5}'.format(market[i]["count"]))
    print(f"Vsego tovarov {len(market)}\n\n")


def infoById():
    i = -1
    id = int(input("Vvedite id: "))
    for j in range(len(market)):
        if market[j]["id"] == id:
            i = j
            break
    if i == -1:
        print(f"Oshibka! Tovar ne najden\n")
    else:
        print(f'\nID: {market[i]["id"]}\nNazvanie: {market[i]["product"]}\nKategoriya: {market[i]["department"]}\
              \nStoimost: {market[i]["cost"]}\nKolichestvo: {market[i]["count"]}\n\n')


def countByDepartment():
    counter = 0
    department = input("Vvedite nazvanie kategorii: ")
    for i in range(len(market)):
        counter += (1 if market[i]["department"] == department else 0)
    print(f"Kolichestvo tovarov v kategorii: {counter}\n")


def updateProduct():
    i = -1
    id = int(input("Vvedite id: "))
    for j in range(len(market)):
        if market[j]["id"] == id:
            i = j
            break
    if i == -1:
        print(f"Oshibka! Tovar ne najden\n")
    else:
        market[i]["id"] = input("Nomer tovara (id): ")
        market[i]["product"] = input("Nazvanie tovara: ")
        market[i]["department"] = input("Nazvanie kategorii: ")
        market[i]["cost"] = int(input("Stoimost: "))
        market[i]["count"] = input("Kolichestvo: ")


def deleteProduct():
    i = -1
    id = int(input("Vvedite id: "))
    for j in range(len(market)):
        if market[j]["id"] == id:
            i = j
            break
    if i == -1:
        print(f"Oshibka! Tovar ne najden\n")
    else:
        del market[i]
        print(f"Tovar udalyon\n\n")


def help():
    print("1 - Informaciya o tovarax\n2 - Informaciya o tovare po id\n3 - Kolichestvo tovarov po kategorii\
          \n4 - Izmenit tovar po nomeru\n5 - Udalenie tovara po nomeru\n6 - Vyxod")


market = [
    {"id": 1, "product": "Coca-cola 0.5", "department": "drinks", "cost": 60, "count": 10},
    {"id": 2, "product": "Coca-cola 1l litr", "department": "drinks", "cost": 100, "count": 10},
    {"id": 23, "product": "Sprite 0.5", "department": "drinks", "cost": 60, "count": 6},
    {"id": 34, "product": "Fanta 0.5", "department": "drinks", "cost": 60, "count": 20},
    {"id": 54, "product": "Took", "department": "snacks", "cost": 60, "count": 80},
    {"id": 76, "product": "Biscuits", "department": "snacks", "cost": 60, "count": 70},
    {"id": 124, "product": "Macaroni", "department": "snacks", "cost": 150, "count": 50},
    {"id": 156, "product": "Oreo", "department": "snacks", "cost": 50, "count": 25},
    {"id": 233, "product": "Brownie Cake", "department": "cakes", "cost": 650, "count": 3},
    {"id": 300, "product": "Cake \"Prague\"", "department": "cakes", "cost": 450, "count": 2},
]


#help()
# ex = int(input())
ex = 6
while ex != 6:
    if ex == 1:
        info()
    elif ex == 2:
        infoById()
    elif ex == 3:
        countByDepartment()
    elif ex == 4:
        updateProduct()
    elif ex == 5:
        deleteProduct()
    help()
    ex = int(input())
