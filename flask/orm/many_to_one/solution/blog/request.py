import requests
import json

headers = {
    "content-type": "application/json",
}
# Must use this url instead of localhost
url = "http://127.0.0.1:5555"

# test data
new_user = {"name": "test"}
new_post = {"content": "my blog post", "title": "my blog title"}
blog_patch = {"title": "new title"}
user_patch = {"name": "patched"}

# Post a new user
r = requests.post(f"{url}/users", data=json.dumps(new_user), headers=headers)
user_post_response = r.json()
assert user_post_response["name"] == "test", "response for user post incorrect"
print("user post successful")

# Get the new user we just posted
r = requests.get(f'{url}/users/{user_post_response["id"]}', headers=headers)
gotten_new_user = r.json()
assert (
    gotten_new_user["name"] == "test"
), "could not get posted user, problem either with get or post users"
print("posted user gotten successfully")

# Delete the user we just posted
r = requests.delete(f'{url}/users/{user_post_response["id"]}', headers=headers)
deleted_user_response = r.json()
assert deleted_user_response == {}, "response for delete was incorrect"
print("posted user deleted successfully")

# Try to get the deleted user (should return an error message)
r = requests.get(f'{url}/users/{user_post_response["id"]}', headers=headers)
gotten_deleted_user = r.json()
assert (
    gotten_deleted_user.get("error") is not None
), "error message not returned for non-existent user"
print("error message for delete user correct")

# Patch user 1
r = requests.patch(f"{url}/users/1", data=json.dumps(user_patch), headers=headers)
patched_user_response = r.json()
assert patched_user_response["name"] == "patched", "response for patch incorrect"
print("user patch request correct")

# Get user 1 and verify that patch was applied
r = requests.get(f"{url}/users/1", headers=headers)
gotten_patched_user = r.json()
assert (
    gotten_patched_user["name"] == "patched"
), "user patch was not persisted to database"
print("successfully got patched user from database")
