from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy  #to instanciate db object

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://sql3293764:2suthnErUU@sql3.freemysqlhosting.net/sql3293764'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app) # instanciate the database object


class Comments(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(28))
	comment = db.Column(db.String(1000))



@app.route('/')				#default endpoint
def index(): 
	result = Comments.query.all()    #utilize sqlAlchemy to retrieve from db

	return render_template('index.html', result=result)

@app.route('/sign')
def sign():
	return render_template('sign.html')

@app.route('/process', methods=['POST'])
def process():
	name = request.form['name']
	comment = request.form['comment'] #request object takes many types of request data . in this case its form data

	signature = Comments(name=name, comment=comment) #creating a row by entanciating the object
	db.session.add(signature) # add row to db
	db.session.commit()			# save update to db

	# return 'Name is : ' + name + 'and the comment is : ' + comment       <--- testing name and comment POST
	#return render_template('index.html', name=name, comment=comment)
	return redirect(url_for('index')) #redirct signer to the index after posting
@app.route('/home', methods=['GET','POST'])
def home():
	links = ['http://www.victoria-duncan.com', 'https://lifehacker.com', 'https://aws.com']
	return render_template('example.html', links=links)


if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)