from instaloader import Instaloader, Profile
import os, json

INSTA_USERNAME = os.environ.get("INSTA_USERNAME")
INSTA_SESSION = os.environ.get("INSTA_SESSION")
INSTA_CSRF = os.environ.get("INSTA_CSRF")
TARGET_PAGE = os.environ.get("TARGET_PAGE") 


L = Instaloader()
L.load_session(INSTA_USERNAME, {"sessionid": INSTA_SESSION, "csrftoken": INSTA_CSRF})


#Download the list of followers of the page
followers_list=[]
profile = Profile.from_username(L.context, TARGET_PAGE)
for follower in profile.get_followers():
        followers_list.append(follower.username)
print('*'*100)
print('Followers list obtained')
print('*'*100)
# Define the JSON file name
json_filename = "followers.json"
# Write the JSON data to the file
with open(json_filename, "w") as json_file:
    json.dump(followers_list, json_file)
print(f"JSON file '{json_filename}' generated successfully.")