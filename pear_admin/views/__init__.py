from flask import Flask

from .index import index_bp
from .system import system_bp
from .general_OCR import general_OCR_bp


def register_views(app: Flask):
    app.register_blueprint(index_bp)
    app.register_blueprint(system_bp)
    app.register_blueprint(general_OCR_bp)