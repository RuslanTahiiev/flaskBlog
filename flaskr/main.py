from flask import Flask, render_template, url_for, request, redirect



app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/about')
def about_page():
    return render_template('about.html')


@app.route('/create', methods=['POST', 'GET'])
def create_article():
    if request.method == 'POST':
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']
        import mymodels
        article = mymodels.Article(title, intro, text)
        if article.add_article():
            return redirect('/')

    return render_template('create.html')


if __name__ == '__main__':
    app.run(debug=True)