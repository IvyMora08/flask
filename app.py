from flask import flask
app = Flask (__name__)
 
@app.roote('/')
def hola():
    return 'Hola,Pagina demo para IDGS93,con el profe rene'
@app.route('/acerca')
def acerca():
    return 'Esta es  otra pagina simple de una aplicacion con flask'
if __name__ == '__main__':
    app.run(debug=True)

