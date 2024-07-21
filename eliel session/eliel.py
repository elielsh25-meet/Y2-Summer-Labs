from flask import Flask, render_template,url_for,redirect,request, session
import random



app = Flask(__name__,template_folder="templates")
app.config['SECRET_KEY'] = "eliel"
fortunes = [
    "You will find happiness soon.",
    "A great opportunity is on the horizon.",
    "Unexpected money will come your way.",
    "You will meet someone important today.",
    "Your hard work will pay off soon.",
    "Good news is coming your way.",
    "You will embark on a new adventure.",
    "Today is your lucky day!",
    "A pleasant surprise awaits you.",
    "Your creativity will bring you success."
]

@app.route('/', methods = ['GET','POST'])
def home():
	if request.method == 'GET':
		return redirect(url_for('login'))
	else:
		session['birthday'] = request.form['birthday']
		session['name']=request.form['name']
		return render_template('home.html')

@app.route('/login')
def login():
		return render_template("login.html")

@app.route('/fortune', methods = ['GET','POST'])
def fortune():
	if len(session['birthday']) > 10:
		fort = fortunes[4]
	else:
		fort = fortunes[len(session['birthday'])]
	return render_template('fortune.html',fort = fort)


if __name__ == '__main__':
    app.run(debug=True)