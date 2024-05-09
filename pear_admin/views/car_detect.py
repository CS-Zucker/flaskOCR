from flask import Blueprint, render_template

car_detect_bp = Blueprint("car_detect", __name__)


@car_detect_bp.get("/car_detect/car")
def car_detect_view():
    return render_template(f"view/car_detect/car.html")

@car_detect_bp.get("/car_detect/vehicle")
def vehicle_detect_view():
    return render_template(f"view/car_detect/vehicle.html")

