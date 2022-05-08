from app import app
from flask import render_template,url_for,flash,redirect
from app.form import RegistrationForm,LoginForm

from app.models import User,Pitch



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

@app.route('/register',methods=['GET','POST'])
def register():
    
    form = RegistrationForm()
    if form.validate_on_submit():
        
        flash(f'Hello {form.username.data}!,Account created successfully','success')
        return redirect(url_for('home'))
    
    return render_template('register.html',form= form)


@app.route('/login',methods=['GET','POST'])
def login(): 
    
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'furywrld5@gmail.com' and form.password.data == 'password':
            flash('Logged in succesfully','success')
            return redirect(url_for('home'))        
         
            
        
        else:
            flash('Login error!!. Enter correct username and password','danger')
    
    
    return render_template('login.html',form = form)