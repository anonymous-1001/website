from flask import Flask
from blueprint import app_blueprint

app = Flask(__name__,static_folder="./images")
app.register_blueprint(app_blueprint)
