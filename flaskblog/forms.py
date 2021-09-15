from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import BooleanField, StringField, PasswordField, SubmitField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import DataRequired, EqualTo, Length, Email, ValidationError
from flaskblog.models import User

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

    def validate_username(self, username):
        # if there is a user in the database with the same username will return ite
        # else it will just be null and conditional is Falsey
        user = User.query.filter_by(username=username.data).first()
        
        if user:
            raise ValidationError('Username is already taken. Choose a new one.')

    def validate_email(self, email):
        # if there is a user in the database with the same email will return ite
        # else it will just be null and conditional is Falsey
        user = User.query.filter_by(email=email.data).first()
        
        if user:
            raise ValidationError('Account with this email already exists.')


class LoginForm(FlaskForm):
    email = StringField('Email', 
                        validators=[DataRequired(), Email()])
    
    password = PasswordField('Password', 
                            validators=[DataRequired()])
    
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username', 
                            validators=[DataRequired(), Length(min=2, max=20)])
    
    email = StringField('Email', 
                        validators=[DataRequired(), Email(message='Invalid Email')])

    image = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])

    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:

            # if there is a user in the database with the same username will return ite
            # else it will just be null and conditional is Falsey
            user = User.query.filter_by(username=username.data).first()
        
            if user:
                raise ValidationError('Username is already taken. Choose a new one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            # if there is a user in the database with the same email will return ite
            # else it will just be null and conditional is Falsey
            user = User.query.filter_by(email=email.data).first()
        
            if user:
                raise ValidationError('Account with this email already exists.')

class CreatePostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])

    content = TextAreaField('Content', validators=[DataRequired()])

    submit = SubmitField('Post')