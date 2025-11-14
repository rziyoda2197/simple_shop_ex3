from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///magazin.db'

db = SQLAlchemy(app)

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=True)
    price = db.Column(db.Float, default=0)
    characteristic = db.Column(db.Text(), nullable=True)
    memory = db.Column(db.Integer, nullable=True)
    protsessor = db.Column(db.Text)
    display = db.Column(db.Text)
    kamera = db.Column(db.Text)
    brand = db.Column(db.String(255))
    description = db.Column(db.Text)
    image = db.Column(db.Text)

@app.route('/')
def index():
    product = Product.query.all()
    return render_template('index.html', product=product)


@app.route('/product_detail')
def product_detail():
    product = Product.query.all()
    return render_template('product_detail.html', product=product)


@app.route('/product')
def products():
    products = Product.query.all()
    return render_template('products.html', products=products)


@app.route('/add_product')
def add_product():
    return render_template('add-product.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    