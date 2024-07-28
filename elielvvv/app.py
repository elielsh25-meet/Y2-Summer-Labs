from flask import Flask, render_template, request, redirect, url_for, session as login_session
import pyrebase
import random


firebaseConfig = {
  "apiKey": "AIzaSyDhq9K5lFRDsGNldfU19u19IYjKLDSyUg4",
  "authDomain": "wishes-d7cff.firebaseapp.com",
  "projectId": "wishes-d7cff",
  "storageBucket": "wishes-d7cff.appspot.com",
  "messagingSenderId": "987112919168",
  "appId": "1:987112919168:web:bd271f2d043f0e390dd665",
  "databaseURL":""}

app = Flask(__name__,template_folder='templates', static_folder = 'static')
app.config['SECRET_KEY'] = 'eliel'

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
auth = firebase.auth()

# @app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        return render_template('home.html')
    else:
        return render_template('home.html')


# @app.route('/login', methods = ['GET', 'POST'])
# def login():
#     if request.method=='POST':
#         email = request.form['email']
#         # user = request.form['user name']
#         password = request.form['password']
#     else:
#         return render_template('main.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            user = auth.sign_in_with_email_and_password(email, password)
            # Assuming successful login, store user information in session
            login_session['user'] = user
            return redirect(url_for('home'))
        except:
            error = 'Invalid credentials. Please try again.'
            return render_template('main.html', error=error)
    else:
        return render_template('main.html')


# @app.route('/signup', methods = ['GET', 'POST'])
# def signup():
#     if request.method=='GET':
#         return render_template('main.html')
#     else:
#         email = request.form['email']
#         # user = request.form['user name']
#         password = request.form['password']

#         login_session['email'] = email
#         login_session['password'] = password


#         login_session['user'] = auth.create_user_with_email_and_password(email, password)
#         user_id = login_session['user']['localId']
#         user = {
#         'email' : email,
#         'password' : password
#         }
#         db.child('Users').child(user_id).set(user)
#         return render_template('main.html')
#         # user = auth.user_with_email_and_password(email, password)
#     # return render_template('main.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            auth.create_user_with_email_and_password(email, password)
            user = {
                'email': email,
                'password': password
            }
            db.child('Users').push(user)
            return redirect(url_for('main'))  # Redirect to a different endpoint after signup
        except:
            return render_template('home.html')
    else:
      m=  return render_template('main.html')

@app.route('/givewish', methods=['GET','POST'])
def givewish():
    randomwish=random.choice(['hello,May your love grow stronger with each passing day Filled with joy and laughter along the way.','Wishing you a lifetime of happiness and bliss','A journey together filled withh loves sweet kiss','heres to love laughter and hapily ever after May your life be full xf joy and laughter may','as you start this new chapter hand in hand may love and understanding alwas stand'])
    return render_template('givewish.html', randomwish = randomwish)

@app.route('/wishes', methods = ['GET', 'POST'])
def wishes():
    if request.method=='POST':
        return redirect(url_for(''))
    else:
        return render_template('wishes.html')
        # user = auth.user_with_email_and_password(email, password)
    # return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)
