from flask import render_template, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app import app
from app import models
from flaskext.lesscss import lesscss

@app.route('/')
@app.route('/index')
def index():
    return render_template('layout/app.html',
    						title = 'Dashboard',
    						navBar = [ {'label' : 'Home', 'icon' : 'icon-home', 'url': 'index', 'final': True } ],
    						js = ['assets/pages/scripts/dashboard/index.js'])

@app.route('/configure')
def configure():
	return render_template('configure/table.html',
							title = "Configure parser",
							navBar = [
									{'label' : 'Home', 'icon' : 'icon-home', 'url': 'index'},
									{'label' : 'Configuration', 'final': True}
							],
							js = [
								'assets/pages/scripts/configure/index.js',
								'assets/global/plugins/bootstrap-fileinput/bootstrap-fileinput.js',
								'assets/global/plugins/ladda/spin.min.js',
								'assets/global/plugins/ladda/ladda.min.js'
							],
							css = [
								'assets/global/plugins/bootstrap-fileinput/bootstrap-fileinput.css',
								'assets/global/plugins/ladda/ladda-themeless.min.css',
								'assets/pages/css/configure/table_custom.css'
							])

@app.route('/slrParser.html')
def slrParser():
	return render_template('')

@app.route('/getRules')
def getRules():
	return jsonify(models.grammar.getRules())


@app.route('/saveMatrix', methods=['POST'])
def saveMatrix():
	# models.grammar.matrix = request.json['matrix']
	return jsonify(request.form)

