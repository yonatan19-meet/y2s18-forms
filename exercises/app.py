from databases import *

from flask import Flask, render_template, url_for, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', students=query_all())

@app.route('/add', methods=['GET', 'POST'])
def add_student_route():
	    if request.method == 'POST':
	    	print('You just made a POST request')
	    	student_name = request.form["student_name"]
	    	student_year = request.form["year"]
	    	new_student = add_student(student_name, student_year, True)
	    	print(query_all())
	    	return render_template('student.html', student=new_student)
	    else:
	    	return render_template('add.html')
	    

@app.route('/student/<int:student_id>')
def display_student(student_id):
    return render_template('student.html', student=query_by_id(student_id))

app.run(debug=True)
