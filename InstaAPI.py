from instaloader import Instaloader, Profile, Post, Hashtag, NodeIterator
import random
import os

INSTA_USERNAME = os.environ.get("INSTA_USERNAME")
INSTA_PASSWORD = os.environ.get("INSTA_PASSWORD")
INSTA_SESSION = os.environ.get("INSTA_SESSION")
INSTA_CSRF = os.environ.get("INSTA_CSRF")

target_page = "eddyfrank325"


L = Instaloader()

#LOGIN
try:
    L.login(INSTA_USERNAME, INSTA_PASSWORD)
except:
    L.load_session(INSTA_USERNAME, {"sessionid": INSTA_SESSION, "csrftoken": INSTA_CSRF})
    L.get_stories()


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



# Get the current working directory where the script is running
current_directory = os.getcwd()

# Define the filename (index.html)
html_filename = "index.html"

# Combine the current directory and filename to create the full file path
html_file_path = os.path.join(current_directory, html_filename)

# Rest of your script...

# Create an HTML file for output
with open(html_file_path, "w") as html_file:
    # Write the HTML header
    html_file.write("<html>\n\n<head>\n</head>\n\n<body>\n\n")

    # Iterate through the top_posts_list and write the data to the HTML file
    for top_posts in top_posts_list:
        username = top_posts[0].owner_username
        html_file.write(f'<h2><a href="https://www.instagram.com/{username}" target="_blank">{username}</a></h2>\n')
        html_file.write(f'<table style="width:100%"><tr>\n\n')
        for post in top_posts:
            post_id = post.shortcode
            post_url = post.url
            html_file.write(f'<td>\n<p>Post ID: <a href="https://www.instagram.com/p/{post_id}" target="_blank">{post_id}</a></p>\n')
            html_file.write(f'<blockquote style="width:300px;" class="instagram-media" data-instgrm-version="14"><a href="https://www.instagram.com/p/{post_id}/" ></a></blockquote>\n</td>\n\n')
        html_file.write("</tr></table><hr>\n\n")  # Add a horizontal line between users

    # Write the HTML footer
    html_file.write('<script src="https://www.instagram.com/embed.js"></script>\n')
    html_file.write("</body>\n</html>\n")
html_file.close()
print(f"HTML file '{html_filename}' generated successfully.")


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

