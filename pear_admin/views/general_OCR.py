from flask import Blueprint, render_template

general_OCR_bp = Blueprint("general_OCR", __name__)


@general_OCR_bp.get("/general_OCR/word")
def general_OCR_word():
    return render_template(f"view/general_OCR/OCR_word.html")

@general_OCR_bp.get("/general_OCR/document")
def general_OCR_document():
    return render_template(f"view/general_OCR/OCR_document.html")

