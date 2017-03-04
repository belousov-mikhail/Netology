from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Trial website for my homerwork"

@app.route('/about')
def about():
    return "This website created by me"

if __name__ == "__main__":
    app.run (debug=False)





