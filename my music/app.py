from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    # Process registration data (e.g., save to database)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
