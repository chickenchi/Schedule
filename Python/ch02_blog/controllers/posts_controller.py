from flask import render_template, request, redirect, url_for, Blueprint
from services.posts_service import PostService

posts_blueprint = Blueprint('post', __name__)
posts_service = PostService()

@posts_blueprint.route('/')
def index():
    posts = posts_service.get()
    return render_template('index.html', posts=posts)

@posts_blueprint.route('/new_post', methods=['POST', 'GET'])
def post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        author = request.form['author']
        posts_service.add({'title': title, 'content': content, 'author': author})
        return redirect(url_for('post.index'))
    else:
        return render_template('post.html')
    
@posts_blueprint.route('/update/<int:index>', methods=['POST', 'GET'])
def update(index):
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        author = request.form['author']
        posts_service.revision({'title': title, 'content': content, 'author': author}, index)
        return redirect(url_for('post.index'))
    else:
        post = posts_service.call(index)
        return render_template('update.html', post=post[0])

@posts_blueprint.route('/delete/<int:index>')
def delete(index):
    posts_service.delete(index)
    return redirect(url_for('post.index'))