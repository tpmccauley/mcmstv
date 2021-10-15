import csv
import json

from flask import (
    Flask,
    render_template
)

from flask_bootstrap import (
    Bootstrap
)

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template(
        'index.html',
        title='CMS TV',
    )

@app.route('/lhc_status')
def lhc_status():
    return render_template(
        'lhc_status.html',
        title='LHC Status'
    )

@app.route('/lhc_luminosity')
def lhc_luminosity():
    return render_template(
        'lhc_luminosity.html',
        title='LHC Luminosity'
    )

@app.route('/cms_status')
def cms_status():
    return render_template(
        'cms_status.html',
        title='CMS Status'
    )

@app.route('/daq_status')
def daq_status():
    return render_template(
        'daq_status.html',
        title='DAQ Status'
    )

@app.route('/live_event_display')
def live_event_display():
    return render_template(
        'live_event_display.html',
        title='Live Event Display'
    )

@app.route('/about')
def about():
    return render_template(
        'about.html',
        title='About'
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
