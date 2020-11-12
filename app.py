import datetime
import json
import os
from flask import Flask, flash, render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
from venmo_api import random_device_id
import venmo_request
app = Flask(__name__)

with open("sensitive.txt", "r") as handle:
    data = handle.read()

config = json.loads(data)
secret = config["secret"]

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.secret_key = secret
db = SQLAlchemy(app)

app.config["IMAGE_UPLOADS"] = "static/images"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.String(60), nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    access_token = db.Column(db.String(120), unique=True, nullable=False)
    title = db.Column(db.String(120), unique=False, nullable=False)
    description = db.Column(db.Text, unique=False, nullable=False)
    goal = db.Column(db.Float, unique=False, nullable=False)
    min_contribution = db.Column(db.Float, unique=False, nullable=False)
    last_updated = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    image_location = db.Column(db.String(120), default='venmo_logo.jpg')
    donations = db.relationship('Donations', backref='post', lazy=True)

    def __repr__(self):
        return '<Post %r>' % self.image_location


class Donations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)


@app.route("/")
def index():
    posts = Post.query.all()
    return render_template("index.html", posts=posts)


@app.route("/create", methods=["POST", "GET"])
def create():
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            image.save(os.path.join(
                app.config["IMAGE_UPLOADS"], image.filename))
            session["image"] = image.filename
        session["title"] = request.form["title"]
        session["description"] = request.form["description"]
        session["goal"] = request.form["goal"]
        session["min_contribution"] = request.form["min_contribution"]
        return redirect("/login")

    return render_template("create.html")


@app.route("/crowdmo/<id>", methods=["POST", "GET"])
def crowdmo(id):
    # check the last time a post was updated, and if it has been greater than 2 hours, update again
    post = Post.query.filter_by(id=id).first()
    if datetime.datetime.utcnow().hour - post.last_updated.hour > 2:
        print("UPDATING DONORS")
        donors = venmo_request.update_contributors(
            search_note=post.title, access_token=post.access_token, creation_date=post.last_updated)
        for donor in donors.keys():
            new_donor = Donations(
                username=donor, amount=donors[donor], post_id=post.id)
            db.session.add(new_donor)
        post.last_updated = datetime.datetime.utcnow()
        db.session.commit()

    # create dictionary of donors from database
    donors = dict()
    for donation in post.donations:
        donors[donation.username] = donation.amount
    progress = venmo_request.calc_progress_to_goal(donors=donors)

    if request.method == "POST":
        venmo_username = request.form["venmo_username"]
        friend_id = venmo_request.find_user_for_request(
            venmo_username, post.access_token)
        if friend_id != False:
            venmo_request.request_friend(
                user_id=friend_id, min_amount=post.min_contribution, access_token=post.access_token, note=post.title)
    return render_template("crowdfund.html", post=post, progress=progress, donors=donors)


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        session["device_id"] = random_device_id()
        otp_secret = venmo_request.venmo_get_otp(
            username, password, session["device_id"])
        session["username"] = username
        session["password"] = password
        session["otp_secret"] = otp_secret

        print(f"storing otp_secret in session={session['otp_secret']}")
        return redirect("/two_factor")
    return render_template("login.html")


@app.route("/two_factor", methods=["POST", "GET"])
def two_factor():
    if "otp_secret" in session:
        if request.method == "POST":
            session["otp_code"] = request.form["otp_code"]
            print(
                f"two_factor using: otp_code={session['otp_code']}    otp_secret={session['otp_secret']}")
            session["access_token"] = venmo_request.venmo_get_access_token(
                otp_secret=session["otp_secret"], otp_code=session["otp_code"], device_id=session["device_id"])
            print(f"access token: {session['access_token']}")
            create_post()
            return "Success"
        return render_template("two_factor.html")
    flash("You must input a username and password first to do that!")
    return redirect("/login")


def create_post():
    if session["access_token"] != None:
        newPost = Post(access_token=session["access_token"], title=session["title"], image_location="images/" + session["image"],
                       owner=session["username"], description=session["description"], goal=session["goal"], min_contribution=session["min_contribution"])
        db.session.add(newPost)
        db.session.commit()


if __name__ == "__main__":
    db.create_all()
