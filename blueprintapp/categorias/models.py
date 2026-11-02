from blueprintapp.app import db

class Categoria(db.Model):
    __tablename__ = "categorias"
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String, nullable = False)
    descripcion = db.Column(db.Text, nullable = True)

    def __repr__(self):
        return f"<CATEGORIA: {self.nombre} - {self.descripcion}"