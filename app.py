from flask import Flask, render_template

# Flask_App Definition
app = Flask(__name__)

# A list having 
PAGES = [
    {'name': 'Home',  'source':'home'},
    {'name': 'About', 'source':'about'},
    {'name': 'Work', 'source':'work'}
]

# A Route to home of the web-app
@app.route('/')
def home():
    return render_template('home.html', title='Home', pages=PAGES)

# A Route to About Page
@app.route('/about')
def about():
    return render_template('about.html', title='About', pages=PAGES)

# A Route definition of Projects
@app.route('/work')
def work():
    return render_template('work.html', title='Work', pages=PAGES)

if __name__ == '__main__':
    app.run()