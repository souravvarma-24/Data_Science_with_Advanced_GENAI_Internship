from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import string, random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# ---------------- MODELS ----------------

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500), nullable=False)
    short_code = db.Column(db.String(10), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# ---------------- HELPERS ----------------

def generate_short_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

# ---------------- ROUTES ----------------

@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and check_password_hash(user.password, request.form['password']):
            login_user(user)
            return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/')
@login_required
def home():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
@login_required
def shorten():
    original_url = request.form['url']
    short_code = generate_short_code()
    new_url = URL(original_url=original_url, short_code=short_code, user_id=current_user.id)
    db.session.add(new_url)
    db.session.commit()
    return redirect(url_for('history'))

@app.route('/history')
@login_required
def history():
    urls = URL.query.filter_by(user_id=current_user.id).all()
    return render_template('history.html', urls=urls)

@app.route('/<short_code>')
def redirect_url(short_code):
    url = URL.query.filter_by(short_code=short_code).first_or_404()
    return redirect(url.original_url)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# ---------------- RUN ----------------

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
