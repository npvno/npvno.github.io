from instaloader import Instaloader, Profile, Post, Hashtag, NodeIterator
import random, os, json

INSTA_USERNAME = os.environ.get("INSTA_USERNAME")
INSTA_PASSWORD = os.environ.get("INSTA_PASSWORD")
INSTA_SESSION = os.environ.get("INSTA_SESSION")
INSTA_CSRF = os.environ.get("INSTA_CSRF")

target_page = "eddyfrank325"


L = Instaloader()
L.load_session(INSTA_USERNAME, {"sessionid": INSTA_SESSION, "csrftoken": INSTA_CSRF})


#Download the list of followers of the page
followers_list=[]
profile = Profile.from_username(L.context, target_page)
for follower in profile.get_followers():
        followers_list.append(follower)
print('*'*100)
print('Followers list obtained')
print('*'*100)


#Download all the post of selected followers sorted by likes and take top 3
num_top_posts=3
num_followers=3
top_posts_list=[]
while len(top_posts_list) < num_followers:
    random_follower = random.choice(followers_list)
    print("Random follower is: " + random_follower.username)
    profile = Profile.from_username(L.context, random_follower.username)
    if profile.is_private: #checking the profile is not private
        print(f"{random_follower.username} is private, skipping")
    else:
        posts_sorted_by_likes = sorted(profile.get_posts(),key=lambda p: p.likes + p.comments,reverse=True) #downloading the posts, I SHOULD CAP THE NUM OF POSTS TO n
        posts_sorted_by_likes = [post for post in posts_sorted_by_likes if not post.is_video]
        if len(posts_sorted_by_likes)>=num_top_posts: #making sure there is more than 3 posts
            top_posts_list.append(posts_sorted_by_likes[:3])
            print(f"{random_follower.username} added to the list")
        else:
            print(f"{random_follower.username} not added to the list (not enought posts)")
print('*'*100)
print('top_posts_list obtained')
print('*'*100)
print(top_posts_list)



# Create a dictionary to store user data
user_data = {
    "users": []
}

# Iterate through the top_posts_list and create the JSON structure
for top_posts in top_posts_list:
    user_info = {
        "username": top_posts[0].owner_username,
        "postIDs": [post.shortcode for post in top_posts]
    }
    user_data["users"].append(user_info)

# Define the JSON file name
json_filename = "top_posts.json"

# Write the JSON data to the file
with open(json_filename, "w") as json_file:
    json.dump(user_data, json_file, indent=4)

print(f"JSON file '{json_filename}' generated successfully.")


"""
#Download top posts
for top_posts in top_posts_list:
    for post in top_posts:
        L.download_post(post, post.owner_username)
"""

# send x profiles
# manually select a profile
# download the top post of that profile
# publish the top post on my page

