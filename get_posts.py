from instaloader import Instaloader, Profile, exceptions
from time import sleep
import random, json


L = Instaloader()

# Define the JSON file name
json_filename = "followers.json"

with open(json_filename, "r") as json_file:
    followers_list = json.load(json_file)

print('*'*100)
print(f'List of {len(followers_list)} followers loaded')
print('*'*100)


num_followers=3
num_top_posts=3
top_posts_list=[]


def num_posts_downloaded_per_profile(num_profiles):
    limit=112
    for i in range (limit-1,0,-1):
        if not (i%num_profiles):
            return int(i/3)


def get_all_posts(selected_profile):
    posts_limit = num_posts_downloaded_per_profile(num_followers)
    posts_limit = 12 #20<x<37
    posts_iterator = selected_profile.get_posts()
    posts=[]
    try:
        for post in posts_iterator:
            posts.append(post)
            if posts_iterator.total_index >= posts_limit:
                break
    except exceptions.ConnectionException as err:
        print("ConnectionException Error:", err)
    finally:
        print(f'Posts list length is {len(posts)}')
    return posts



#Download all the post of selected followers sorted by likes and take top 3

while len(top_posts_list) < num_followers:
    random_follower = random.choice(followers_list)
    print(f"Random follower is {random_follower}")
    profile = Profile.from_username(L.context, random_follower)
    if profile.is_private: #checking the profile is not private
        print(f"X {random_follower} not added to the list (private profile)")
    else:
        all_posts = get_all_posts(profile) #retrieving the posts
        if len(all_posts)<num_top_posts: #making sure there is more than 3 posts
            print(f"X {random_follower} not added to the list (not enought posts)")
        else:
            posts_sorted_by_likes = sorted(all_posts,key=lambda p: p.likes + p.comments,reverse=True) #classifying the posts
            posts_sorted_by_likes = [post for post in posts_sorted_by_likes if not post.is_video] #removing videos
            top_posts_list.append(posts_sorted_by_likes[:3]) #taking top three
            print(f"✓ {random_follower} added to the list")
            #r=random.randint(20,40)
            #print(f'Sleeping {r} seconds...')
            #sleep(r)
            



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
