from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user

from extensions import login_manager, bcrypt

from models.user import User, db

register_controller = Blueprint('register_controller', __name__)

@login_manager.user_loader
def load_user(user_id):
      return User.query.get(int(user_id))

@register_controller.route('/register', methods=['GET', 'POST'])
def register():
      if request.method == 'POST':
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']
            password = bcrypt.generate_password_hash(password).decode('utf-8')
            # Cek apakah username atau email sudah digunakan
            existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
            if existing_user:
                  return render_template('register.html', error='Username atau email sudah digunakan.')

            # Buat objek User baru
            new_user = User(username=username, email=email, password=password)

            # Simpan pengguna ke dalam database
            db.session.add(new_user)
            db.session.commit()

            # Login pengguna yang baru didaftarkan
            login_user(new_user)

            return redirect(url_for('viewController.index'))
      else:
            return render_template('register.html')  
