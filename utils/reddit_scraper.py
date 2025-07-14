import praw
import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# Initialize Reddit API client
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)

def get_user_data(username):
    try:
        redditor = reddit.redditor(username)

        # Get the last 50 posts
        posts = []
        for submission in redditor.submissions.new(limit=50):
            posts.append(f"Title: {submission.title}\nText: {submission.selftext}\n")

        # Get the last 100 comments
        comments = []
        for comment in redditor.comments.new(limit=100):
            comments.append(f"Comment: {comment.body}\n")

        return posts, comments

    except Exception as e:
        print(f"❌ Error fetching user data: {e}")
        return [], []
