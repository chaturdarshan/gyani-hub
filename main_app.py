from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gyanni_hub.db'
db = SQLAlchemy(app)

# Define database models (e.g., User, Post)

@app.route('/')
def index():
    # Display homepage with list of posts
    return render_template('index.html')

@app.route('/post/<int:post_id>')
def view_post(post_id):
    # View individual post
    return render_template('post.html', post=post)

@app.route('/new_post', methods=['GET', 'POST'])
def new_post():
    # Create new post
    return render_template('new_post.html')

@app.route('/edit_post/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    # Edit existing post
    return render_template('edit_post.html', post=post)

if __name__ == '__main__':
    app.run(debug=True)
