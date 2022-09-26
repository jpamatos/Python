from flask import Flask, render_template
import requests
from post import Post

response = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
posts = []
for post in response:
    post_object = Post(post["id"], post["title"], post["subtitle"],
                       post["body"])
    posts.append(post_object)

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts=posts)


@app.route('/post/<int:index>')
def blog_post(index):
    post = None
    for blog_post in posts:
        if blog_post.id == index:
            post = blog_post
    return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)
