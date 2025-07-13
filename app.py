from flask import Flask, request, render_template
import qrcode
import base64
from io import BytesIO
#from vercel_wsgi import handle_request  # Required for Vercel

app = Flask(__name__, template_folder="templates")

@app.route("/", methods=["GET", "POST"])
def home():
    qr_base64 = None
    if request.method == "POST":
        data = request.form["data"]
        img = qrcode.make(data)

        # Save image to memory instead of disk
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        qr_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")

    return render_template("index.html", qr_base64=qr_base64)

# if __name__ == "__main__":
#     app.run(debug=True)