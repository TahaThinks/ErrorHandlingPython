# eval() function will create a list of dictionaries using the input
facebook_posts = eval(input())

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        continue


print(total_likes)