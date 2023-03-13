from flask import Flask, render_template, request, redirect, url_for, flash

posts = [
    {
        'author': 'John Doe',
        'title': 'Blog Post 1',
        'content': 'Lorem ipsum',
        'date': 'Jan 1 3033',
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Lorem ipsum',
        'date': 'Jan 1 3033',
    }
]

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)