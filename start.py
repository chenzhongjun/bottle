#! /usr/bin/env python

from bottle import Bottle, run, error, response
from bottle import template, static_file, request

response.set_header("Set_Cookie", "name=visited")

app = Bottle()
@app.route("/<filename>")
def server_static(filename):
    return static_file(filename, root = "/home/zhongjun/projects/bottle/")

@app.route("/hello/<name>")
def greet(name = "Stranger"):
    return template("hello {{ name }}, how are you?", name = name)

@app.error(404)
def error404(error):
    return "Nothing here, sorry"

@app.route("/hello")
def hello_again():
    if request.get_cookie("visited"):
        return "welcom back, nice to see you again"
    else:
        response.set_cookie("visited", "yes", "max_age = 1200")
        return "hello, there, Nice to meet you"

@app.route("/is_ajax")
def is_ajax():
    if request.headers.get("X-Request-With") == "XMLHttpRequest":
        return "this is ajax request"
    else:
        return "this is a normal request"
run(app, host = "localhost", port = 8011, debug = True)
