from flask import Blueprint, render_template, request

from models.katakhusus import KataKhusus, db

search_blueprint = Blueprint('search', __name__)

@search_blueprint.route('/search', methods=['POST'])
def search():
    # get data from form
    keyword = request.form.get('keyword')

    # pagination
    page = request.args.get('page', 1, type=int)
    # get daata from database
    words = KataKhusus.query.filter(KataKhusus.kata.like('%' + keyword + '%')).paginate(page=page, per_page=18)
    # # get data from database
    # words = KataKhusus.query.filter(KataKhusus.kata.like('%' + keyword + '%')).all()
    # pagination
            
    return render_template('word_list.html', words=words, current_page=page)
