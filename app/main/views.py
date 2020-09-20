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