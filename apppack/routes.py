import functools
from flask import render_template, Blueprint, redirect

bp = Blueprint('routes', __name__, url_prefix='')

from .static.icons import iconList

from . import pageContent


@bp.route('/', methods=(['GET']))
def index():
    return redirect('home')


@bp.route('/home', methods=(['GET']))
def home():
    data = pageContent.home
    return render_template('home.html', data=data)


@bp.route('/projects', methods=(['GET']))
def projects():
    data = pageContent.projects
    return render_template('projects.html', data=data)


@bp.route('/fun', methods=(['GET']))
def fun():
    data = pageContent.fun
    return render_template('fun.html', data=data)


@bp.route('/contact', methods=(['GET']))
def contact():
    data = pageContent.contact
    return render_template('contact.html', data=data)

@bp.route('/math', methods=(['GET']))
def math():
    data = pageContent.math
    return render_template('math.html', data=data)