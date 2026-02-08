from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import string
import random

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'
db = SQLAlchemy(app)

# Database model
class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500), nullable=False)
    short_code = db.Column(db.String(10), unique=True, nullable=False)

# Create database
with app.app_context():
    db.create_all()

# Generate short code
def generate_short_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

# Home page
@app.route("/", methods=["GET", "POST"])
def index():
    short_url = None
    error = None

    if request.method == "POST":
        original_url = request.form.get("url")

        if not original_url.startswith("http://") and not original_url.startswith("https://"):
            error = "Invalid URL. Must start with http:// or https://"
        else:
            code = generate_short_code()
            new_url = URL(original_url=original_url, short_code=code)
            db.session.add(new_url)
            db.session.commit()
            short_url = request.host_url + code

    return render_template("index.html", short_url=short_url, error=error)

# Redirect short URL
@app.route("/<code>")
def redirect_url(code):
    url = URL.query.filter_by(short_code=code).first_or_404()
    return redirect(url.original_url)

# History page
@app.route("/history")
def history():
    urls = URL.query.all()
    return render_template("history.html", urls=urls)

if __name__ == "__main__":
    app.run(debug=True)
