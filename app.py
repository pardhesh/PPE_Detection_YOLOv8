import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, Response
from ultralytics import YOLO
import cv2
from pathlib import Path

# Flask setup
app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
RESULT_FOLDER = "static/results"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

# Load your best model
model = YOLO("best.pt")   # make sure best.pt is in same folder

# Home page
@app.route("/")
def index():
    return render_template("index.html")

# File upload handler
@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return redirect(url_for("index"))

    file = request.files["file"]
    if file.filename == "":
        return redirect(url_for("index"))

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    # Run YOLO inference
    results = model(filepath, save=True, project=RESULT_FOLDER, name="detect", exist_ok=True)
    
    # Grab YOLO’s auto-saved file
    save_dir = Path(results[0].save_dir)   # convert to Path object
    result_path = list(save_dir.glob("*"))[0]
    result_file = result_path.name

    return render_template("result.html", result_file=result_file)

# Download handler
@app.route("/download/<filename>")
def download(filename):
    return send_from_directory(os.path.join(RESULT_FOLDER, "detect"), filename, as_attachment=True)

# Webcam generator
def gen_frames():
    cap = cv2.VideoCapture(0)  # webcam
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            results = model(frame)
            annotated = results[0].plot()

            # Encode as JPEG
            _, buffer = cv2.imencode(".jpg", annotated)
            frame_bytes = buffer.tobytes()

            yield (b"--frame\r\n"
                   b"Content-Type: image/jpeg\r\n\r\n" + frame_bytes + b"\r\n")

# Webcam route
@app.route("/webcam")
def webcam():
    return Response(gen_frames(),
                    mimetype="multipart/x-mixed-replace; boundary=frame")

if __name__ == "__main__":
    app.run(debug=True)
