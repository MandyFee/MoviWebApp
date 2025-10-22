def has_consecutive_nums(numbers):
    for i in range(len(numbers)-1):
        if numbers[i+1] == numbers[i] +1:
            return True

    return False

#print(has_consecutive_nums([3, 6, 6, 8]))

# Input:
posts = [
     {'title': 'Intro to HTML', 'content': 'HTML is a markup language.', 'tags': ['HTML', 'web']},
     {'title': 'CSS Grid', 'content': 'CSS Grid is a layout system.', 'tags': ['CSS', 'web']},
     {'title': 'Responsive Web Design', 'content': 'Responsive design techniques.', 'tags': ['CSS', 'design']},
]

# result = filter_posts_by_tag(posts, 'CSS')
# Output: ['CSS Grid', 'Responsive Web Design']

def filter_posts_by_tag(posts, search_tag):
    output=[]
    for post in posts:
        if search_tag in post["tags"]:
            output.append(post["title"])

    return output

print(filter_posts_by_tag(posts,"web"))
