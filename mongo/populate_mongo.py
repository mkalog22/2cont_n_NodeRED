import requests
from pymongo import MongoClient

# Fetch data from URL
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
data = response.json()

# Connect to MongoDB and insert data
mongo_ip = "172.18.0.2"  # Use the IP address obtained from the inspect command
client = MongoClient(f"mongodb://{mongo_ip}:27017/")
db = client.mydatabase
collection = db.posts
collection.insert_many(data)

print("Data inserted successfully.")

