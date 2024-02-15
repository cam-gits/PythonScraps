import praw
import csv
from datetime import datetime

# USE reddit.com/prefs/apps 
reddit_client_id = 'ID'
reddit_client_secret = 'SECRET'
reddit_user_agent = 'AGENT'  

# Create a Reddit instance
reddit = praw.Reddit(
    client_id=reddit_client_id,
    client_secret=reddit_client_secret,
    user_agent=reddit_user_agent
)

#def scrape to CSV
def scrape_reddit(subreddit_name, num_posts=10):
    subreddit = reddit.subreddit(subreddit_name)
    new_posts = subreddit.new(limit=num_posts)

    for post in new_posts:
        with open('reddit.csv', 'a', newline='',encoding="utf-8") as csvfile: #encode for web
            created = datetime.utcfromtimestamp(post.created)
            fieldnames = ['Title', 'Date','URL','Text','Score','Number of Comments']
            postdump = csv.writer(csvfile, delimiter=',')
            postdump.writerow([post.title,created,post.url,post.selftext[:150],post.score,post.num_comments])

scrape_reddit('DevelEire', num_posts=50)
print('Done')
