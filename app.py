from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('blog.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS posts
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  title TEXT NOT NULL,
                  content TEXT NOT NULL,
                  created_at TIMESTAMP NOT NULL)''')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    conn = sqlite3.connect('blog.db')
    c = conn.cursor()
    c.execute('SELECT * FROM posts ORDER BY created_at DESC')
    posts = c.fetchall()
    conn.close()
    return render_template('home.html', posts=posts)

@app.route('/create', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        created_at = datetime.now()
        
        conn = sqlite3.connect('blog.db')
        c = conn.cursor()
        c.execute('INSERT INTO posts (title, content, created_at) VALUES (?, ?, ?)',
                 (title, content, created_at))
        conn.commit()
        conn.close()
        
        return redirect(url_for('home'))
    return render_template('create.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True) 

git init