# Function to create a new YouTube video dictionary
def create_youtube_video(title, description):
    return {
        'title': title,
        'description': description,
        'likes': 0,
        'dislikes': 0,
        'comments': {}
    }

# Function to increment likes
def like(youtube_video):
    if 'likes' in youtube_video:
        youtube_video['likes'] += 1
    return youtube_video

# Function to increment dislikes
def dislike(youtube_video):
    if 'dislikes' in youtube_video:
        youtube_video['dislikes'] += 1
    return youtube_video

# Function to add a comment
def add_comment(youtube_video, username, comment_text):
    youtube_video['comments'][username] = comment_text
    return youtube_video

video = create_youtube_video("eliel","eliel the king")
for i in range(495):
    like(video)
dislike(video)
print(add_comment(video,"nizan","you are the king"))
