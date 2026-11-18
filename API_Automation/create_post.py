#create post using request
import requests
url="https://jsonplaceholder.typicode.com/posts"
payload={
    "userId":1,
    "title":"API Auto",
    "body":"This is api auto"
}

response=requests.post(url, json=payload)
print(response.json())
print(response.status_code)

assert response.status_code==201, "post is not created"
print("post is created successfullly")