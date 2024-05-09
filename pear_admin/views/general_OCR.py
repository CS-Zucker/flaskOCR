from flask import Blueprint, render_template

general_OCR_bp = Blueprint("general_OCR", __name__)


@general_OCR_bp.get("/general_OCR/word")
def general_OCR_word():
    return render_template(f"view/general_OCR/OCR_word.html")

@general_OCR_bp.get("/general_OCR/seal")
def general_OCR_seal():
    return render_template(f"view/general_OCR/OCR_seal.html")


@general_OCR_bp.get("/general_OCR/qrcode")
def general_OCR_seal():
    return render_template(f"view/general_OCR/OCR_seal.html")


@general_OCR_bp.get("/general_OCR/handwriting")
def general_OCR_seal():
    return render_template(f"view/general_OCR/OCR_seal.html")


@general_OCR_bp.get("/general_OCR/number")
def general_OCR_seal():
    return render_template(f"view/general_OCR/OCR_seal.html")


@general_OCR_bp.get("/general_OCR/bankcard")
def general_OCR_seal():
    return render_template(f"view/general_OCR/OCR_seal.html")