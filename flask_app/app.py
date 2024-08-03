from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

@app.route('/')
def aggregate_data():
    client = MongoClient("mongodb://mongodb:27017/")
    db = client.mydatabase
    collection = db.posts

    # Perform a simple aggregation (e.g., count the number of posts)
    post_count = collection.count_documents({})
    
    return jsonify({"total_posts": post_count})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

