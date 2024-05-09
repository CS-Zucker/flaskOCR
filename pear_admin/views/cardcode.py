from flask import Blueprint, render_template

cardcode_OCR_bp = Blueprint("cardcode_OCR", __name__)


@cardcode_OCR_bp.get("/cardcode_OCR/qrcode")
def qrcode_OCR_view():
    return render_template(f"view/cardcode_OCR/qrcode.html")

@cardcode_OCR_bp.get("/cardcode_OCR/bankcard")
def bankcard_OCR_view():
    return render_template(f"view/cardcode_OCR/bankcard.html")




