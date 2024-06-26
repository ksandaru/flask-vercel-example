from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "Flask Vercel Example App by Kanishka", 200


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"status": 404, "message": "Not Found"}), 404
