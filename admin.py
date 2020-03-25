from flask import Flask, flash, jsonify, redirect, render_template, request
app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    return render_template("index.html")
