from flask import Blueprint, render_template

app_blueprint= Blueprint('app_blueprint',__name__)

#variables
content =[
    {"name":"Normal","types":"normale","images":"/image/images.jpg"},
]

@app_blueprint.route('/')
def index():
    return render_template("index.html",content=content)

@app_blueprint.route('/about')
def about():
    return render_template("about.html")

@app_blueprint.route("/contact")
def contact():
    return render_template("contact.html")