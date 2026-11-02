from blueprintapp.app import db

class Anuncio(db.Model):
    __tablename__ = 'anuncios'
    
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    contenido = db.Column(db.Text, nullable=False)
    
    # Llaves foráneas
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable=False)
    
    # Relaciones para que SQLAlchemy traiga el objeto completo
    usuario = db.relationship('Usuario', backref=db.backref('anuncios', lazy=True))
    categoria = db.relationship('Categoria', backref=db.backref('anuncios', lazy=True))