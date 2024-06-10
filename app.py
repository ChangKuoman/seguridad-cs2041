from flask import Flask, render_template, request
from config import *

app = Flask(__name__)
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        nombrEstudent = request.form['nombre']
        try:

            result =get_estudiante_by_Nombre(nombrEstudent)

            return render_template('index.html', estudiantes=result)
        except:
            return 'Ocurrió un problema al buscar'

    else:
        result = get_estudiante_All()
        return render_template('index.html', estudiantes=result)

def get_estudiante_by_Nombre(pcodigo):
    db, cur = get_connection()
    print(pcodigo)
    cur.execute('select * from notas where codigo ='+"'"+pcodigo+"'")
    print(cur)
    return cur.fetchall()

def get_estudiante_by_NombreSeguro(nombre):
    db, cur = get_connection()
    print(nombre)
    cur.execute('prepare myplan as select * from notas where codigo like $1;')
    cur.execute('execute myplan (%s)', (nombre,))
    return cur.fetchall()

def get_estudiante_All():
    conn, cur = get_connection()
    cur.execute('select * from notas')
    return cur.fetchall()

if __name__ == '__main__':
    app.run()
