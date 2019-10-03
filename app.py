"""
Luz Glass (OCR)
A world made with words for those visually impaired or blinds.
"""
import os
from flask import Flask, jsonify, request, url_for, render_template
import urllib.request
from flask_cors import CORS
import re, time, base64
from io import BytesIO

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

def sky_ocr(filename):
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(Image.open(filename))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text  # Then we will print the text in the image


# Convert Base64 Image to PNG
def getI420FromBase64(codec):
    print(codec)
    base64_data = re.sub('^data:image/.+;base64,', '', codec)
    byte_data = base64.b64decode(base64_data)
    image_data = BytesIO(byte_data)
    img = Image.open(image_data)
    t = time.time()
    img.save('images/temp.png', "PNG")

app = Flask(__name__, static_url_path='/static')
CORS(app)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/api', methods=['GET', 'POST'])
def ocr_api():
    post_content = request.args.get('url')
    if not request.args.get('url'):
        post_content = request.form['url']
    if not post_content:
        return jsonify({"Error": 'No URL entered'})
    try:
        getI420FromBase64(request.form['url'])
        extracted_text = sky_ocr('images/temp.png')
        return jsonify({"data": extracted_text})
    except Exception as e:
        return jsonify({"Error": 'There was an error while processing your request. ' + str(e)})

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5005)
