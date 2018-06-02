from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

bp = Blueprint('resume', __name__)


@bp.route('/')
def index():
    return render_template('resume/resume.html')
