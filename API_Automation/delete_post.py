#post delete
import requests
url="https://jsonplaceholder.typicode.com/posts/1"
response=requests.delete(url)
print
payload={

    "body":"This is api auto"
}



assert response.status_code==200, "post is not deleted"
print("post is deleted successfullly")