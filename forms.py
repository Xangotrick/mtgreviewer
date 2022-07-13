from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    submitminus1 = SubmitField("-1")
    submit0 = SubmitField("0")
    submit1 = SubmitField("1")
    submit2 = SubmitField("2")
    submit3 = SubmitField("3")
    submit4 = SubmitField("4")
    submit5 = SubmitField("5")
    submit6 = SubmitField("6")
    submit7 = SubmitField("7")
    submit8 = SubmitField("8")
    submit9 = SubmitField("9")
    submit10 = SubmitField("10")
    submit99 = SubmitField("99")
    submitminus2 = SubmitField("-2")
