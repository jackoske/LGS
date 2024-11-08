from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    collections = [
    {
        "name": "CDisko65 & PNF - W.MC.A.",
        "description": "",
        "url": "https://youtu.be/qB06eSObXaI?si=yZWRNmKMq0kIiAua",
        "image": "https://img.youtube.com/vi/qB06eSObXaI/0.jpg"  # YouTube video thumbnail
    },
    {
        "name": "PNF - Big Sofo (prod. Avatos)",
        "description": "",
        "url": "https://youtu.be/LyARPaCOVJY?si=ZNNJA3s_vR81uCsO",
        "image": "https://img.youtube.com/vi/LyARPaCOVJY/0.jpg"  # YouTube video thumbnail
    },
    # Add more c
    ]
    return render_template("home.html", collections=collections)

if __name__ == "__main__":
    app.run(debug=True)
