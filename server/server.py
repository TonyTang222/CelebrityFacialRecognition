from flask import Flask, request, jsonify
import util

app = Flask(__name__)


@app.route('/classify_image', methods=['GET', 'POST'])
def classify_image():
    image_data = request.form['image_data']

    response = jsonify(util.classify_image(image_data))

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

'''
@app.route('/', methods=['GET'])
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Blackpink Facial Classifier</title>
    </head>
    <body>
        <h1>Blackpink Facial Classifier</h1>
        <form action="/classify_image" method="post" enctype="multipart/form-data">
            <input type="file" id="imageInput" onchange="encodeImage()" accept="image/*">
            <input type="hidden" name="image_data" id="imageData">
            <input type="submit" value="Classify">
        </form>

        <script>
            function encodeImage() {
                const fileInput = document.getElementById('imageInput');
                const file = fileInput.files[0];

                if (file) {
                    const reader = new FileReader();
                    reader.onload = function(e) {
                        const base64Data = e.target.result.split(',')[1];
                        document.getElementById('imageData').value = base64Data;
                    };
                    reader.readAsDataURL(file);
                }
            }
        </script>
    </body>
    </html>
    """
'''

if __name__ == "__main__":
    print("Starting Python Flask Server For BLACKPINK Member Image Classification")
    util.load_saved_artifacts()
    app.run(port=5001)