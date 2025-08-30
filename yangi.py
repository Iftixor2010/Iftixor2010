from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'some_secret_key'  # Flash xabarlar uchun maxfiy kalit

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    flash(f"Rahmat, {name}! Sizning xabaringiz qabul qilindi.")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
