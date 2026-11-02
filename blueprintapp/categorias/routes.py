# Librerias a usar en el modulo
from flask import request, render_template, redirect, url_for, Blueprint
# Referencia a la base de datos
from blueprintapp.app import db
# Modelos con los que interactua el modulo
from blueprintapp.categorias.models import Categoria

bp_categoria = Blueprint('bp_categoria', __name__, template_folder='templates')

@bp_categoria.route('/')
def index():
    categorias = Categoria.query.all()
    return render_template('categoria/index.html', categorias=categorias)

@bp_categoria.route("/create", methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('categoria/create.html')
    elif request.method == 'POST':
        nombre = request.form.get('nombre')
        categoria = Categoria(nombre=nombre)
        db.session.add(categoria)
        db.session.commit()
        return redirect(url_for('bp_categoria.index'))

# --- NUEVAS RUTAS: CONSULTA, MODIFICACIÓN Y ELIMINACIÓN ---

@bp_categoria.route("/show/<int:id>")
def show(id):
    categoria = Categoria.query.get_or_404(id)
    return render_template('categoria/show.html', categoria=categoria)

@bp_categoria.route("/update/<int:id>", methods=['GET', 'POST'])
def update(id):
    categoria = Categoria.query.get_or_404(id)
    if request.method == 'GET':
        return render_template('categoria/update.html', categoria=categoria)
    elif request.method == 'POST':
        categoria.nombre = request.form.get('nombre')
        db.session.commit()
        return redirect(url_for('bp_categoria.index'))

@bp_categoria.route("/delete/<int:id>")
def delete(id):
    categoria = Categoria.query.get_or_404(id)
    db.session.delete(categoria)
    db.session.commit()
    return redirect(url_for('bp_categoria.index'))