from flask import render_template, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('dashboard_home.html', title = 'Parser')