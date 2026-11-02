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
        # Crear un objeto usuario
        usuario = Usuario(nombre=nombre, email=email, password=password)
        #Insertar en la base de datos a traves del ORM
        db.session.add(usuario)
        db.session.commit()
        # Redireccion al listado de usuarios
        return redirect(url_for('bp_usuario.index'))

@bp_usuario.route("/login", methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('usuario/login.html')
    elif request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Validar credenciales en la base de datos
        usuario = Usuario.query.filter_by(email=email, password=password).first()
        
        if usuario:
            # Guardar datos básicos en sesión
            session['usuario_id'] = usuario.id
            session['usuario_nombre'] = usuario.nombre
            # Redirigir al listado de anuncios o bienvenida
            return redirect(url_for('bp_anuncio.index'))
        else:
            # Si falla, recargar con un mensaje de error simple
            error = "Correo o contraseña incorrectos"
            return render_template('usuario/login.html', error=error)

@bp_usuario.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('bp_core.index'))
