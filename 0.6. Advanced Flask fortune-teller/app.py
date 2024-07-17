from flask import Flask, render_template
import random

app = Flask(__name__, template_folder = 'templates')


@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html')


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


@app.route('/fortune')
def fortune():
    random_fortune = random.choice(fortunes)
    return render_template('fortune.html', fortune=random_fortune)

if __name__ == '__main__':
    app.run(debug=True)
