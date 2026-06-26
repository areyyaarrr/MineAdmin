from flask import Flask
from routes.dashboard import dashboard_bp
from routes.players import players_bp
from routes.auth import auth_bp
from routes.settings import settings_bp

app = Flask(__name__)
app.config.from_object("config")

# Register blueprints
app.register_blueprint(dashboard_bp)
app.register_blueprint(players_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(settings_bp)

if __name__ == "__main__":
    app.run(debug=True)
