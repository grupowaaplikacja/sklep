import os
from flask_sqlalchemy import SQLAlchemy
from flask import *
import uuid

project_dir = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///{}".format(os.path.join(project_dir,"database.db"))
db = SQLAlchemy(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique = True)
    password = db.Column(db.String(50))
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    phone = db.Column(db.String(50))
    role = db.Column(db.Integer)
    first_address = db.Column(db.String(100), nullable = True)
    second_address = db.Column(db.String(100), nullable = True)

    def __repr__(self):
        return '<User {}>'.format(self.email)
    
    def __init__(self,email,password,first_name,last_name,phone,role, first_address=None, second_address=None):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.role = role
        self.first_address = first_address
        self.second_address = second_address
		
class Product(db.Model):
	__tablename__ = 'product'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100))
	description = db.Column(db.String(100), nullable=True)
	category = db.Column(db.String(3))
	stock = db.Column(db.Integer)
	price_per_unit=db.Column(db.Float)
	unique_id=db.Column(db.Text)
	
	def __init__(self, name, category, stock, price_per_unit, description=None):
		self.name = name
		self.category = category
		self.stock = stock
		self.price_per_unit=price_per_unit
		self.description = description
	
class Order(db.Model):
	__tablename__='order'
	id=db.Column(db.Integer, primary_key=True)
	customer_id=db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
	delivery_type=db.Column(db.String(3), db.ForeignKey('delivery.id'), nullable=False)
	payment_type=db.Column(db.String(1))
	order_date=db.Column(db.Date)
	total_price=db.Column(db.Float)
	status=db.Column(db.String(15))
	order_details=db.relationship('Order_detailed', backref='order', lazy=True)
	unique_id=db.Column(db.Text)
	
	def __init__(self, customer_id, delivery_type, payment_type, order_date, status):
		self.customer_id=customer_id
		self.delivery_type=delivery_type
		self.payment_type=payment_type
		self.order_date=order_date
		self.status=status
		self.unique_id=str(uuid.uuid4())
	def set_price():
		total=0.0
		y=Order_detailed.query.filter_by(order_id=self.unique_id)
		for x in y:
			total+=x.price
		self.total_price=total+Delivery.query.filter_by(id=self.delivery_type).first().price
	
	
class Order_detailed(db.Model):
	__tablename__='order_detailed'
	unique_id=db.Column(db.Text, primary_key=True)
	order_id=db.Column(db.Integer, db.ForeignKey('order.id'))
	product_id=db.Column(db.Integer, db.ForeignKey('product.id'))
	quantity=db.Column(db.Integer, nullable=False)
	price=db.Column(db.Float)
	
	def __init__(self, product_id,quantity, order_id=None):
		self.unique_id=str(uuid.uuid4())
		self.product_id=product_id
		self.order_id=order_id
		self.quantity=quantity
		self.price=Product.query.filter_by(id=product_id).first().price_per_unit*quantity
		
class Delivery(db.Model):
	__tablename__='delivery'
	id=db.Column(db.String(3),primary_key=True)
	name=db.Column(db.String(20))
	price=db.Column(db.Float)
	
	def __init__(self, id, p_name, price):
		self.id=id
		self.name=p_name
		self.price=price

class Newsletter(db.Model):
	id=db.Column(db.Integer, primary_key=True)
	mail=db.Column(db.String(80))
    
	def __init__(self,mail):
		self.mail=mail
		

def products(product_list):
	list=[]
	for x in product_list:
		list.append(Order_detailed(x.id,x.quantity))
	return list
		
def ordering(user, product_list, del_type, pay_type, date, status='Złożone'):
	order=Order(user.id, del_type, pay_type, date, status)
	list=products(product_list)
	for x in list:
		x.order_id=order.unique_id
		db.session.add(x)
	order.set_price()
	db.session.add(order)
		
	
		
		
		
#Dodac tabele kategorie, dodac UUID dla Order oraz Product





