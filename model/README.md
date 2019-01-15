# Baza danych sklepu internetowego

# Ważne

  - Baza się kompiluje, ale nie jest jeszcze w 100% sprawna. Wymaga ona jeszcze kilku poprawek, których na tym etapie nie jest do końca w stanie zrobić
  - Póki co baza dalej działa na SQLite, więc plik database.db jest wymagany do działania aplikacji

# Dokumentacja

Tutaj znajdują się wszystkie informacje dotyczące kompilacji bazy oraz wszystkich zaimplementowanych, ***działających*** metod:
> Przed jakimikolwiek operacjami na bazie: należy wpierw skompilować pliki database.db oraz db_generator.db


# Zaimplementowane klasy oraz metody:
### User: konstruktor 
>***User(<string> email, <string> hasło, <string> imię, <string> nazwisko, <string> numer telefonu, <Integer> Rola/Ranga, <String Default = Null> pierwszy adres, <String Default = Null> drugi adres )***
### Product: konstruktor:
>***Product(<string> nazwa, <string max 3 znaki> kategoria, <Integer> ilość, <Float> Cena za sztukę, <String Default = Null> Opis)***
### Order: konstruktor:
> ***Order(<Integer> Id klienta, <String max 3 znaki> Rodzaj Dostawy, <Char> Rodzaj płatności, <Typ Daty Pythona> Data zamówienia, <String max 15> Status zamówienia)***
### Order_detailed: konstruktor:
> ***Order_detailed(<Integer> Id produktu, <Integer> Liczba sztuk, <Integer Default = Null> Id zamówienia)***
### Delivery: konstruktor
> ***Delivery(<String max 3> Id modelu przesyłki, <String max 20> Pełna nazwa modelu przesyłki, <Float> koszt wysyłki)***
### Newsletter
> ***Newsletter(<String> Email)***
## Metody i operacje na bazie:
> Przed jakimikolwiek operacjami należy dokonać importu: ***import db from database***
### Insert:
> db.session.add(konstruktor bądź zmienna przechowujące informacje o obiekcie danej klasy)
>db.session.commit()
### Select:
> db.query.all() - wyświetla całą tabelę
> db.query.filter_by(nazwa_pola='wartość') - select z warunkiem where - zwraca tablicę, w związku z czym warto używać tutaj metod .first(), .get(numer_rekordu) - np. db.query.filter_by(nazwa_pola='wartość').first()
### Delete:
> db.session.delete(nazwa_zmiennej)
db.session.commit()