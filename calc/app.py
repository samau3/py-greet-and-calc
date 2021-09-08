from flask import Flask, request
import operations

app = Flask(__name__)


@app.get('/add')
def addition():
    """Return sum of query string args"""
    [a, b] = [request.args["a"], request.args["b"]]
    return str(operations.add(int(a), int(b)))


@app.get('/sub')
def subtraction():
    """Return difference of query string args"""
    [a, b] = [request.args["a"], request.args["b"]]
    return str(operations.sub(int(a), int(b)))


@app.get('/mult')
def multiplication():
    """Return product of query string args"""
    [a, b] = [request.args["a"], request.args["b"]]
    return str(operations.mult(int(a), int(b)))


@app.get('/div')
def division():
    """Return quotient of query string args"""
    [a, b] = [request.args["a"], request.args["b"]]
    return str(operations.div(int(a), int(b)))


@app.get('/math/<operation>')
def math(operation):
    """Return result of chosen math operation from the query string args"""
    [a, b] = [int(request.args["a"]), int(request.args["b"])]

    op_query = {
        "add": operations.add,
        "sub": operations.sub,
        "mult": operations.mult,
        "div": operations.div
    }

    return str(op_query[operation](a, b))
