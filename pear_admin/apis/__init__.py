from flask import Blueprint, Flask

from .passport import passport_api
from .rights import rights_api
from .role import role_api
from .user import user_api
from .general_OCR import general_OCR_api
from .car_detect import car_detect_api
from .cardcode_OCR import cardcode_OCR_api
from .img_Classify import img_Classify_api



def register_apis(app: Flask):
    apis = Blueprint("api", __name__, url_prefix="/api/v1")

    apis.register_blueprint(passport_api)
    apis.register_blueprint(rights_api)
    apis.register_blueprint(role_api)
    apis.register_blueprint(user_api)
    apis.register_blueprint(general_OCR_api)
    apis.register_blueprint(car_detect_api)
    apis.register_blueprint(cardcode_OCR_api)
    apis.register_blueprint(img_Classify_api)

    app.register_blueprint(apis)
