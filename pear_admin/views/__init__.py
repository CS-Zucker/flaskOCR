from flask import Flask

from .index import index_bp
from .system import system_bp
from .general_OCR import general_OCR_bp
from .car_detect import car_detect_bp
from .cardcode import cardcode_OCR_bp
from .image_Classify import image_Classify_bp


def register_views(app: Flask):
    app.register_blueprint(index_bp)
    app.register_blueprint(system_bp)
    app.register_blueprint(general_OCR_bp)
    app.register_blueprint(car_detect_bp)
    app.register_blueprint(cardcode_OCR_bp)
    app.register_blueprint(image_Classify_bp)
