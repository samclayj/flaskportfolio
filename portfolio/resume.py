from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, Markup
)
from werkzeug.exceptions import abort

import json
import sys

bp = Blueprint('resume', __name__)


@bp.route('/')
def index():
    return render_template('resume/resume.html')

@bp.route('/charts')
def charts():
    return render_template('charts/test-chart.html')
