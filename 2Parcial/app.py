from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__)

def cargar_productos():
    try:
        df = pd.read_csv('productos.csv')
        productos = df.to_dict(orient='records')
        return productos
    except FileNotFoundError:
        return [
            {"id": 1, "nombre": "Laptop", "precio": 1200},
            {"id": 2, "nombre": "Smartphone", "precio": 800},
            {"id": 3, "nombre": "Tablet", "precio": 500}
        ]

productos_lista = cargar_productos()

@app.route('/productos')
def productos():
    return jsonify(productos_lista)

@app.route('/')
def lista_productos():
    return render_template('lista_productos.html', productos=productos_lista)

@app.route('/productos/<int:id>')
def detalles_producto(id):
    producto = next((p for p in productos_lista if p['id'] == id), None)
    return render_template('detalles_producto.html', producto=producto)

if __name__ == '__main__':
    app.run(debug=True)