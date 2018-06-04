from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, Markup
)
from werkzeug.exceptions import abort

import json
import sys

from charts import Chart, ChartTypes

bp = Blueprint('resume', __name__)


@bp.route('/')
def index():
    return render_template('resume/resume.html')

@bp.route('/charts')
def charts():
    labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July']
    data = [0, 10, 5, 2, 20, 30, 45]
    data2 = [0, 20, 1, 8, 30, 50, 25]

    bubbleData = [{'x': 1, 'y': 10, 'r': 50}, {'x': 2, 'y': 10, 'r': 30}]

    chart = Chart(ChartTypes.LINE)
    chart.set_labels(labels)
    chart.create_and_add_dataset(
            label='First dataset',
            bgColor='blue',
            borderColor='green',
            data=data)

    chart.create_and_add_dataset(
            label='Second dataset',
            bgColor='rgb(255, 99, 132)',
            borderColor='rgb(255, 99, 132)',
            data=data2)


    bubbleChart = Chart(ChartTypes.BUBBLE)
    bubbleChart.create_and_add_dataset(
            label='Bubble dataset',
            bgColor='blue',
            borderColor='green',
            data=bubbleData)

    return render_template('charts/test-chart.html',
            chart=chart.get_nonescaped_json(),
            bubbleChart=bubbleChart.get_nonescaped_json())
