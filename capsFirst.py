from flask import Flask, render_template, url_for, flash, redirect
# from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = ''

posts = [
    {
        'author': 'GV',
        'title': 'Capstone Project',
        'phase': 'Phase 1'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)



