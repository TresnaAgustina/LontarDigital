from flask import Blueprint, render_template, request, session
from flask_login import login_required
from fuzzywuzzy import fuzz

from extensions import login_manager, db

from models.user import User
from models.tokenizing import Tokenizing
from models.katakhusus import KataKhusus
from models.history import History, db

from services.jarowinkler import JaroWinkler
from services.rulebase import Rulebase
from services.tokenizing import Tokenisasi
 
main_controller = Blueprint('main_controller', __name__)

def tokenisasi(teks):

      # instance Tokenisasi
      # tokenisasi = Tokenisasi()

      # tokenisasi
      # text_tokenize = tokenisasi.etokenisasi(teks)
      
      text_tokenize = teks.split()  #memecah teks menjadi kata-kata

      return text_tokenize  

def translate_kata(teks):
      daftar = KataKhusus.query.all()
      hasil_terjemahan = []
      kata_latin = tokenisasi(teks)

      # instance JaroWinkler
      jaro_winkler = JaroWinkler()

      # perbandingan kata dengan JaroWinkler
      suggestions = []
      for kata in kata_latin:
            kata_terjemahan = None
            for kata_khusus in daftar:
                  jaro = jaro_winkler.jaro_similarity(kata, kata_khusus.kata)
                  if jaro > 0.90 :
                        # for i in range(len(kata_khusus.kata)):
                        # ambil kata yang dijadikan pembanding pada jaro winkler lalu masukan ke dalam array kata_asli
                        suggest = [
                              kata, 
                              kata_khusus.kata,
                              kata_khusus.arti
                        ]
                        # suggestions.append(suggest)

                  else:
                        kata_terjemahan = kata_khusus

            #jika kata ditemukan dalam database 
            if kata_terjemahan:
                  # hasil_terjemahan.append(kata_khusus.format_aksara)  # Ganti 'nama' dengan atribut yang sesuai pada objek 'KataKhusus'
                  hasil_terjemahan.append(kata) #GANTI INI KETIKA RULE BASE SUDAH FIX
                  # hasil_terjemahan.append(kata_terjemahan.format_aksara)  # Ganti 'nama' dengan atribut yang sesuai pada objek 'KataKhusus'
            else:
                  hasil_terjemahan.append(kata)  # Kata tidak ditemukan dalam database, biarkan seperti itu
      # gabungkan kata-kata terjemahan menjadi satu kalimat
      trans_result = " ".join(hasil_terjemahan)
      # Menghilangkan spasi berlebihan
      trans_result = " ".join(trans_result.split())

      last = trans_result[-1]  # Mengambil karakter terakhir dari string

      if last != "." and last != ",":
            trans_result += '.'  # Menambahkan titik di akhir kalimat jika belum ada

      rule_base = Rulebase()
      passToRulebase = rule_base.looping_teks(trans_result)

      return passToRulebase, suggestions  # Menggabungkan kata-kata terjemahan menjadi satu kalimat

@login_manager.user_loader
def load_user(user_id):
      return User.query.get(int(user_id))

# =====***===== Translate Controller =====***===== #
@main_controller.route('/translate', methods=['POST'])
@login_required
def translate():
      kata_latin = request.form.get('kata_latin', '')
      # kata_latin = request.form['kata_latin']
      hasil_rulebase = translate_kata(kata_latin)

      hasil = hasil_rulebase[0]

      suggest = hasil_rulebase[1]

      # Query history berdasarkan kata_latin
      existing_history = History.query.filter_by(teks_hasil=hasil).first()

      if existing_history:
            # Jika data dengan kata_latin yang sama sudah ada, update teks_hasil
            existing_history.teks_hasil = hasil
      else:
            # Jika tidak ada data yang cocok, tambahkan data baru
            new_history = History(teks_asli=kata_latin, teks_hasil=hasil)
            db.session.add(new_history)

      db.session.commit()  # Commit perubahan ke dalam database

      # Store the translated text in a session variable
      session['result_text'] = hasil
      
      # return hasil
      return render_template('index.html', hasil=hasil, kata_latin = kata_latin, suggest=suggest)  # Ganti 'hasil.html' dengan template yang sesuai
      # return render_template('index.html', hasil=hasil)  # Ganti 'hasil.html' dengan template yang sesuai

      # 1. tokenizing kata_latin
      # 1. looping kata hasil tokenizing
      # 2. looping kata_khusus yang ada pada database
      # 3. bandingkan setiap kata tokenizing dengan kata database menggunakan JaroWinkler

