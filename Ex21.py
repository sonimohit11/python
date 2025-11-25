# Building a Simple API Client (Write a simple Python class that encapsulates the functionality for making GET and POST requests to the JSONPlaceholder API. Include methods for fetching posts and creating a new post.)

import requests

class JSONPlaceholderClient:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    def get_posts(self):
        """Fetch all posts."""
        url = f"{self.BASE_URL}/posts"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to fetch posts: {response.status_code}")

    def get_post(self, post_id):
        """Fetch a single post by ID."""
        url = f"{self.BASE_URL}/posts/{post_id}"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return None  # post does not exist
        else:
            raise Exception(f"Error fetching post: {response.status_code}")

    def create_post(self, title, body, user_id):
        """Create a new post."""
        url = f"{self.BASE_URL}/posts"
        data = {
            "title": title,
            "body": body,
            "userId": user_id
        }

        response = requests.post(url, json=data)

        if response.status_code == 201:
            return response.json()
        else:
            raise Exception(f"Failed to create post: {response.status_code}")


# # client = JSONPlaceholderClient()

# # 1. Get all posts
# posts = client.get_posts()
# print("Fetched", len(posts), "posts")

# # 2. Get a single post
# post = client.get_post(5)
# print("\nPost ID 5:", post)

# # 3. Test with non-existing post
# missing = client.get_post(1000)
# print("\nPost ID 1000:", missing)  # None

# # 4. Create a new post
# new_post = client.create_post(
#     title="Hello World",
#     body="This is my first API post!",
#     user_id=1
# )
# print("\nCreated Post:", new_post)
