#Librerias a usar en el modulo
from flask import request, render_template, redirect, url_for,Blueprint
#Referencia a la base de datos
from blueprintapp.app import db
#Modelos con los que interactua el modulo
from blueprintapp.categorias.models import Categoria

bp_categoria = Blueprint('bp_categoria', __name__, template_folder='templates')

@bp_categoria.route('/')
def index():
    categorias = Categoria.query.all()
    return render_template('categoria/index.html', categoria=categorias)

@bp_categoria.route("/create", methods = ['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('categoria/create.html')
    elif request.method == 'POST':
        nombre = request.form.get('nombre')
        descripcion = request.form.get('descripcion')
        # Crear un objeto usuario
        categoria = Categoria(nombre=nombre, descripcion=descripcion)
        #Insertar en la base de datos a traves del ORM
        db.session.add(categoria)
        db.session.commit()
        # Redireccion al listado de usuarios
        return redirect(url_for('bp_categoria.index'))