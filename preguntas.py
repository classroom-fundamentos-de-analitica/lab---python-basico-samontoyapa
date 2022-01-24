"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
import csv

from collections import OrderedDict

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    with open("data.csv", "r") as csv_file:
        csv_reader = csv.reader(
        csv_file,
        delimiter=" ",
        quotechar='"',
        )

        sum = 0
        for row in csv_reader:
            fila = row[0]
            sum = sum + int(fila[2])

    return sum

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """

    with open("data.csv", "r") as csv_file:
        csv_reader = csv.reader(
        csv_file,
        delimiter=" ",
        quotechar='"',
        )

        a = 0
        b = 0
        c = 0
        d = 0
        e = 0

        for row in csv_reader:
            fila = row[0]
            letter = fila[0]
            if letter == "A":
                a = a + 1
            elif letter == "B":
                b = b + 1
            elif letter == "C":
                c = c + 1
            elif letter == "D":
                d = d + 1
            elif letter == "E":
                e = e + 1
    return [("A", a),("B", b),("C", c ),("D", d),("E", e)]

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    with open("data.csv", "r") as csv_file:
        csv_reader = csv.reader(
        csv_file,
        delimiter=" ",
        quotechar='"',
        )

        a = 0
        b = 0
        c = 0
        d = 0
        e = 0

        for row in csv_reader:
            fila = row[0]
            letter = fila[0]
            if letter == "A":
                a = a + int(fila[2])
            elif letter == "B":
                b = b + int(fila[2])
            elif letter == "C":
                c = c + int(fila[2])
            elif letter == "D":
                d = d + int(fila[2])
            elif letter == "E":
                e = e + int(fila[2])

    return [("A", a),("B", b),("C", c ),("D", d),("E", e)]


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    with open("data.csv", "r") as csv_file:
        csv_reader = csv.reader(
        csv_file,
        delimiter=" ",
        quotechar='"',
        )

        a = 0
        b = 0
        c = 0
        d = 0
        e = 0
        f = 0
        g = 0
        h = 0
        i = 0
        j = 0
        k = 0
        l = 0

        for row in csv_reader:
            fila = row[0]
            date = fila[9:11]
            if date == "01":
                a = a + 1
            elif date == "02":
                b = b + 1
            elif date == "03":
                c = c + 1
            elif date == "04":
                d = d + 1
            elif date == "05":
                e = e + 1
            elif date == "06":
                f = f + 1
            elif date == "07":
                g = g + 1
            elif date == "08":
                h = h + 1
            elif date == "09":
                i = i + 1
            elif date == "10":
                j = j + 1
            elif date == "11":
                k = k + 1
            elif date == "12":
                l = l + 1

    return [("01", a),("02", b),("03", c ),("04", d),("05", e),("06", f),
            ("07", g),("08", h ),("09", i),("10", j),("11",k),("12",l)]

pregunta_04()

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    with open("data.csv", "r") as csv_file:
        csv_reader = csv.reader(
        csv_file,
        delimiter=" ",
        quotechar='"',
        )

        a = []
        b = []
        c = []
        d = []
        e = []

        for row in csv_reader:
            fila = row[0]
            letter = fila[0]
            if letter == "A":
                a.append(int(fila[2]))
            elif letter == "B":
                b.append(int(fila[2]))
            elif letter == "C":
                c.append(int(fila[2]))
            elif letter == "D":
                d.append(int(fila[2]))
            elif letter == "E":
                e.append(int(fila[2]))

    return [("A", max(a), min(a)),("B", max(b), min(b)),("C", max(c), min(c)),("D", max(d), min(d)),("E", max(e), min(e))]

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    with open("data.csv", "r") as csv_file:
        csv_reader = csv.reader(
        csv_file,
        delimiter="\t",
        quotechar='"',
        )
        a = []
        b = []
        c = []
        d = []
        e = []
        f = []
        g = []
        h = []
        i = []
        j = []
        for row in csv_reader:
            fila = row[4].split(',')
            
            for item in fila:
                parts =  item.split(':')
                if parts[0] == "aaa":
                    a.append(int(parts[1]))
                elif parts[0] == "bbb":
                    b.append(int(parts[1]))
                elif parts[0] == "ccc":
                    c.append(int(parts[1]))
                elif parts[0] == "ddd":
                    d.append(int(parts[1]))
                elif parts[0] == "eee":
                    e.append(int(parts[1]))
                elif parts[0] == "fff":
                    f.append(int(parts[1]))
                elif parts[0] == "ggg":
                    g.append(int(parts[1]))
                elif parts[0] == "hhh":
                    h.append(int(parts[1]))
                elif parts[0] == "iii":
                    i.append(int(parts[1]))
                elif parts[0] == "jjj":
                    j.append(int(parts[1]))

    return [("aaa", min(a), max(a)),("bbb", min(b), max(b)),("ccc", min(c), max(c)),("ddd", min(d), max(d)),("eee", min(e), max(e)),
    ("fff", min(f), max(f)),("ggg", min(g), max(g)),("hhh", min(h), max(h)),("iii", min(i), max(i)),("jjj", min(j), max(j))]

def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    with open("data.csv", "r") as csv_file:
        csv_reader = csv.reader(
        csv_file,
        delimiter="\t",
        quotechar='"',
        )
        f0 = []
        f1 = []
        f2 = []
        f3 = []
        f4 = []
        f5 = []
        f6 = []
        f7 = []
        f8 = []
        f9 = []
        
        for row in csv_reader:
            if  row[1] == "0":
                f0.append(row[0])
            elif row[1]  == "1":
                f1.append(row[0])
            elif row[1]  == "2":
                f2.append(row[0])
            elif row[1]  == "3":
                f3.append(row[0])
            elif row[1]  == "4":
                f4.append(row[0])
            elif row[1]  == "5":
                f5.append(row[0])
            elif row[1]  == "6":
                f6.append(row[0])
            elif row[1]  == "7":
                f7.append(row[0])
            elif row[1]  == "8":
                f8.append(row[0])
            elif row[1]  == "9":
                f9.append(row[0])


    return [(0, f0),(1,f1),(2,f2),(3,f3),(4,f4),(5, f5),(6, f6),(7, f7),(8, f8),(9, f9)]

def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    with open("data.csv", "r") as csv_file:
        csv_reader = csv.reader(
        csv_file,
        delimiter="\t",
        quotechar='"',
        )
        f0 = []
        f1 = []
        f2 = []
        f3 = []
        f4 = []
        f5 = []
        f6 = []
        f7 = []
        f8 = []
        f9 = []
        
        for row in csv_reader:
            if  row[1] == "0":
                f0.append(row[0])
            elif row[1]  == "1":
                f1.append(row[0])
            elif row[1]  == "2":
                f2.append(row[0])
            elif row[1]  == "3":
                f3.append(row[0])
            elif row[1]  == "4":
                f4.append(row[0])
            elif row[1]  == "5":
                f5.append(row[0])
            elif row[1]  == "6":
                f6.append(row[0])
            elif row[1]  == "7":
                f7.append(row[0])
            elif row[1]  == "8":
                f8.append(row[0])
            elif row[1]  == "9":
                f9.append(row[0])


    return [(0,  list(OrderedDict.fromkeys(sorted(f0)))),(1, list(OrderedDict.fromkeys(sorted(f1)))),(2, list(OrderedDict.fromkeys(sorted(f2)))),(3, list(OrderedDict.fromkeys(sorted(f3)))),(4, list(OrderedDict.fromkeys(sorted(f4)))),
            (5,  list(OrderedDict.fromkeys(sorted(f5)))),(6,  list(OrderedDict.fromkeys(sorted(f6)))),(7,  list(OrderedDict.fromkeys(sorted(f7)))),(8,  list(OrderedDict.fromkeys(sorted(f8)))),(9,  list(OrderedDict.fromkeys(sorted(f9))))]

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    with open("data.csv", "r") as csv_file:
        csv_reader = csv.reader(
        csv_file,
        delimiter="\t",
        quotechar='"',
        )
        a = 0
        b = 0
        c = 0
        d = 0
        e = 0
        f = 0
        g = 0
        h = 0
        i = 0
        j = 0
        for row in csv_reader:
            fila = row[4].split(',')
            
            for item in fila:
                parts =  item.split(':')
                if parts[0] == "aaa":
                    a = a + 1
                elif parts[0] == "bbb":
                    b = b + 1
                elif parts[0] == "ccc":
                    c = c + 1
                elif parts[0] == "ddd":
                    d = d + 1
                elif parts[0] == "eee":
                    e = e + 1
                elif parts[0] == "fff":
                    f = f + 1
                elif parts[0] == "ggg":
                    g = g + 1
                elif parts[0] == "hhh":
                    h = h + 1
                elif parts[0] == "iii":
                    i = i + 1
                elif parts[0] == "jjj":
                    j = j + 1

    return {"aaa": a, "bbb" : b, "ccc": c, "ddd": d, "eee": e ,
     "fff": f , "ggg": g , "hhh": h, "iii": i , "jjj": j }

def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    with open("data.csv", "r") as csv_file:
        csv_reader = csv.reader(
        csv_file,
        delimiter="\t",
        quotechar='"',
        )
        
        d = []
        for row in csv_reader:
            column4 = row[3].split(',')
            column5 = row[4].split(',')
            
            d.append((row[0], len(column4), len(column5)))
                

    return d

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    with open("data.csv", "r") as csv_file:
        csv_reader = csv.reader(
        csv_file,
        delimiter="\t",
        quotechar='"',
        )
        
        a = []
        b = []
        c = []
        d = []
        e = []
        f = []
        g = []

        for row in csv_reader:
            
            times = row[1]
            letters = row[3]
            for item in letters:
                if item == "a":
                    a.append(int(times))
                elif item == "b":
                    b.append(int(times))
                elif item == "c":
                    c.append(int(times))
                elif item == "d":
                    d.append(int(times))
                elif item == "e":
                    e.append(int(times))
                elif item == "f":
                    f.append(int(times))
                elif item == "g":
                    g.append(int(times))

                

        return {"a": sum(a), "b" : sum(b), "c": sum(c), "d": sum(d), "e": sum(e) ,
                "f": sum(f) , "g": sum(g)}

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    with open("data.csv", "r") as csv_file:
        csv_reader = csv.reader(
        csv_file,
        delimiter="\t",
        quotechar='"',
        )
        
        a = []
        b = []
        c = []
        d = []
        e = []

        for row in csv_reader:
            
            letter = row[0]
            column4 = row[4].split(',')

            list1 = []
            for item in column4:
                parts =  item.split(':')
                list1.append(int(parts[1]))

            if letter == "A":
                for i in list1:
                    a.append(i)
            elif letter == "B":
                for i in list1:
                    b.append(i)
            elif letter == "C":
                for i in list1:
                    c.append(i)
            elif letter == "D":
                for i in list1:
                    d.append(i)
            elif letter == "E":
                for i in list1:
                    e.append(i)      

        return {"A": sum(a), "B" : sum(b), "C": sum(c), "D": sum(d), "E": sum(e)}
