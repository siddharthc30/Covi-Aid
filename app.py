from flask import Flask, render_template, request, url_for
from twitter_resources import *
app = Flask(__name__)
@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/resource/', methods = ['POST'])
def fill_data():
    city = request.form["n1"]
    required_resource = request.form["n2"]

    tweets = get_tweets(city, required_resource)
    if len(tweets) == 0:
        return render_template('error.html')
    else:    
        return render_template('output.html', tweets = tweets)




if __name__ == '__main__':
    app.run(debug = True)


