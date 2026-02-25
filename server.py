from flask import Flask, request, send_file
import subprocess

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def upload():
    if request.method == "POST":
        f = request.files["file"]
        f.save("input")

        subprocess.run(["ffmpeg", "-i", "input", "output.mp3"])

        return send_file("output.mp3", as_attachment=True)

    return '''
    <form method="post" enctype="multipart/form-data">
    <input type="file" name="file">
    <input type="submit">
    </form>
    '''

app.run(host="0.0.0.0", port=10000)
