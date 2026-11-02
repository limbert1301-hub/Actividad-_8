from blueprintapp.app import db

class Anuncio(db.Model):
    __tablename__ = "anuncios"

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String, nullable=False)
    contenido = db.Column(db.Text, nullable=False)
    
    # Claves foráneas
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable=False)

    def __repr__(self):
        return f"<ANUNCIO: {self.titulo} - {self.contenido}>"