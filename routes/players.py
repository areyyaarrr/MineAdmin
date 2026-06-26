from flask import Blueprint, render_template

players_bp = Blueprint("players", __name__, url_prefix="/players")

@players_bp.route("/")
def players():
    return render_template("players.html")
