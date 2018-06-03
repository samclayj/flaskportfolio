from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

import json

bp = Blueprint('resume', __name__)


@bp.route('/')
def index():
    return render_template('resume/resume.html')

@bp.route('/charts')
def charts():
    labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July']
    json_data = json.dumps([1,2,3,{'4': 5, '6': 7}], separators=(',',':'))
    return render_template('charts/test-chart.html', data=json_data)
