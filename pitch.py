from flask import Flask, render_template,url_for
from form import RegistrationForm,LoginForm

app = Flask(__name__)

app.config['SECRET_KEY']= '56f0def8068b3dfc'

pitches =[
    {
        'author':'Mike will',
        'title':'UX Design',
        'pitch':'Did you know that the best payment milestones are dependent on your delivery and not on client approval?',
        'posted':'03/02/2020'
        
    },
    {
        'author':'Mint',
        'title':'Product Design',
        'pitch':'Designing a product is a very broad concept, it is essentially the efficient ',
        'posted':'12/02/2021'
    },
    {
        'author':'Juice',
        'title':'Interview',
        'pitch':'The executive engaged in the normal conduct of business devotes much of his time to interviewing. ',
        'posted':'22/04/2022'
        
    }    
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',pitches=pitches)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/register')
def register():
    
    form = RegistrationForm()
    
    return render_template('register.html',form = form)


@app.route('/login')
def login():
    
    form = LoginForm()
    
    return render_template('login.html',form = form)


if __name__ == '__main__':
    app.run(debug=True)


    
    