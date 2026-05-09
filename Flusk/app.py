from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask import jsonify

app = Flask(__name__)
app.secret_key = 'klucz-tajny-do-zmiany-w-produkcji'

@app.route('/')
def index():
    items = ['Python', 'Flask', 'Jinja2']
    return render_template('index.html', items=items)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact/', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        message = request.form.get('message', '').strip()
        if not name or not email or not message:
            flash('Wszystkie pola są wymagane!', 'error')
            return redirect(url_for('contact'))
        flash(f'Dziękujemy, {name}! Twoja wiadomość została wysłana.', 'success')
        return redirect(url_for('index'))
    return render_template('contact.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')
        if username == 'admin' and password == 'admin123':
            session['username'] = username
            flash(f'Zalogowano jako {username}!', 'success')
            return redirect(url_for('index'))
        flash('Nieprawidłowe dane logowania!', 'error')
        return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Wylogowano pomyślnie.', 'info')
    return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html', code=404, message='Strona nie została znaleziona'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('error.html', code=500, message='Wewnętrzny błąd serwera'), 500

books_data = [
    {'id': 1, 'title': 'Wiedźmin: Ostatnie życzenie', 'author': 'Andrzej Sapkowski', 'year': 1993},
    {'id': 2, 'title': 'Solaris', 'author': 'Stanisław Lem', 'year': 1961},
    {'id': 3, 'title': 'Lalka', 'author': 'Bolesław Prus', 'year': 1890},
]
next_id = 4

@app.route('/api/books')
def api_books():
    return books_data

@app.route('/api/authors')
def api_authors():
    authors = list(book['author'] for book in books_data)
    return authors

@app.route('/api/books/<int:book_id>')
def api_book(book_id):
    book = next((b for b in books_data if b['id'] == book_id), None)
    if book is None:
        return {'error': 'Nie znaleziono książki'}, 404
    return book

@app.route('/api/books', methods=['POST'])
def api_book_create():
    global next_id
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Brak danych JSON'}), 400
    for field in ['title', 'author', 'year']:
        if field not in data:
            return jsonify({'error': f'Brak pola: {field}'}), 400
    book = {'id': next_id, 'title': str(data['title']),
            'author': str(data['author']), 'year': int(data['year'])}
    next_id += 1
    books_data.append(book)
    return jsonify(book), 201

if __name__ == '__main__':
    app.run(debug=True, port=5001)

# ==============================================================================================

# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html',
#                            title='Strona główna',
#                            username='Student',
#                            items=['Chleb', 'Masło', 'Mleko', 'Jajka'])

# @app.route('/empty')
# def empty():
#     return render_template('index.html',
#                            title='Pusta lista',
#                            username='Student',
#                            items=[])

# if __name__ == '__main__':
#     app.run(debug=True, port=5001)

# ==============================================================================================

# from flask import Flask, request

# app = Flask(__name__)

# attempts = 0

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     global attempts
#     if request.method == 'POST':
#         username = request.form.get('username', '')
#         password = request.form.get('password', '')
#         if username == 'admin' and password == 'admin':
#             attempts = 0
#             return f'<h1>Witaj, {username}!</h1>'
#         attempts += 1
#         if attempts >= 3:
#             attempts = 0
#             return '<h1>Przekroczono liczbę prób logowania!</h1>'
#         return '<h1>Błędne dane!</h1><a href="/login">Spróbuj ponownie</a>'
#     return '''
#         <h1>Logowanie</h1>
#         <form method="POST">
#             <p>Login: <input type="text" name="username"></p>
#             <p>Hasło: <input type="password" name="password"></p>
#             <p><input type="submit" value="Zaloguj"></p>
#         </form>
#     '''

# if __name__ == '__main__':
#     app.run(debug=True, port=5001)

# ==============================================================================================

# from flask import Flask
# from markupsafe import escape
# from datetime import datetime

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return '<h1>Strona główna</h1>'

# @app.route('/about')
# def about():
#     return '<h1>O aplikacji</h1>'

# @app.route('/contact/')
# def contact():
#     return '<h1>Kontakt</h1>'

# # Routing dynamiczny - wartość z URL trafia jako argument funkcji
# @app.route('/user/<username>')
# def show_user(username):
#     return f'<h1>Profil: {escape(username)}</h1>'

# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     return f'<h1>Post nr {post_id}</h1>'

# @app.route('/date')
# def date():
#     now = datetime.now()
#     return f'<h1>Aktualna data i godzina:</h1><p>{now}</p>'

# @app.route('/sum/<a>/<b>')
# def sum(a, b):
#     return f'<h1>Suma:</h1><p>{int(a) + int(b)}</p>'

# if __name__ == '__main__':
#     app.run(debug=True, port=5001)