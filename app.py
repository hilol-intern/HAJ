from flask import Flask, render_template, request, flash
import info


app = Flask(__name__)
app.secret_key = "super secret key"

@app.route('/')
def main():
    lang_info = info.uz_lotin
    return render_template('index.html', information = lang_info)

@app.route('/uz')
def main_lt():
    lang_info = info.uz_ciril
    return render_template('index.html', information = lang_info)