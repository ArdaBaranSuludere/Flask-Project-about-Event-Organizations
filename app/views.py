from flask import render_template, redirect, url_for, request, flash
from app import app, db

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/tickets.html')
def tickets():
    return render_template('tickets.html')

@app.route('/ticket-details.html')
def ticket_details():
    return render_template('ticket-details.html')

@app.route('/shows-events.html')
def shows_events():
    return render_template('shows-events.html')

@app.route('/event-details.html')
def event_details():
    return render_template('event-details.html')

@app.route('/rent-venue.html')
def rent_venue():
    return render_template('rent-venue.html')
