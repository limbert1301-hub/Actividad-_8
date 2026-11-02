#Librerias a usar en el modulo
from flask import request, render_template, redirect, url_for, Blueprint, session
#Referencia a la base de datos
from blueprintapp.app import db
#Modelos con los que interactua el modulo
from blueprintapp.usuarios.models import Usuario

bp_usuario = Blueprint('bp_usuario', __name__, template_folder='templates')

@bp_usuario.route('/')
def index():
    usuarios = Usuario.query.all()
    return render_template('usuario/index.html', usuarios=usuarios)

@bp_usuario.route("/create", methods = ['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('usuario/create.html')
    elif request.method == 'POST':
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        password = request.form.get('password')
        usuario = Usuario(nombre=nombre, email=email, password=password)
        db.session.add(usuario)
        db.session.commit()
        return redirect(url_for('bp_usuario.index'))

@bp_usuario.route("/login", methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('usuario/login.html')
    elif request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        usuario = Usuario.query.filter_by(email=email, password=password).first()
        if usuario:
            session['usuario_id'] = usuario.id
            session['usuario_nombre'] = usuario.nombre
            return redirect(url_for('bp_anuncio.index'))
        else:
            error = "Correo o contraseña incorrectos"
            return render_template('usuario/login.html', error=error)

@bp_usuario.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('bp_core.index'))

# --- NUEVAS RUTAS PARA CONSULTA, MODIFICACIÓN Y ELIMINACIÓN ---

@bp_usuario.route("/show/<int:id>")
def show(id):
    usuario = Usuario.query.get_or_404(id)
    return render_template('usuario/show.html', usuario=usuario)

@bp_usuario.route("/update/<int:id>", methods=['GET', 'POST'])
def update(id):
    usuario = Usuario.query.get_or_404(id)
    if request.method == 'GET':
        return render_template('usuario/update.html', usuario=usuario)
    elif request.method == 'POST':
        usuario.nombre = request.form.get('nombre')
        usuario.email = request.form.get('email')
        password = request.form.get('password')
        if password:
            usuario.password = password
        db.session.commit()
        return redirect(url_for('bp_usuario.index'))

@bp_usuario.route("/delete/<int:id>")
def delete(id):
    usuario = Usuario.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    return redirect(url_for('bp_usuario.index'))