from flask import Flask, request, render_template
from utils import search_web, search_images, search_videos, search_news, search_forum

app = Flask(__name__)

@app.route("/")
def index():
    query = request.args.get("query","")
    search_type = request.args.get("type","web")
    page = int(request.args.get("page",1))
    per_page = 10
    results, total_results = [], 0

    if query:
        if search_type == "web":
            results, total_results = search_web(query, page, per_page)
        elif search_type == "images":
            results, total_results = search_images(query, page, per_page)
        elif search_type == "videos":
            results, total_results = search_videos(query, page, per_page)
        elif search_type == "news":
            results, total_results = search_news(query, page, per_page)
        elif search_type == "forum":
            results, total_results = search_forum(query, page, per_page)

    return render_template("index.html",
                           query=query,
                           search_type=search_type,
                           results=results,
                           page=page,
                           per_page=per_page,
                           total_results=total_results)

if __name__ == "__main__":
    app.run(debug=True)

