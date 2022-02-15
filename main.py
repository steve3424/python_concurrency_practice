import itertools
from flask import Flask,request,Response
import requests

app = Flask(__name__)

from concurrent import futures
import random, time

final_posts = []

def make_request():
    print("start")
    time.sleep(4)
    # response = requests.get("https://api.hatchways.io/assessment/blog/posts", params={"tag" : t})
    print("end")
    # final_posts.append(response.json()["posts"])

@app.route("/api/posts", methods=["GET"])
def API_Posts():
    start_time = time.perf_counter()

    # Validate tags param
    tags = request.args.get("tags")
    if not tags:
        return {"error" : "Tags parameter is required"}, 400
    tags = tags.split(",")

    # Validate sortBy param
    valid_sorts = set(["id", "reads", "likes", "popularity"])
    sort_by = request.args.get("sortBy")
    if not sort_by:
        sort_by = "id"
    elif sort_by not in valid_sorts:
        return {"error" : "sortBy parameter is invalid"}, 400
    
    # Validate direction param
    valid_directions = set(["asc", "desc"])
    direction = request.args.get("direction")
    if not direction:
        direction = "asc"
    elif direction not in valid_directions:
        return {"error" : "direction parameter is invalid"}, 400

    # Call API and process results
    posts_added = set()
    l = [1,2,3]
    with futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(make_request(), l)
    return {"s" : "s"}
    # for t in tags:
    #     response = requests.get("https://api.hatchways.io/assessment/blog/posts", params={"tag" : t})
    #     if not response.ok:
    #         return {"error" : "Something went wrong"}, 400
    #     requested_posts = response.json()["posts"]
    #     for post in requested_posts:
    #         id = post["id"]
    #         if id not in posts_added:
    #             final_posts.append(post)
    #             posts_added.add(id)
    # if sort_by:
    #         final_posts = sorted(final_posts, key=lambda p: p[sort_by], reverse=direction == "desc")

    # end_time = time.perf_counter()
    # print(f"TIMING: {end_time - start_time}")
    # return {"posts" : final_posts}

if __name__ == "__main__":
    app.run(debug=True)
