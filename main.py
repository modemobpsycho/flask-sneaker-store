from typing import Literal
from flask import Flask, render_template
from flask_login import current_user
from website import create_app

app: Flask = create_app()


@app.errorhandler(404)
def pageNotFound(error) -> tuple[str, Literal[404]]:
    return (
        render_template("page404.html", user=current_user),
        404,
    )


@app.errorhandler(400)
def badRequest(error) -> tuple[str, Literal[400]]:
    return (render_template("page400.html", user=current_user), 400)


if __name__ == "__main__":
    app.run(debug=True)
