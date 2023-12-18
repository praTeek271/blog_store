from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import PostForm
from app.models import Post

@app.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)

@app.route('/add_post', methods=['GET', 'POST'])
def add_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data)
        db.session.add(post)
        db.session.commit()
        flash('Post added successfully!')
        return redirect(url_for('index'))
    return render_template('add_post.html', form=form)
