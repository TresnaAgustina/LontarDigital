from flask import Blueprint, render_template, request, redirect, url_for, session
from flask_login import login_required
from datetime import datetime

from extensions import login_manager

from models.user import User, db
from models.katakhusus import KataKhusus, db
from models.history import History, db

viewController = Blueprint('viewController', __name__)

@login_manager.user_loader
def load_user(user_id):
      return User.query.get(int(user_id))

# ===== View Controllers ===== #
# index page
@viewController.route('/')
@login_required
def index():
      return render_template('index.html')

ROWS_PER_PAGE = 18
@viewController.route('/list', methods=['GET'])
@login_required
def wordList():
      # get all words from database
      # words = KataKhusus.query.all()
      # pagination
      page = request.args.get('page', 1, type=int)
      words = KataKhusus.query.paginate(page=page, per_page=ROWS_PER_PAGE)
      if words is None:
            return render_template('word_list.html', words=None, current_page=page)
      return render_template('word_list.html', words=words, current_page=page)

# ===== Word Add Routes =====
@viewController.route('/add', methods=['GET', 'POST'])
@login_required
def wordAdd():
#      check request method
      if request.method == 'POST':
            # get data from form
            kata = request.form['kata_latin']
            arti = request.form['arti_kata']
            format_aksara = request.form['bentuk_aksara']

            # create new word
            new_word = KataKhusus(kata=kata, arti=arti, format_aksara=format_aksara)
            
            # save word to database
            db.session.add(new_word)
            db.session.commit()
            return redirect(url_for('viewController.wordList'))
      else:
            return render_template('add_word.html')


# ===== Word Edit Routes =====
@viewController.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
def wordEdit(id):
      # check request method
      if request.method == 'POST':
            # get word from database
            word = KataKhusus.query.filter_by(id=id).first()

            # update word
            word.kata = request.form['kata_latin']
            word.arti = request.form['arti_kata']
            word.format_aksara = request.form['bentuk_aksara']
            word.updated_at = datetime.utcnow()
            
            # save word to database
            db.session.commit()
            return redirect(url_for('viewController.wordList'))
      else:
            # get word from database
            word = KataKhusus.query.filter_by(id=id).first()
            return render_template('edit_word.html', words=word)

#  delete word
@viewController.route('/delete/<int:id>', methods=['GET'])
@login_required
def wordDelete(id):
      # get word from database
      word = KataKhusus.query.filter_by(id=id).first()
      # delete word
      db.session.delete(word)
      db.session.commit()
      # return to word list, success message and stay on current page
      return redirect(url_for('viewController.wordList', success='Kata berhasil dihapus.'))

# history page
@viewController.route('/history', methods=['GET'])
@login_required
def history():
      history = History.query.all()
      return render_template('history.html', history=history, index=index)

# details history
@viewController.route('/history/<int:id>', methods=['GET'])
@login_required
def historyDetails(id):
      history = History.query.filter_by(id=id).first()
      return render_template('history_detail.html', history=history)

# delete history
@viewController.route('/history/delete/<int:id>', methods=['GET'])
@login_required
def historyDelete(id):
      # get history from database
      history = History.query.filter_by(id=id).first()
      # delete history
      db.session.delete(history)
      db.session.commit()
      # return to history list, success message and stay on current page
      return redirect(url_for('viewController.history', success='Riwayat berhasil dihapus.'))
# translate route
# @viewController.route('/translate', methods=['POST'])
# @login_required
# def translate():
#       # getting data
#       kata = request.form['latin_text']

#       token = word_tokenize(kata)
#       return render_template('index.html', hasil=token)

# view lontar template
@viewController.route('/lontar/template/<int:id>', methods=['GET'])
@login_required
def templateLontar(id):
      history = History.query.filter_by(id = id).first()
      return render_template('LontarTemplate.html', history=history)