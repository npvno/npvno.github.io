from instaloader import Instaloader, Profile
import random, os, json


L = Instaloader()

# Define the JSON file name
json_filename = "followers.json"

with open(json_filename, "r") as json_file:
    followers_list = json.load(json_file)

print('*'*100)
print(f'List of {len(followers_list)} followers obtained')
print('*'*100)


#Download all the post of selected followers sorted by likes and take top 3
num_top_posts=3
num_followers=3
top_posts_list=[]
while len(top_posts_list) < num_followers:
    random_follower = random.choice(followers_list)
    print("Random follower is: " + random_follower)
    profile = Profile.from_username(L.context, random_follower)
    if profile.is_private: #checking the profile is not private
        print(f"X {random_follower} is private, skipping")
    else:
        posts_sorted_by_likes = sorted(profile.get_posts(),key=lambda p: p.likes + p.comments,reverse=True) #downloading the posts, I SHOULD CAP THE NUM OF POSTS TO n
        posts_sorted_by_likes = [post for post in posts_sorted_by_likes if not post.is_video]
        if len(posts_sorted_by_likes)>=num_top_posts: #making sure there is more than 3 posts
            top_posts_list.append(posts_sorted_by_likes[:3])
            print(f"✓ {random_follower} added to the list")
        else:
            print(f"X {random_follower} not added to the list (not enought posts)")
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
