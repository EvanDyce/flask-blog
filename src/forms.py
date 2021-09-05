from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length, Email

class RegistrationForm(FlaskForm):
    username = StringField('Username', 
                            validators=[DataRequired(), Length(min=2, max=20)])
    
    email = StringField('Email', 
                        validators=[DataRequired(), Email(message='Invalid Email')])
    
    password = PasswordField('Password', 
                            validators=[DataRequired()])
    
    confirm_password = PasswordField('Confirm Password', 
                                    validators=[DataRequired(), EqualTo('password', 'Passwords must match')])

    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email', 
                        validators=[DataRequired(), Email()])
    
    password = PasswordField('Password', 
                            validators=[DataRequired()])
    
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')