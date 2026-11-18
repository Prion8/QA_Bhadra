#create put using request
import requests
url="https://jsonplaceholder.typicode.com/posts/1"
payload={

    "body":"This is api auto"
}

response=requests.patch(url, json=payload)
print(response.json())
print(response.status_code)

assert response.status_code==200, "post is not created"
print("post is uploaded successfullly")