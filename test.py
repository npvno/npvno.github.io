from instaloader import Instaloader, Profile


L = Instaloader()
random_follower = "lek_ky_36"
profile = Profile.from_username(L.context, random_follower)
print(profile.biography)


def loop(selected_profile):
    post_iterator = selected_profile.get_posts()
    posts=[]
    try:
        for post in post_iterator:
            posts.append(post)
            print(f"added post {post.url}")
    except ConnectionException:
        print("error")
        print(post_iterator.total_index)
    return posts


x=loop(profile)
print(x)
print(len(x))