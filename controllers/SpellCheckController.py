from flask import Blueprint, request, jsonify, session, render_template

# import service jaro_winkler
from services.jarowinkler import JaroWinkler

# import model KataKhusus
from models.katakhusus import KataKhusus

spell_check_blueprint = Blueprint('spell_check', __name__)

@spell_check_blueprint.route('/spell_check', methods=['POST'])
def spell_check():
    # get text from request
    data = request.get_json()
    kata_latin = data['kata_latin']

    # get kata khusus
    daftar = KataKhusus.query.all()
    hasil_terjemahan = []
    kata_latin = tokenisasi(kata_latin)

    # instance JaroWinkler
    jaro_winkler = JaroWinkler()

    # perbandingan kata dengan JaroWinkler
    suggestions = []
    for kata in kata_latin:
        kata_terjemahan = None
        for kata_khusus in daftar:
            jaro = jaro_winkler.jaro_similarity(kata, kata_khusus.kata)
            if jaro > 0.90:
                suggest = [
                    kata,
                    kata_khusus.kata,
                    kata_khusus.arti,
                    kata_khusus.format_aksara
                ]
                suggestions.append(suggest)
            else:
                kata_terjemahan = kata_khusus

        if kata_terjemahan:
            hasil_terjemahan.append(kata)
        else:
            hasil_terjemahan.append(kata)

    trans_result = " ".join(hasil_terjemahan)
    trans_result = " ".join(trans_result.split())

    return jsonify({"suggestions": suggestions, "trans_result": trans_result})

def tokenisasi(text):
    text_tokenize = text.split()  # memecah teks menjadi kata-kata
    return text_tokenize
