from database import *
db.session.add(User('admin@toysworld.pl','password','Admin','Admin','999999999',1,'Lublin, 20-606, Zana 16','Lublin, 20-606, Zana 16'))
db.session.add(User('grupowaaplikacja@wp','haslo12345','Jan','Nowak','123 456 789',0,'Lublin, 20-700, Pana Balcera 10/2', 'Lublin, 20-700, Pana Balcera 10/2'))
db.session.commit()

db.session.add(Product('Umpa Lumpa','pluszaki_xxl',12, 199.99,'Super miękki i milutki, wykonane z bardzo wysokiej jakości materiału, idealny do przytulania. Prać ręcznie, nie stosować wybielaczy, nie czyścić chemicznie, nie prasować, nie suszyć w suszarce bębnowej.Produkt wykonany z najwyszej jakości surowców wg norm EU.'))
db.session.add(Product('Hannibal Lecter','pluszaki_xxl',30, 321.99,'Super miękki i milutki, wykonane z bardzo wysokiej jakości materiału, idealny do przytulania. Prać ręcznie, nie stosować wybielaczy, nie czyścić chemicznie, nie prasować, nie suszyć w suszarce bębnowej.Produkt wykonany z najwyszej jakości surowców wg norm EU.'))

db.session.add(Product('Super Miś','pluszaki_xxl',10, 123.99,'Super miękki i milutki, wykonane z bardzo wysokiej jakości materiału, idealny do przytulania. Prać ręcznie, nie stosować wybielaczy, nie czyścić chemicznie, nie prasować, nie suszyć w suszarce bębnowej.Produkt wykonany z najwyszej jakości surowców wg norm EU.'))
db.session.add(Product('Pan Jan','pluszaki_xxl',6, 1.99,'Super miękki i milutki, wykonane z bardzo wysokiej jakości materiału, idealny do przytulania. Prać ręcznie, nie stosować wybielaczy, nie czyścić chemicznie, nie prasować, nie suszyć w suszarce bębnowej.Produkt wykonany z najwyszej jakości surowców wg norm EU.'))
db.session.add(Product('Joey Black','pluszaki_xxl',3, 932.99,'Super miękki i milutki, wykonane z bardzo wysokiej jakości materiału, idealny do przytulania. Prać ręcznie, nie stosować wybielaczy, nie czyścić chemicznie, nie prasować, nie suszyć w suszarce bębnowej.Produkt wykonany z najwyszej jakości surowców wg norm EU.'))
db.session.add(Product('Gruby Tony','pluszaki_xxl',40, 95.99,'Super miękki i milutki, wykonane z bardzo wysokiej jakości materiału, idealny do przytulania. Prać ręcznie, nie stosować wybielaczy, nie czyścić chemicznie, nie prasować, nie suszyć w suszarce bębnowej.Produkt wykonany z najwyszej jakości surowców wg norm EU.'))
db.session.add(Product('John Wiertara','pluszaki_xxl',3, 90.99,'Super miękki i milutki, wykonane z bardzo wysokiej jakości materiału, idealny do przytulania. Prać ręcznie, nie stosować wybielaczy, nie czyścić chemicznie, nie prasować, nie suszyć w suszarce bębnowej.Produkt wykonany z najwyszej jakości surowców wg norm EU.'))
db.session.add(Product('Vito Corelone','pluszaki_xxl',30, 11.99,'Super miękki i milutki, wykonane z bardzo wysokiej jakości materiału, idealny do przytulania. Prać ręcznie, nie stosować wybielaczy, nie czyścić chemicznie, nie prasować, nie suszyć w suszarce bębnowej.Produkt wykonany z najwyszej jakości surowców wg norm EU.'))
db.session.add(Product('Michael Corleone','pluszaki_xxl',3, 56.99,'Super miękki i milutki, wykonane z bardzo wysokiej jakości materiału, idealny do przytulania. Prać ręcznie, nie stosować wybielaczy, nie czyścić chemicznie, nie prasować, nie suszyć w suszarce bębnowej.Produkt wykonany z najwyszej jakości surowców wg norm EU.'))
db.session.add(Product('Goodkat','pluszaki_xxl',100, 99.99,'Super miękki i milutki, wykonane z bardzo wysokiej jakości materiału, idealny do przytulania. Prać ręcznie, nie stosować wybielaczy, nie czyścić chemicznie, nie prasować, nie suszyć w suszarce bębnowej.Produkt wykonany z najwyszej jakości surowców wg norm EU.'))
db.session.add(Product('Diego de la Vega','pluszaki_xxl',3, 111.99,'Super miękki i milutki, wykonane z bardzo wysokiej jakości materiału, idealny do przytulania. Prać ręcznie, nie stosować wybielaczy, nie czyścić chemicznie, nie prasować, nie suszyć w suszarce bębnowej.Produkt wykonany z najwyszej jakości surowców wg norm EU.'))
db.session.add(Product('Alejandro','pluszaki_xxl',34, 91.99,'Super miękki i milutki, wykonane z bardzo wysokiej jakości materiału, idealny do przytulania. Prać ręcznie, nie stosować wybielaczy, nie czyścić chemicznie, nie prasować, nie suszyć w suszarce bębnowej.Produkt wykonany z najwyszej jakości surowców wg norm EU.'))
db.session.add(Product('Mufasa','pluszaki_xxl',43, 132.99,'Super miękki i milutki, wykonane z bardzo wysokiej jakości materiału, idealny do przytulania. Prać ręcznie, nie stosować wybielaczy, nie czyścić chemicznie, nie prasować, nie suszyć w suszarce bębnowej.Produkt wykonany z najwyszej jakości surowców wg norm EU.'))
db.session.add(Product('Puchatek','pluszaki_xxl',3, 89.99,'Super miękki i milutki, wykonane z bardzo wysokiej jakości materiału, idealny do przytulania. Prać ręcznie, nie stosować wybielaczy, nie czyścić chemicznie, nie prasować, nie suszyć w suszarce bębnowej.Produkt wykonany z najwyszej jakości surowców wg norm EU.'))
db.session.add(Product('Łysol','pluszaki_xxl',12, 199.99,'Super miękki i milutki, wykonane z bardzo wysokiej jakości materiału, idealny do przytulania. Prać ręcznie, nie stosować wybielaczy, nie czyścić chemicznie, nie prasować, nie suszyć w suszarce bębnowej.Produkt wykonany z najwyszej jakości surowców wg norm EU.'))
db.session.add(Product('Rysiek','pluszaki_xxl',3, 799.99,'Super miękki i milutki, wykonane z bardzo wysokiej jakości materiału, idealny do przytulania. Prać ręcznie, nie stosować wybielaczy, nie czyścić chemicznie, nie prasować, nie suszyć w suszarce bębnowej.Produkt wykonany z najwyszej jakości surowców wg norm EU.'))



