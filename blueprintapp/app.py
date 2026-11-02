from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bd_anuncios.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app,db)

    #1. Importacion del blueprint (para cada modulo)
    from blueprintapp.usuarios.routes import bp_usuario
    from blueprintapp.core.routes import bp_core
    from blueprintapp.categorias.routes import bp_categoria

    #2. Registrar el blueprint (para cada modulo)
    app.register_blueprint(bp_usuario, url_prefix="/usuarios")
    app.register_blueprint(bp_core, url_prefix="/")
    app.register_blueprint(bp_categoria, url_prefix="/categorias")

    return app