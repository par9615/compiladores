from flask import render_template, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app import app
import os
from ascendantAnalysis.grammar import Grammar
from ascendantAnalysis.ascendantAnalyzer import languagePattern

grammar = Grammar(grammarPattern)

@app.route('/')
@app.route('/index')
def index():
    return render_template('layout/app.html',
    						title = 'Dashboard',
    						navBar = [ {'label' : 'Home', 'icon' : 'icon-home', 'url': 'index', 'final': True } ],
    						js = ['assets/pages/scripts/dashboard/index.js'])

@app.route('/configure')
def configure():
	return render_template('configure/index.html',
							title = "Configure parser",
							navBar = [
									{'label' : 'Home', 'icon' : 'icon-home', 'url': 'index'},
									{'label' : 'Configuration', 'final': True}
							],
							js = [
								'assets/pages/scripts/configure/index.js',
								'assets/global/plugins/bootstrap-fileinput/bootstrap-fileinput.js'
							],
							css = [
								'assets/global/plugins/bootstrap-fileinput/bootstrap-fileinput.css'
							])

@app.route('/slrParser.html')
def slrParser():
	return render_template('')

@app.route('/getRules')
def getRules():
	return grammar.getRules()


@app.route('/saveMatrix', methods=['POST'])
def saveMatrix():
	grammar.matrix = request.matrix
	return json.dumps({'success':True}), 200, {'ContentType' : 'application/json'}

