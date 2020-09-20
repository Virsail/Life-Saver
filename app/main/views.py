from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from . import main 
from flask_login import login_required, current_user
from .forms import UpdateProfile, GeneralForm, GeneralReviewForm, SaleForm, SaleReviewForm, SeductionForm, SeductionReviewForm, MusicForm, MusicReviewForm, ProjectForm, ProjectReviewForm, InterviewForm, InterviewReviewForm, AdvertisementForm, AdvertisementReviewForm
from .. import db
from sqlalchemy import func
from ..models import User, Interview, Advertisement, Project, Music, Sale, Seduction, General, ReviewAdvertisement, ReviewGeneral, ReviewInterview, ReviewMusic, ReviewProject, ReviewSale, ReviewSeduction, Upvote, Downvote

@main.route('/')
def index():
    """
    View root page function that returns the index page and its data
    """
    title = 'Home - Welcome to The Pitch website'

    return render_template('index.html', title=title)


@main.route('/user/<uname>/update', methods=['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)

         form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname=user.username))

    return render_template('profile/update.html', form=form)


@main.route('/',methods = ['GET', 'POST'])

def index():

    '''
    View root page function that returns the index page and its data
    '''
    general = Pitch.query.filter_by(category="general").order_by(Pitch.posted.desc()).all()
    project = Pitch.query.filter_by(category="project").order_by(Pitch.posted.desc()).all()
    advertisement = Pitch.query.filter_by(category="advertisement").order_by(Pitch.posted.desc()).all()
    sale = Pitch.query.filter_by(category="sale").order_by(Pitch.posted.desc()).all()

    pitch = Pitch.query.filter_by().first()
    likes = Like.get_all_likes(pitch_id=Pitch.id)
    dislikes = Dislike.get_all_dislikes(pitch_id=Pitch.id)


     title = 'Home | One Min Pitch'
    return render_template('index.html', title = title, pitch = pitch, general = general, project = project, advertisement = advertisement, sale = sale, likes=likes, dislikes=dislikes)



@main.route('/user/<uname>')
def profile(uname):
    '''
    View profile page function that returns the profile page and its data
    '''
    user = User.query.filter_by(username = uname).first()
    title = f"{uname.capitalize()}'s Profile"

    get_pitches = Pitch.query.filter_by(author = User.id).all()
    get_comments = Comment.query.filter_by(user_id = User.id).all()
    get_likes = Like.query.filter_by(user_id = User.id).all()
    get_dislikes = Dislike.query.filter_by(user_id = User.id).all()

    if user is None:
        abort (404) 

    return render_template("profile/profile.html", user = user, title=title, pitches_no = get_pitches, comments_no = get_comments, likes_no = get_likes, dislikes_no = get_dislikes)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    '''
    View update profile page function that returns the update profile page and its data
    '''
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

  