
import os
import secrets
from PIL import Image
from app import app,db,bcrypt
from flask import render_template,url_for,flash,redirect,request,abort
from app.form import RegistrationForm,LoginForm,UpdateAccountForm,PitchForm
from app.models import User,Pitch
from flask_login import login_user,current_user,logout_user,login_required




@app.route('/')
@app.route('/home')
def home():
    pitches = Pitch.query.all()
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
        pitch = Pitch(title=form.title.data,pitch=form.pitch.data, author=current_user)
        db.session.add(pitch)
        db.session.commit()
        flash('Your pitch has been added!','success')
        return redirect(url_for('home'))
    
    return render_template('newpitch.html',form= form,legend ='New pitch')    


@app.route('/pitch/<int:pitch_id>')
def pitched(pitch_id):
    pitch = Pitch.query.get_or_404(pitch_id) 
    return render_template('pitched.html', pitch= pitch)   

@app.route('/pitch/<int:pitch_id>/update',methods=['GET','POST'])
@login_required
def update_pitch(pitch_id):
    pitch = Pitch.query.get_or_404(pitch_id) 
    if pitch.author != current_user:
        abort(403)
    form = PitchForm()
    if form.validate_on_submit():
        pitch.title = form.title.data
        pitch.pitch = form.pitch.data
        db.session.commit()
        flash('Your pitch has been updated','success')
        return redirect(url_for('home'))
    elif request.method == 'GET':
        form.title.data = pitch.title
        form.pitch.data = pitch.pitch
    
    return render_template('newpitch.html',form= form, legend ='Update pitch')    



@app.route('/pitch/<int:pitch_id>/delete',methods=['POST'])
@login_required
def delete_pitch(pitch_id):
    pitch = Pitch.query.get_or_404(pitch_id) 
    if pitch.author != current_user:
        abort(403)
    db.session.delete(pitch)
    db.session.commit() 
    flash('Your pitch has been deleted','success')
    
    return redirect(url_for('home'))
       
        
       
    
        