from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,BooleanField
from wtforms.validators import DataRequired,Length,Email,EqualTo



def RegistrationForm():
    
    username = StringField('Username',validators=[DataRequired(),Length(min=4,max=20)])
    
    email = StringField('Email',validators=[DataRequired(),Email()])
    
    password = StringField('Password',validators=[DataRequired()])
    confirm_password = StringField('Password',validators=[DataRequired(),EqualTo('password')])
    
    submit = SubmitField('Sign Up')
    
    
def LoginForm():
    

    
    email = StringField('Email',validators=[DataRequired(),Email()])
    
    password = StringField('Password',validators=[DataRequired()])
    remember = BooleanField('Remember me')
    
    submit = SubmitField('Login')    