from flask import Blueprint, render_template, request, redirect, url_for

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # For now, just accept any username/password
        username = request.form.get("username")
        password = request.form.get("password")
        if username and password:
            return redirect(url_for("dashboard.dashboard"))
        else:
            return render_template("login.html", error="Invalid credentials")
    return render_template("login.html")
