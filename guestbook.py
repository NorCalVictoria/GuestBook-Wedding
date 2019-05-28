from flask import Flask, render_template
 
app = Flask(__name__)

@app.route('/')				#default endpoint
def index():
	return render_template('index.html')

@app.route('/sign')
def sign():
	return render_template('sign.html')

@app.route('/home', methods=['GET','POST'])
def home():
	links = ['http://www.victoria-duncan.com', 'https://lifehacker.com', 'https://aws.com']
	return render_template('example.html', links=links)


if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)