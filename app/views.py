from flask import render_template, request, redirect, url_for
from app import app
import random

# Predefined mood-based playlists
playlists = {
    "happy": ["Happy Song 1", "Happy Song 2", "Happy Song 3"],
    "sad": ["Sad Song 1", "Sad Song 2", "Sad Song 3"],
    "relaxed": ["Relaxed Song 1", "Relaxed Song 2", "Relaxed Song 3"],
    "energetic": ["Energetic Song 1", "Energetic Song 2", "Energetic Song 3"],
}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/get-mood", methods=["POST"])
def get_mood():
    if request.method == "POST":
        mood = request.form.get("mood")
        songs = playlists.get(mood.lower(), [])
        if songs:
            return render_template("result.html", mood=mood.capitalize(), songs=songs)
        return render_template("result.html", mood=mood.capitalize(), songs=["No songs found!"])
    return redirect(url_for("home"))

@app.route("/sign-up", methods=["GET","POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        return render_template("sign_up.html", email=email)
    return redirect(url_for("home"))
