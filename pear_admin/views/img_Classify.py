from flask import Blueprint, render_template

img_Classify_bp = Blueprint("img_Classify", __name__)


@img_Classify_bp.get("/img_Classify/carDetect")
def img_Classify_word():
    return render_template(f"view/img_Classify/car_Detect.html")

@img_Classify_bp.get("/img_Classify/vehicleDetect")
def img_Classify_document():
    return render_template(f"view/img_Classify/vehicle_Detect.html")

