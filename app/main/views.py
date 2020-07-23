from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required,current_user
# from .. request import get_random_quote,subscribe_user
from .. import db,photos
from . import main
# from . forms import Post_Form,CommentsForm,SubscribeUserForm
# from ..models import User,Post,Comment,PhotoProfile,PostPhoto,Subscribed

@main.route('/', methods = ["GET","POST"])
def index():
    '''
    function that define route to index page
    '''
    return render_template('index.html')

