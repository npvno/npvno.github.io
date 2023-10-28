from instaloader import Instaloader, Profile, exceptions
from time import sleep
from datetime import datetime, timedelta
import random, json


L = Instaloader()

# Define the JSON file name
json_filename = "followers.json"

with open(json_filename, "r") as json_file:
    followers_list = json.load(json_file)

print('*'*100)
print(f'List of {len(followers_list)} followers loaded')
print('*'*100)



def get_all_posts(selected_profile):
    posts_limit = 12
    posts_iterator = selected_profile.get_posts()
    posts=[]
    try:
        for post in posts_iterator:
            posts.append(post)
            if not posts_iterator.total_index % 12:
                r=random.randint(0,0)
                print(f'Posts list length is {len(posts)}, sleeping {r} seconds...')
                sleep(r)
            if posts_iterator.total_index >= posts_limit: 
                break
    except exceptions.ConnectionException as err:
        print("ConnectionException Error:", err)  
    finally:
        print(f'Final posts list length is {len(posts)}')
        return posts



#Download all the post of selected followers sorted by likes and take top 3
num_followers=3
num_top_posts=3
top_posts_list=[]

while len(top_posts_list) < num_followers:
    random_follower = random.choice(followers_list)
    print(f"Random follower is {random_follower}")
    profile = Profile.from_username(L.context, random_follower)
    if profile.is_private: #checking the profile is not private
        print(f"X {random_follower} not added to the list (private profile)")
    else:
        all_posts = get_all_posts(profile) #retrieving the posts
        most_recent_post=max(all_posts, key=lambda post: post.date_local)
        if len(all_posts)<num_top_posts: #making sure there is more than 3 posts
            print(f"X {random_follower} not added to the list (not enought posts)")
        elif most_recent_post.date_local >= (datetime.now(most_recent_post.date_local.tzinfo) - timedelta(days=90)): #making sure the most recent posts is no older than 3 months
              print(f"The most recent post is older than 3 months. (ID: {most_recent_post.shortcode})")
              print(f"X {random_follower} not added to the list (last post too old)")
        else:
            posts_sorted_by_likes = sorted(all_posts,key=lambda p: p.likes + p.comments,reverse=True) #classifying the posts
            posts_sorted_by_likes = [post for post in posts_sorted_by_likes if not post.is_video] #removing videos
            top_posts_list.append(posts_sorted_by_likes[:3]) #taking top three
            print(f"✓ {random_follower} added to the list")
            



print('*'*100)
print('top_posts_list obtained')
print(top_posts_list)
print('*'*100)



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
