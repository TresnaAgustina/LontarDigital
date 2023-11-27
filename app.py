from flask import Flask
from flask_bcrypt import Bcrypt
# extensions
from extensions import db, login_manager
# controllers
from controllers.viewController import viewController
from controllers.login_controller import login_controller
from controllers.register_controller import register_controller
from controllers.main_controller import main_controller
from controllers.exportPdf_controller import export_pdf_blueprint
from controllers.exportLontar_controller import export_lontar_blueprint
from controllers.SpellCheckController import spell_check_blueprint

# models
import models.user
import models.tokenizing
import models.katakhusus
import models.history


app = Flask(__name__)

# ===== Configurasi ===== #
app.config['SECRET_KEY'] = "thisissecretkey3321" 
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost:3306/lontardigital'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# inisialisasi db dan login manager
db.init_app(app)
login_manager.init_app(app)

# ===== Register Blueprints ===== #
app.register_blueprint(login_controller, url_prefix='/auth')
app.register_blueprint(register_controller, url_prefix='/auth')
app.register_blueprint(viewController)
app.register_blueprint(main_controller)
app.register_blueprint(export_pdf_blueprint)
app.register_blueprint(export_lontar_blueprint)
app.register_blueprint(spell_check_blueprint)

# inisialisasi bcrypt
bcrypt = Bcrypt(app)

# create table
with app.app_context():
      db.create_all()

if __name__ == '__main__':
      app.run(debug=True)
