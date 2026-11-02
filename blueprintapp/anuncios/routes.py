#Librerias a usar en el modulo
from flask import request, render_template, redirect, url_for, Blueprint
#Referencia a la base de datos
from blueprintapp.app import db
#Modelos con los que interactua el modulo
from blueprintapp.anuncios.models import Anuncio
from blueprintapp.usuarios.models import Usuario
from blueprintapp.categorias.models import Categoria

bp_anuncio = Blueprint('bp_anuncio', __name__, template_folder='templates')

@bp_anuncio.route('/')
def index():
    anuncios = Anuncio.query.all()
    return render_template('anuncio/index.html', anuncios=anuncios)

@bp_anuncio.route("/create", methods = ['GET', 'POST'])
def create():
    if request.method == 'GET':
        usuarios = Usuario.query.all()
        categorias = Categoria.query.all()
        return render_template('anuncio/create.html', usuarios=usuarios, categorias=categorias)
    elif request.method == 'POST':
        titulo = request.form.get('titulo')
        contenido = request.form.get('contenido')
        usuario_id = request.form.get('usuario_id')
        categoria_id = request.form.get('categoria_id')
        
        # Crear un objeto anuncio
        anuncio = Anuncio(
            titulo=titulo, 
            contenido=contenido, 
            usuario_id=usuario_id, 
            categoria_id=categoria_id
        )
        
        # Insertar en la base de datos a traves del ORM
        db.session.add(anuncio)
        db.session.commit()
        
        # Redireccion al listado de anuncios
        return redirect(url_for('bp_anuncio.index'))