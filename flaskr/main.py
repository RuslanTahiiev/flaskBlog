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
            return redirect('/posts')

    return render_template('create.html')


@app.route('/posts')
def posts():
    import mymodels
    articles = mymodels.Article.query.order_by(mymodels.Article.date.desc()).all()
    return render_template('posts.html', articles=articles)


@app.route('/posts/<int:id>')
def post_detail(id):
    import mymodels
    article = mymodels.Article.query.get(id)
    return render_template('post_detail.html', article=article)



if __name__ == '__main__':
    app.run(debug=True)
