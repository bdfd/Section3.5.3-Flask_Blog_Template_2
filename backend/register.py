'''
Date         : 2022-09-12 17:54:43
Author       : BDFD,bdfd2005@gmail.com
Github       : https://github.com/bdfd
LastEditTime : 2022-09-13 10:27:14
LastEditors  : BDFD
Description  : 
FilePath     : \backend\register.py
Copyright (c) 2022 by BDFD, All Rights Reserved. 
'''
from flask import Blueprint, render_template
from Component.forms import SignUpForm

register = Blueprint("register", __name__, static_folder="static", template_folder="templates")

@register.route('/')
def index():
  return render_template('index.html')

@register.route("/signup")
def reghome():
    form = SignUpForm()
    return render_template('signup.html', form=form)
