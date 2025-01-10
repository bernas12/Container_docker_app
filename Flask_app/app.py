from flask import Flask, render_template

app = Flask(__name__)

#setting up the home page of the frontend
@app.route('/')
def frontend_page():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()