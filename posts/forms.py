from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField,SelectField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    problem = StringField('Problem Name', validators=[DataRequired()])
    url = StringField('Url', validators=[DataRequired()])
    language= SelectField('Language', choices=[('Python','Python'),('C++','C++'),('C','C'),
    	('Java','Java'),('Javascript','Javascript')])
    platform= SelectField('Platform', choices=[('Spoj','Spoj'),('Codechef','Codechef'),('Codeforces','Codeforces')
    	,('Hackerrank','Hackerrank'),('Leetcode','Leetcode')])
    code = TextAreaField('Code', validators=[DataRequired()])
    submit = SubmitField('Post')

    
