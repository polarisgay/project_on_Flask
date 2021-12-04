from flask import Flask, render_template, url_for, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = '46280'

menu = [{'name': 'Установка', 'url': 'install-flask'},
        {'name': 'Первое приложение', 'url': 'first-app'},
        {'name': 'Обратная свять', 'url': 'contact'}]

@app.route("/")
def index():
    print(url_for('index'))
    return render_template("index.html", menu = menu)

@app.route("/about")
def about():
    print(url_for('about'))
    return render_template("about.html", title = "О сайте", menu = menu)

@app.route('/profile/<username>')
def profile(username):
    return f'Пользователь: {username}'

@app.route('/contact', methods = ['POST', 'GET'])
def contact():
    if request.method == "POST":
        if len('username') > 2:
            flash('ЧЕЛ ХАРОШ')
        else:
            flash('КРИНЖАНУЛ')
        print(request.form)
    return render_template('contact.html', title = 'Обратная связь', menu = menu)

# with app.test_request_context():
#    print(url_for('index'))

if __name__ =="__main__":
    app.run(debug=True)