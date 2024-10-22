from flask import Flask,render_template,request,session,redirect,url_for

app = Flask(__name__)
# para session requiere una clave secreta debajo de app es importante
app.secret_key ='unaclavesecreta'

@app.route("/")
def carrito():
    #verficando si esta en la sesion
    if 'lista' not in session:
        #inicializar la lista
        session['lista'] =[]
    return render_template('index.html',lista = session['lista'])

@app.route("/proceso",methods=['GET','POST'])
def procesa():
    producto = request.form.get("producto")
    if 'lista' in session and producto:
        #producto adicionado en la lista
        session['lista'].append(producto)
        #aseguramos que la session a sido modificado
        session.modified = True
    return redirect(url_for("carrito"))
@app.route("/vaciar",methods=['GET'])
def vaciar():
    #elimina de session el objeto oh la lista
    session.pop("lista",None)
    return redirect(url_for("carrito"))




if __name__=="__main__":
    app.run(debug=True)