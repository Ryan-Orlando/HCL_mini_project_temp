from flask import Flask
from blueprint import blueprint

# flask appp
app = Flask(__name__)

# blueprint
app.register_blueprint(blueprint, url_prefix='/')

# running the flask app
if __name__ == '__main__':
    app.run(debug=True)