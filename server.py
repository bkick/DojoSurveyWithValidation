from flask import Flask, render_template, request, redirect, flash
import re
app= Flask(__name__)
app.secret_key='swag'
@app.route('/', methods=['GET'])
def index():
	return render_template("index.html")

@app.route('/result', methods=['POST'])
def create_user():
	if len(request.form['comment'])<1:
		flash('Comment cannot be blank')
		return redirect('/')
	elif len(request.form['comment'])>120:
		flash('Comment must be less than 120 characters')
		return redirect('/')
	else:	
		print("Got Post Info")
		print (request.form)
		name=request.form['name']
		dojo=request.form['dojo']
		lang=request.form['lang']
		comment=request.form['comment']
		return render_template('submit.html', name=name, lang=lang, dojo=dojo, comment=comment)
@app.route('/danger')
def danger():
	print("a user tried to visit /danger. we have redirected the user to /")
	return redirect('/')
if __name__=="__main__":
	app.run(debug=True)