from flask import render_template, url_for, request, redirect
from flask import current_app as app
from .models import Article


@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home_page():
    if request.method == 'POST':
        return redirect(url_for('search_posts', title=request.form['title']))
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
        article = Article(title, intro, text)
        if article.add_article():
            return redirect(url_for('posts'))

    return render_template('create.html')


@app.route('/posts')
def posts():
    articles = Article.query.order_by(Article.date.desc()).all()
    return render_template('posts.html', articles=articles)


@app.route('/posts/search/<title>')
def search_posts(title):
    articles = Article.query.filter_by(title=title).all()
    return render_template('posts.html', articles=articles)


@app.route('/posts/<int:article_id>')
def post_detail(article_id):
    article = Article.query.get(article_id)
    return render_template('post_detail.html', article=article)


@app.route('/posts/<int:article_id>/delete')
def post_delete(article_id):
    article = Article.query.get_or_404(article_id)
    if article.delete_article():
        return redirect(url_for('posts'))
    else:
        return 'Error'


@app.route('/posts/<int:article_id>/update', methods=['POST', 'GET'])
def post_update(article_id):
    article = Article.query.get(article_id)
    if request.method == 'POST':
        article.title = request.form['title']
        article.intro = request.form['intro']
        article.text = request.form['text']
        if article.update_article():
            return redirect(url_for('posts'))
    return render_template('update.html', article=article)

