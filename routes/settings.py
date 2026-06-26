from flask import Blueprint, render_template, request

settings_bp = Blueprint("settings", __name__, url_prefix="/settings")

@settings_bp.route("/", methods=["GET", "POST"])
def settings():
    if request.method == "POST":
        motd = request.form.get("motd")
        max_players = request.form.get("max_players")
        whitelist = request.form.get("whitelist")
        # For now, just print values (later you can save to DB)
        print("Updated Settings:", motd, max_players, whitelist)
    return render_template("settings.html")
