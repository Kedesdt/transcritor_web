from flask import Flask

app = Flask(__name__)

from server.routes import (
    app_routes,
)  # Import the app_routes module to register the routes
