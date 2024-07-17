from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__,template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        birth_month = request.form['birth_month']
        return redirect(url_for('fortune', birth_month=birth_month))
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

@app.route('/fortune/<birth_month>')
def fortune(birth_month):
    fortune_index = len(birth_month) % len(fortunes)
    chosen_fortune = fortunes[fortune_index]
    return render_template('fortune.html', fortune=chosen_fortune)

if __name__ == '__main__':
    app.run(debug=True)
