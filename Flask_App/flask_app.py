from flask import Flask, app
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from flask import flash
import datetime
import folium

microweb_app = Flask(__name__)

users = {'user1': 'password1', 'user2': 'password2'}

@microweb_app.route("/")
def main():
    return render_template("index.html" , datetime_now = datetime.datetime.now())

@microweb_app.route("/map")
def map():
    # Create a map centered on Brussels
    m = folium.Map(location=[50.8503, 4.3517], zoom_start=13)

    # Add a marker at the center of Brussels
    folium.Marker(location=[50.8503, 4.3517], popup='Brussels').add_to(m)

    # Render the map
    map_html = m.get_root().render()

    # Create an HTML template with the map
    return render_template('map.html', map_html=map_html)

@microweb_app.route("/time")
def time():
    return render_template("time.html")

@microweb_app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username] == password:
        return f'Welcome, {username}!'
    else:
        return 'Invalid login credentials. <a href="/">Try again</a>'

@microweb_app.route('/create', methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']

    if username in users:
        return 'Username already exists. <a href="/">Try again</a>'
    else:
        users[username] = password
        return 'Account created successfully. <a href="/">Login</a>'

if __name__ == "__main__":
    microweb_app.run(host="127.0.0.1", port=5555)