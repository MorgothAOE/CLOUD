from flask import render_template


def not_found_error(e):
    kwargs = {
        "error_name": "404 Not Found Error",
        "error_description": "La url a la que queres accceder no existe."
    }
    return render_template("error.html", **kwargs), 404


def unauthorized(e):
    kwargs = {
        "error_name": "401 Unauthorized",
        "error_description": "No posee acceso a la url solicitada."
    }
    return render_template("error.html", **kwargs), 401
