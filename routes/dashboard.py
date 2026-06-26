from flask import Blueprint, render_template
from services.minecraft import get_server_status
from services.monitoring import get_system_stats

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/")
def dashboard():
    server_status = get_server_status()
    system_stats = get_system_stats()
    return render_template("dashboard.html",
                           server=server_status,
                           stats=system_stats)
