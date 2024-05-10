from flask import Blueprint, render_template

image_Classify_bp = Blueprint("image_Classify", __name__)


@image_Classify_bp.get("/img_Classify/animal")
def image_Classify_animal():
    return render_template(f"view/img_Classify/animal.html")

@image_Classify_bp.get("/img_Classify/dish")
def image_Classify_eat():
    return render_template(f"view/img_Classify/dish.html")


@image_Classify_bp.get("/img_Classify/ingredient")
def image_Classify_fruit():
    return render_template(f"view/img_Classify/fruit.html")