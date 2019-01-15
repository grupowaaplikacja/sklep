import sqlite3

conn = sqlite3.connect('baza.db')
c = conn.cursor()

c.execute('DROP TABLE IF EXISTS konta')
c.execute('''CREATE TABLE IF NOT EXISTS konta (id INTEGER PRIMARY KEY ASC, imie TEXT, nazwisko TEXT, email TEXT, haslo TEXT, telefon TEXT, miasto1 TEXT, kod_pocztowy1 TEXT, adres1 TEXT, miasto2 TEXT, kod_pocztowy2 TEXT, adres2 TEXT, rola CHAR)''')
c.execute("INSERT INTO konta VALUES(NULL, 'Admin', 'Admin', 'admin@toysworld.pl', 'password', '99999999', 'Lublin', '20-606', 'Zana 16','Lublin', '20-606', 'Zana 16', 'A' )")
c.execute("INSERT INTO konta VALUES(NULL, 'Jan', 'Nowak', 'grupowaaplikacja@wp.pl', 'haslo12345', '123 456 789', 'Lublin', '20-700', 'Pana Balcera 10/2','Lublin', '20-700', 'Pana Balcera 10/2', 'K' )")

c.execute('DROP TABLE IF EXISTS produkty')
c.execute('''CREATE TABLE IF NOT EXISTS produkty (id INTEGER PRIMARY KEY ASC, nazwa TEXT, opis TEXT, kategoria TEXT, cena_zl INTEGER, cena_gr INTEGER, il_sztuk INTEGER, kod TEXT, min_wiek INTEGER)''')
c.execute("INSERT INTO produkty VALUES(NULL,'Umpa Lumpa', 'Super miękki i milutki, wykonane z bardzo wysokiej jakości materiału, idealny do przytulania. Prać ręcznie, nie stosować wybielaczy, nie czyścić chemicznie, nie prasować, nie suszyć w suszarce bębnowej.Produkt wykonany z najwyszej jakości surowców wg norm EU.', 'pluszaki_xxl', 199, 99, 12, 'pxxl001', 3)")
c.execute("INSERT INTO produkty VALUES(NULL,'Hannibal Lecter', 'Super miękki i milutki, wykonane z bardzo wysokiej jakości materiału, idealny do przytulania. Prać ręcznie, nie stosować wybielaczy, nie czyścić chemicznie, nie prasować, nie suszyć w suszarce bębnowej. Produkt wykonany z najwyszej jakości surowców wg norm EU.', 'pluszaki_xxl', 55, 99, 3, 'pxxl002', 3)")
c.execute("INSERT INTO produkty VALUES(NULL,'Super Miś', 'Super miękki i milutki, wykonane z bardzo wysokiej jakości materiału, idealny do przytulania. Prać ręcznie, nie stosować wybielaczy, nie czyścić chemicznie, nie prasować, nie suszyć w suszarce bębnowej. Produkt wykonany z najwyszej jakości surowców wg norm EU.', 'pluszaki_xxl', 321, 99, 30, 'pxxl003', 3)")
c.execute("INSERT INTO produkty VALUES(NULL,'Pan Jan', 'Super miękki i milutki, wykonane z bardzo wysokiej jakości materiału, idealny do przytulania. Prać ręcznie, nie stosować wybielaczy, nie czyścić chemicznie, nie prasować, nie suszyć w suszarce bębnowej. Produkt wykonany z najwyszej jakości surowców wg norm EU.', 'pluszaki_xxl', 123, 99, 10, 'pxxl004', 3)")
c.execute("INSERT INTO produkty VALUES(NULL,'Joey Black', 'Super miękki i milutki, wykonane z bardzo wysokiej jakości materiału, idealny do przytulania. Prać ręcznie, nie stosować wybielaczy, nie czyścić chemicznie, nie prasować, nie suszyć w suszarce bębnowej. Produkt wykonany z najwyszej jakości surowców wg norm EU.', 'pluszaki_xxl', 1, 99, 6, 'pxxl005', 3)")
c.execute("INSERT INTO produkty VALUES(NULL,'Gruby Tony', 'Super miękki i milutki, wykonane z bardzo wysokiej jakości materiału, idealny do przytulania. Prać ręcznie, nie stosować wybielaczy, nie czyścić chemicznie, nie prasować, nie suszyć w suszarce bębnowej. Produkt wykonany z najwyszej jakości surowców wg norm EU.', 'pluszaki_xxl', 932, 99, 3, 'pxxl006', 3)")
c.execute("INSERT INTO produkty VALUES(NULL,'Johny Wiertara', 'Super miękki i milutki, wykonane z bardzo wysokiej jakości materiału, idealny do przytulania. Prać ręcznie, nie stosować wybielaczy, nie czyścić chemicznie, nie prasować, nie suszyć w suszarce bębnowej. Produkt wykonany z najwyszej jakości surowców wg norm EU.', 'pluszaki_xxl', 95, 99, 40, 'pxxl007', 3)")
c.execute("INSERT INTO produkty VALUES(NULL,'Vito Corelone', 'Super miękki i milutki, wykonane z bardzo wysokiej jakości materiału, idealny do przytulania. Prać ręcznie, nie stosować wybielaczy, nie czyścić chemicznie, nie prasować, nie suszyć w suszarce bębnowej. Produkt wykonany z najwyszej jakości surowców wg norm EU.', 'pluszaki_xxl', 90, 99, 3, 'pxxl008', 3)")
c.execute("INSERT INTO produkty VALUES(NULL,'Michael Corleone', 'Super miękki i milutki, wykonane z bardzo wysokiej jakości materiału, idealny do przytulania. Prać ręcznie, nie stosować wybielaczy, nie czyścić chemicznie, nie prasować, nie suszyć w suszarce bębnowej. Produkt wykonany z najwyszej jakości surowców wg norm EU.', 'pluszaki_xxl', 11, 99, 30, 'pxxl009', 3)")
c.execute("INSERT INTO produkty VALUES(NULL,'Goodkat', 'Super miękki i milutki, wykonane z bardzo wysokiej jakości materiału, idealny do przytulania. Prać ręcznie, nie stosować wybielaczy, nie czyścić chemicznie, nie prasować, nie suszyć w suszarce bębnowej. Produkt wykonany z najwyszej jakości surowców wg norm EU.', 'pluszaki_xxl', 56, 99, 3, 'pxxl010', 3)")
c.execute("INSERT INTO produkty VALUES(NULL,'Diego de la Vega', 'Super miękki i milutki, wykonane z bardzo wysokiej jakości materiału, idealny do przytulania. Prać ręcznie, nie stosować wybielaczy, nie czyścić chemicznie, nie prasować, nie suszyć w suszarce bębnowej. Produkt wykonany z najwyszej jakości surowców wg norm EU.', 'pluszaki_xxl', 99, 99, 100, 'pxxl011', 3)")
c.execute("INSERT INTO produkty VALUES(NULL,'Alejandro', 'Super miękki i milutki, wykonane z bardzo wysokiej jakości materiału, idealny do przytulania. Prać ręcznie, nie stosować wybielaczy, nie czyścić chemicznie, nie prasować, nie suszyć w suszarce bębnowej. Produkt wykonany z najwyszej jakości surowców wg norm EU.', 'pluszaki_xxl', 111, 99, 3, 'pxxl012', 3)")
c.execute("INSERT INTO produkty VALUES(NULL,'Mufasa', 'Super miękki i milutki, wykonane z bardzo wysokiej jakości materiału, idealny do przytulania. Prać ręcznie, nie stosować wybielaczy, nie czyścić chemicznie, nie prasować, nie suszyć w suszarce bębnowej. Produkt wykonany z najwyszej jakości surowców wg norm EU.', 'pluszaki_xxl', 91, 99, 34, 'pxxl013', 3)")
c.execute("INSERT INTO produkty VALUES(NULL,'Puchatek', 'Super miękki i milutki, wykonane z bardzo wysokiej jakości materiału, idealny do przytulania. Prać ręcznie, nie stosować wybielaczy, nie czyścić chemicznie, nie prasować, nie suszyć w suszarce bębnowej. Produkt wykonany z najwyszej jakości surowców wg norm EU.', 'pluszaki_xxl', 132, 99, 43, 'pxxl014', 3)")
c.execute("INSERT INTO produkty VALUES(NULL,'Łysol', 'Super miękki i milutki, wykonane z bardzo wysokiej jakości materiału, idealny do przytulania. Prać ręcznie, nie stosować wybielaczy, nie czyścić chemicznie, nie prasować, nie suszyć w suszarce bębnowej. Produkt wykonany z najwyszej jakości surowców wg norm EU.', 'pluszaki_xxl', 89, 89, 3, 'pxxl015', 3)")
c.execute("INSERT INTO produkty VALUES(NULL,'Rysiek', 'Super miękki i milutki, wykonane z bardzo wysokiej jakości materiału, idealny do przytulania. Prać ręcznie, nie stosować wybielaczy, nie czyścić chemicznie, nie prasować, nie suszyć w suszarce bębnowej. Produkt wykonany z najwyszej jakości surowców wg norm EU.', 'pluszaki_xxl', 799, 99, 100, 'pxxl016', 3)")


c.execute('DROP TABLE IF EXISTS subskrybenci')
c.execute('''CREATE TABLE IF NOT EXISTS subskrybenci (id INTEGER PRIMARY KEY ASC, email TEXT)''')

c.execute('DROP TABLE IF EXISTS zapytania')
c.execute('''CREATE TABLE IF NOT EXISTS zapytania (id INTEGER PRIMARY KEY ASC, imie TEXT, temat TEXT, email TEXT, wiadomosc TEXT)''')

conn.commit()
conn.close()

