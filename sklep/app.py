from flask import *
import datetime
import os
import sqlite3
from database.database import *
import uuid
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config.update(dict(
    SECRET_KEY='bardzosekretnawartosc',
    DATABASE=os.path.join(app.root_path, 'database/database.db'),
    SITE_NAME='TOYS WORLD'
))





		
# ////////////////////////////////////////	
# /////////////////SKLEP/////////////////
# //////////////////////////////////////	

@app.route('/')
def index():
	return render_template('index.html')
	
@app.route('/wyszukaj', methods=['POST'])	
def wyszukaj():
	nazwa = request.form['nazwa_szukana']
	kategoria = request.form['kategoria_szukana']
	if(kategoria == 'wszystkie'):
		produkty=Product.query.all()
	else:
		produkty=Product.query.filter_by(category=kategoria).all()
	ile = len(produkty)
	return render_template('wyniki_wyszukiwania.html', nazwa=nazwa, kategoria=kategoria, ile=ile, produkty=produkty)
	
@app.route('/katalog/<kategoria>')
def pokaz_kategorie(kategoria):
	if(kategoria == 'nowosci'):
		produkty=Product.query.order_by(id.desc()).all()
	else:
		produkty=Product.query.filter_by(category=kategoria).all()
	ile = len(produkty)
	kat = kategoria.replace('_', ' ').upper()
	return render_template('katalog.html', kategoria=kat, ile=ile, produkty=produkty)

@app.route('/produkt/<kod>')
def produkt(kod):
	t = (kod,)
	produkt = Product.query.filter_by(unique_id=t)
	return render_template('produkt.html', produkt=produkt)
	
@app.route('/koszyk')
def koszyk():
    return render_template('koszyk.html')
	
@app.route('/dodaj_subskrybenta', methods=['POST'])
def dodaj_subskrybenta():
	adres = request.form['adres_email_subskrybcji']
	db.session.add(Newsletter(adres))
	db.session.commit()
	return redirect(url_for('index'))

@app.route('/zapytanie', methods=['POST'])
def zapytanie():
	imie = request.form['imie_zapytania']
	email = request.form['email_zapytania']
	temat = request.form['temat_zapytania']
	wiadomosc = request.form['wiadomosc_zapytania']
	#db = get_db()
	#db.execute('INSERT INTO zapytania VALUES(null,?,?,?,?)', [imie, email, temat, wiadomosc])
	#db.commit();
	return redirect(url_for('index'))
	

	
# ////////////////////////////////////////	
# /////////////////KONTO/////////////////
# //////////////////////////////////////

@app.route('/login')
def login_page():
	if(session.get('zalogowany') == True):
		return redirect(url_for('konto'))
	return render_template('login_page.html')
	
@app.route('/logging', methods=['POST'])
def logging():
	email_podany = request.form['email']
	haslo_podane = request.form['haslo']
	konto =User.query.filter_by(email=email_podany).first()
	if(konto is not None):
		haslo = konto.password
		rola = konto.role
		if(haslo == haslo_podane):
			if(rola == '1'):
				session['admin_mode'] = True
				session['zalogowany'] = True
				return redirect(url_for('index'))
			session['zalogowany'] = True
			return redirect(url_for('index'))
	return render_template('login_page.html', error=True)
	
@app.route('/logging_out')
def logging_out():
	session.pop('zalogowany', None)
	session.pop('admin_mode', None)
	return redirect(url_for('login_page'))	

@app.route('/rejestracja')
def rejestracja():
	if(session.get('zalogowany') == True):
		return redirect(url_for('konto'))
	return render_template('rejestracja.html')
	
@app.route('/tworzenie_konta', methods=['POST'])
def tworzenie_konta():
	return redirect(url_for('konto'))
	
@app.route('/konto')
def konto():
	if(session.get('zalogowany') == True):
			return redirect(url_for('konto_dane'))
	return redirect(url_for('login_page'))

@app.route('/konto/zamowienia')
def konto_zamowienia():
	if(session.get('zalogowany') == True):
		return render_template('konto_zamowienia.html')
	return redirect(url_for('login_page'))
	
@app.route('/konto/zwroty')
def konto_zwroty():
	if(session.get('zalogowany') == True):
		return render_template('konto_zwroty.html')
	return redirect(url_for('login_page'))
	