#c.execute('DROP TABLE IF EXISTS produkty')
#c.execute('''CREATE TABLE IF NOT EXISTS produkty (id INTEGER PRIMARY KEY ASC, nazwa TEXT, opis TEXT, kategoria TEXT, cena_zl INTEGER, cena_gr INTEGER, il_sztuk INTEGER, kod TEXT, min_wiek INTEGER)''')
#c.execute("INSERT INTO produkty VALUES(NULL,'Hannibal Lecter', 'Super miękki i milutki, wykonane z bardzo wysokiej jakości materiału, idealny do przytulania. Prać ręcznie, nie stosować wybielaczy, nie czyścić chemicznie, nie prasować, nie suszyć w suszarce bębnowej. Produkt wykonany z najwyszej jakości surowców wg norm EU.', 'pluszaki_xxl', 55, 99, 3, 'pxxl002', 3)")
#c.execute("INSERT INTO produkty VALUES(NULL,'Super Miś', 'Super miękki i milutki, wykonane z bardzo wysokiej jakości materiału, idealny do przytulania. Prać ręcznie, nie stosować wybielaczy, nie czyścić chemicznie, nie prasować, nie suszyć w suszarce bębnowej. Produkt wykonany z najwyszej jakości surowców wg norm EU.', 'pluszaki_xxl', 321, 99, 30, 'pxxl003', 3)")
#c.execute("INSERT INTO produkty VALUES(NULL,'Pan Jan', 'Super miękki i milutki, wykonane z bardzo wysokiej jakości materiału, idealny do przytulania. Prać ręcznie, nie stosować wybielaczy, nie czyścić chemicznie, nie prasować, nie suszyć w suszarce bębnowej. Produkt wykonany z najwyszej jakości surowców wg norm EU.', 'pluszaki_xxl', 123, 99, 10, 'pxxl004', 3)")
#c.execute("INSERT INTO produkty VALUES(NULL,'Joey Black', 'Super miękki i milutki, wykonane z bardzo wysokiej jakości materiału, idealny do przytulania. Prać ręcznie, nie stosować wybielaczy, nie czyścić chemicznie, nie prasować, nie suszyć w suszarce bębnowej. Produkt wykonany z najwyszej jakości surowców wg norm EU.', 'pluszaki_xxl', 1, 99, 6, 'pxxl005', 3)")
#c.execute("INSERT INTO produkty VALUES(NULL,'Gruby Tony', 'Super miękki i milutki, wykonane z bardzo wysokiej jakości materiału, idealny do przytulania. Prać ręcznie, nie stosować wybielaczy, nie czyścić chemicznie, nie prasować, nie suszyć w suszarce bębnowej. Produkt wykonany z najwyszej jakości surowców wg norm EU.', 'pluszaki_xxl', 932, 99, 3, 'pxxl006', 3)")
#c.execute("INSERT INTO produkty VALUES(NULL,'Johny Wiertara', 'Super miękki i milutki, wykonane z bardzo wysokiej jakości materiału, idealny do przytulania. Prać ręcznie, nie stosować wybielaczy, nie czyścić chemicznie, nie prasować, nie suszyć w suszarce bębnowej. Produkt wykonany z najwyszej jakości surowców wg norm EU.', 'pluszaki_xxl', 95, 99, 40, 'pxxl007', 3)")
#c.execute("INSERT INTO produkty VALUES(NULL,'Vito Corelone', 'Super miękki i milutki, wykonane z bardzo wysokiej jakości materiału, idealny do przytulania. Prać ręcznie, nie stosować wybielaczy, nie czyścić chemicznie, nie prasować, nie suszyć w suszarce bębnowej. Produkt wykonany z najwyszej jakości surowców wg norm EU.', 'pluszaki_xxl', 90, 99, 3, 'pxxl008', 3)")
#c.execute("INSERT INTO produkty VALUES(NULL,'Michael Corleone', 'Super miękki i milutki, wykonane z bardzo wysokiej jakości materiału, idealny do przytulania. Prać ręcznie, nie stosować wybielaczy, nie czyścić chemicznie, nie prasować, nie suszyć w suszarce bębnowej. Produkt wykonany z najwyszej jakości surowców wg norm EU.', 'pluszaki_xxl', 11, 99, 30, 'pxxl009', 3)")
#c.execute("INSERT INTO produkty VALUES(NULL,'Goodkat', 'Super miękki i milutki, wykonane z bardzo wysokiej jakości materiału, idealny do przytulania. Prać ręcznie, nie stosować wybielaczy, nie czyścić chemicznie, nie prasować, nie suszyć w suszarce bębnowej. Produkt wykonany z najwyszej jakości surowców wg norm EU.', 'pluszaki_xxl', 56, 99, 3, 'pxxl010', 3)")
#c.execute("INSERT INTO produkty VALUES(NULL,'Diego de la Vega', 'Super miękki i milutki, wykonane z bardzo wysokiej jakości materiału, idealny do przytulania. Prać ręcznie, nie stosować wybielaczy, nie czyścić chemicznie, nie prasować, nie suszyć w suszarce bębnowej. Produkt wykonany z najwyszej jakości surowców wg norm EU.', 'pluszaki_xxl', 99, 99, 100, 'pxxl011', 3)")
#c.execute("INSERT INTO produkty VALUES(NULL,'Alejandro', 'Super miękki i milutki, wykonane z bardzo wysokiej jakości materiału, idealny do przytulania. Prać ręcznie, nie stosować wybielaczy, nie czyścić chemicznie, nie prasować, nie suszyć w suszarce bębnowej. Produkt wykonany z najwyszej jakości surowców wg norm EU.', 'pluszaki_xxl', 111, 99, 3, 'pxxl012', 3)")
#c.execute("INSERT INTO produkty VALUES(NULL,'Mufasa', 'Super miękki i milutki, wykonane z bardzo wysokiej jakości materiału, idealny do przytulania. Prać ręcznie, nie stosować wybielaczy, nie czyścić chemicznie, nie prasować, nie suszyć w suszarce bębnowej. Produkt wykonany z najwyszej jakości surowców wg norm EU.', 'pluszaki_xxl', 91, 99, 34, 'pxxl013', 3)")
#c.execute("INSERT INTO produkty VALUES(NULL,'Puchatek', 'Super miękki i milutki, wykonane z bardzo wysokiej jakości materiału, idealny do przytulania. Prać ręcznie, nie stosować wybielaczy, nie czyścić chemicznie, nie prasować, nie suszyć w suszarce bębnowej. Produkt wykonany z najwyszej jakości surowców wg norm EU.', 'pluszaki_xxl', 132, 99, 43, 'pxxl014', 3)")
#c.execute("INSERT INTO produkty VALUES(NULL,'Łysol', 'Super miękki i milutki, wykonane z bardzo wysokiej jakości materiału, idealny do przytulania. Prać ręcznie, nie stosować wybielaczy, nie czyścić chemicznie, nie prasować, nie suszyć w suszarce bębnowej. Produkt wykonany z najwyszej jakości surowców wg norm EU.', 'pluszaki_xxl', 89, 89, 3, 'pxxl015', 3)")
#c.execute("INSERT INTO produkty VALUES(NULL,'Rysiek', 'Super miękki i milutki, wykonane z bardzo wysokiej jakości materiału, idealny do przytulania. Prać ręcznie, nie stosować wybielaczy, nie czyścić chemicznie, nie prasować, nie suszyć w suszarce bębnowej. Produkt wykonany z najwyszej jakości surowców wg norm EU.', 'pluszaki_xxl', 799, 99, 100, 'pxxl016', 3)")


db.session.commit()

