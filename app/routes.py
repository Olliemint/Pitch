import os
import secrets
from PIL import Image
from app import app,db,bcrypt
from flask import render_template,url_for,flash,redirect,request
from app.form import RegistrationForm,LoginForm,UpdateAccountForm,PitchForm
from app.models import User,Pitch
from flask_login import login_user,current_user,logout_user,login_required



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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created succefully,You can login now','success')
        return redirect(url_for('login'))
    
    return render_template('register.html',form= form)


@app.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home')) 
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember= form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        
        else:
            flash('Login error!!. Enter correct email and password','danger')
            
            
    return render_template('login.html',form = form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

def save_avatar(form_picture):
    random_hex = secrets.token_hex(8)
    _,f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profiles', picture_fn)
    
    
    output_resize = (75,77)
    i = Image.open(form_picture)
    i.thumbnail(output_resize)
    i.save(picture_path)
    
    return picture_fn

    
    

@app.route('/account',methods=['GET','POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file =save_avatar(form.picture.data)
            current_user.avatar = picture_file

        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your data has been updated', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username 
        form.email.data = current_user.email 

        
    profile_img = url_for('static',filename ='profiles/' + current_user.avatar)
    return render_template('account.html',profile_img = profile_img, form=form)    


@app.route('/pitch/new',methods=['GET','POST'])
@login_required
def pitch():
    form = PitchForm()
    if form.validate_on_submit():
        flash('Your pitch has been added!','success')
        return redirect(url_for('home'))
    
    return render_template('newpitch.html',form= form)    
    

    
        