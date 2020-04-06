from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('oAutorze.html')

@app.route('/product_list')
def product_list():
    return render_template('ListaProduktow.html')

@app.route('/extraction')
def extraction():
    return render_template('Ekstrakcja.html')

@app.route('/singleProduct')
def single_product():
    return render_template('PojedynczyProdukt.html')


if __name__ == '__main__':
    app.run(debug=True)