@app.route('/konto/dane')
def konto_dane():
	if(session.get('zalogowany') == True):
		return render_template('konto_dane.html')
	return redirect(url_for('login_page'))
	
@app.route('/konto/dane_adresowe')
def konto_dane_adresowe():
	if(session.get('zalogowany') == True):
		return render_template('konto_dane_adresowe.html')
	return redirect(url_for('login_page'))

	
	
# ////////////////////////////////////////	
# /////////////////ADMIN/////////////////
# //////////////////////////////////////

@app.route('/admin')
def admin():
	if(session.get('admin_mode') != True):
		return redirect(url_for('index'))
	return redirect(url_for('admin_dodaj_produkt'))

@app.route('/admin/dodaj_produkt')
def admin_dodaj_produkt():
	if(session.get('admin_mode') != True):
		return redirect(url_for('index'))
	return render_template('admin_dodaj_produkt.html')

@app.route('/dodaj_produkt', methods=['POST'])
def dodaj_produkt():
	nazwa = request.form['nazwa']
	kategoria = request.form['kategoria']
	cena = request.form['cena']
	zl = cena[:-3]
	gr = cena[-2:]
	ilosc = request.form['ilosc']
	kod = request.form['kod']
	min_wiek = request.form['min_wiek']
	opis = request.form['opis']
	zdjecie = request.files['zdjecie']
	sciezka = 'static/images/'+kod+'.png'
	zdjecie.save(sciezka)
	db.session.add(Product(nazwa, kategoria, ilosc, cena, opis))
	db.session.commit()
	return redirect(url_for('admin_dodaj_produkt'))
	
@app.route('/admin/dodaj_administratora')
def admin_dodaj_administratora():
	if(session.get('admin_mode') != True):
		return redirect(url_for('index'))
	return render_template('admin_dodaj_administratora.html')

@app.route('/admin/lista_produktow')
def admin_lista_produktow():
	if(session.get('admin_mode') != True):
		return redirect(url_for('index'))
	lista=Product.query.all()
	return render_template('admin_lista_produktow.html', lista=lista)
	
@app.route('/admin/lista_klientow')
def admin_lista_klientow():
	if(session.get('admin_mode') != True):
		return redirect(url_for('index'))
	lista = User.query.filter_by(role=0)
	return render_template('admin_lista_klientow.html', lista=lista)

@app.route('/admin/zamowienia_biezace')
def admin_zamowienia_biezace():
	if(session.get('admin_mode') != True):
		return redirect(url_for('index'))
	return render_template('admin_zamowienia_biezace.html')
	
@app.route('/admin/historia_zamowien')
def admin_historia_zamowien():
	if(session.get('admin_mode') != True):
		return redirect(url_for('index'))
	return render_template('admin_historia_zamowien.html')
	
	
@app.route('/admin/raporty')
def admin_raporty():
	if(session.get('admin_mode') != True):
		return redirect(url_for('index'))
	return render_template('admin_raporty.html')
	
@app.route('/admin/ustaw_bestsellery')
def admin_ustaw_bestsellery():
	if(session.get('admin_mode') != True):
		return redirect(url_for('index'))
	return render_template('admin_ustaw_bestsellery.html')
	
@app.route('/admin/pytania_klientow')
def admin_pytania_klientow():
	if(session.get('admin_mode') != True):
		return redirect(url_for('index'))
	return render_template('admin_pytania_klientow.html')


	
# ////////////////////////////////////////	
# /////////////////NIC///////////////////
# //////////////////////////////////////
	
@app.route('/regulamin')
def regulamin():
    return render_template('regulamin.html')
	
@app.route('/info/o_nas')
def info_o_nas():
    return render_template('info_o_nas.html')
	
@app.route('/info/dostawa')
def info_dostawa():
	return render_template('info_dostawa.html')
	
@app.route('/info/platnosc')
def info_platnosc():
    return render_template('info_platnosc.html')
	
@app.route('/info/zwroty')
def info_zwroty():
    return render_template('info_zwroty.html')
	
@app.route('/info/pomoc')
def info_pomoc():
    return render_template('info_pomoc.html')
	
	
	
	
if __name__ == '__main__':
	app.run(host='0.0.0.0', port='34567')
	
	
	
	
	
	
	
	
	
	