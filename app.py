from flask import Flask, render_template

app = Flask(__name__)

@app.route('/test')
def test_page():
   return render_template ('index.html', test = True)

@app.route('/')
@app.route('/<user>')
def default_name(user = 'Anonymus'):
   return render_template('index.html', name = user)

if __name__ == '__main__':
   app.run(debug = True)





