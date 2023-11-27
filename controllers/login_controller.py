from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, login_required, logout_user

from extensions import login_manager, bcrypt

from models.user import User, db

login_controller = Blueprint('login_controller', __name__)

@login_manager.user_loader
def load_user(user_id):
      return User.query.get(int(user_id))

# login page
@login_controller.route('/login', methods=['GET', 'POST'])
def login():
      if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            user = User.query.filter_by(username=username).first()
            if not user:
                  return render_template('login.html', error="Akun tidak ditemukan.")

            if user and bcrypt.check_password_hash(user.password, password):
                  login_user(user)
                  return redirect(url_for('viewController.index'))
            else:
                  return render_template('login.html', error='Username atau password salah.')
      else:
            return render_template('login.html')

# logout page
@login_controller.route('/logout')
@login_required
def logout():
      logout_user()
      return redirect(url_for('login_controller.login'))
    