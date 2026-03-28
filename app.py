import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

class Kategori(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nama = db.Column(db.String(50), nullable = False, unique = True)
    barangs = db.relationship('Barang', backref = 'kategori_info', lazy = True)

class Barang(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    harga = db.Column(db.Integer, nullable = False, default = 0)
    stok = db.Column(db.Integer, nullable=False)
    kategori_id = db.Column(db.Integer, db.ForeignKey('kategori.id'), nullable = True)
    gambar = db.Column(db.String(255), nullable=True)

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# --- ROUTES ---

@app.route('/')
def index():
    search_query = request.args.get('search')
    kategori_id = request.args.get('kat')
    
    query = Barang.query
    if search_query:
        query = query.filter(Barang.nama.contains(search_query))
    
    if kategori_id:
        query = query.filter(Barang.kategori_id == kategori_id)
        
    daftar_barang = query.all()
    daftar_kategori = Kategori.query.all()
    return render_template('index.html', barang=daftar_barang, kategori = daftar_kategori)

# Route untuk Tambah Barang
@app.route('/add', methods=['POST'])
def add():
    nama_input = request.form.get('nama')
    stok_input = int(request.form.get('stok') or 0)
    harga_input = int(request.form.get('harga') or 0)
    kat_id = request.form.get('kategori_id')
    file = request.files.get('gambar')

    if stok_input < 0 or harga_input < 0:
        return redirect(url_for('index'))
    
    filename = None
    if file and file.filename != '':
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    barang_baru = Barang(nama=nama_input, stok=stok_input, harga=harga_input, gambar=filename, kategori_id=kat_id if kat_id else None)

    db.session.add(barang_baru)
    db.session.commit()
    return redirect(url_for('index'))

#Route kategori tambahan
@app.route('/add_kategori', methods=['POST'])
def add_kategori():
    nama_kat = request.form.get('nama_kategori')
    if nama_kat:
        baru = Kategori(nama=nama_kat)
        db.session.add(baru)
        db.session.commit()
    return redirect(url_for('index'))

#Route edit barang
@app.route('/edit/<int:id>', methods=['POST'])
def edit(id):
    barang = Barang.query.get_or_404(id)

    nama_baru = request.form.get('nama')
    stok_baru = int(request.form.get('stok') or 0)
    harga_baru = int(request.form.get('harga') or 0)
    kat_id = request.form.get('kategori_id')

    if not nama_baru or stok_baru < 0 or harga_baru < 0:
        return redirect(url_for('index'))
    
    barang.nama = request.form.get('nama')
    barang.stok = int(request.form.get('stok') or 0)
    barang.harga = int(request.form.get('harga') or 0)
    barang.kategori_id = request.form.get('kategori_id') or None

    file = request.files.get('gambar')
    if file and file.filename != '':
        if barang.gambar:
            old_path = os.path.join(app.config['UPLOAD_FOLDER'], barang.gambar)
            if os.path.exists(old_path):
                os.remove(old_path)
        
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        barang.gambar = filename

    db.session.commit()
    return redirect(url_for('index'))

# Route untuk Hapus Barang
@app.route('/delete/<int:id>')
def delete(id):
    barang_hapus = Barang.query.get_or_404(id)

    if barang_hapus.gambar:
        path_gambar = os.path.join(app.config['UPLOAD_FOLDER'], barang_hapus.gambar)
        if os.path.exists(path_gambar):
            os.remove(path_gambar)

    db.session.delete(barang_hapus)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)