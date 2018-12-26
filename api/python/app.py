from flask import Flask, request, json, session
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
import os
import jwt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Sembilantujuh97@localhost:5432/e_library'
CORS(app, support_credentials=True)

db = SQLAlchemy(app)

class Buku(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    judul = db.Column(db.String())
    tahun_terbit = db.Column(db.String())
    pengarang =  db.Column(db.String())
    gambar = db.Column(db.String())

class Peminjam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama_peminjam = db.Column(db.String())
    judul = db.Column(db.String())
    no_buku = db.Column(db.Integer, db.ForeignKey('buku.id'))
    tanggal_peminjaman = db.Column(db.String())
    tanggal_pengembalian = db.Column(db.String())


#fungsi menambah buku
@app.route('/tambahBuku', methods=["POST"])
def tambahBuku ():
    if request.method == "POST":
        req_data = request.get_json()

        # ngirim ke Database
        sent_data = Buku(
            #harus sesuai urutan yang di class person
            judul = req_data.get('judul'),
            tahun_terbit = req_data.get('tahun_terbit'),
            pengarang = req_data.get('pengarang'),
            gambar = req_data.get('gambar')
        )

        #add to Data Base
        db.session.add(sent_data)
        db.session.commit()

        return "Success", 200
    else:
        return "Method Not Allowed",405


#fungsi menambah data peminjam
@app.route('/dataPeminjam', methods=["POST"])
def dataPeminjam ():
    if request.method == "POST":
        req_data = request.get_json()

        # ngirim ke Database
        sent_data = Peminjam(
            #harus sesuai urutan yang di class person
            nama_peminjam = req_data.get('nama_peminjam'),
            judul = req_data.get('judul'),
            no_buku = req_data.get('no_buku'),
            tanggal_peminjaman = req_data.get('tanggal_peminjaman'),
            tanggal_pengembalian = req_data.get('tanggal_pengembalian')
        )

        #add to Data Base
        db.session.add(sent_data)
        db.session.commit()

        return "Success", 200
    else:
        return "Method Not Allowed",405

# fungsi untuk menampilkan data buku
@app.route('/dataBuku', methods=["GET"])
def dataBuku():
    semuaBuku = Buku.query.all()
    arrayBuku = []
    for buku in semuaBuku:
        jsonFormat = {
            "judul": buku.judul,
            "no_buku": buku.id,
            "tahun_terbit": buku.tahun_terbit,
            "pengarang": buku.pengarang,
            "gambar" : buku.gambar
        }
        arrayBuku.append(jsonFormat)
    detailbuku = json.dumps(arrayBuku)
    return detailbuku, 201

if __name__ == '__main__':
    app.run(debug=os.getenv("DEBUG"), host=os.getenv("HOST"), port=3000)