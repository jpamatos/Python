from flask import Flask, render_template, request
import requests

posts = requests.get("https://api.npoint.io/5b3b5d0c54af7fa025f5").json()
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", all_posts=posts)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


@app.route('/post/<int:index>')
def blog_post(index):
    post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            post = blog_post
    return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)
