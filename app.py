from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flash messages

# Hardcoded credentials (username: user, password: pass)
USERNAME = 'user'
PASSWORD = 'pass'

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    if username == USERNAME and password == PASSWORD:
        return redirect(url_for('beranda'))
    else:
        flash('Username atau password salah. Silahkan coba lagi.')
        return redirect(url_for('index'))

@app.route("/beranda")
def beranda():
    return render_template('beranda.html')

@app.route("/transaksi")
def transaksi():
    return render_template('transaksi.html')

@app.route("/produk")
def produk():
    return render_template('produk.html')

@app.route("/laporan")
def laporan():
    return render_template('laporan.html')

@app.route("/pengaturan")
def pengaturan():
    return render_template('pengaturan.html')

if __name__ == '__main__':
    app.run(debug=True)