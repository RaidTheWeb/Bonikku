template = '''
{}
\n*This is a bot, for more information contact RaidTheWeb*
\n*[bot info](https://github.com/RaidTheWeb/RedBot/wiki)|[bot github](https://github.com/RaidTheWeb/RedBot)*'''




def read_subreddit(posts, subreddit):
  import praw

  reddit = praw.Reddit('redbot')

  subreddit = reddit.subreddit(subreddit)

  for submission in subreddit.new(limit=posts):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("ID: ", submission.id)
    print("---------------------------------\n")

def post(title, text, subreddit):
  import praw

  reddit = praw.Reddit('redbot')

  reddit.subreddit(subreddit).submit(title, selftext=text)

def reply_to_keyword(keyword, reply_text, post_id):
  import praw
  import re
  import os
  from time import sleep

  if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []

  # If we have run the code before, load the list of posts we have replied to
  else:
    # Read the file into a list and remove any empty values
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))

  reddit = praw.Reddit('redbot')
  for comment in reddit.submission(id=post_id).comments.list():
    current = 0
    print(comment.body)
    if re.search(keyword, comment.body, re.IGNORECASE):
      reply = reply_text
      comment.reply(reply)
      print(reply)
      posts_replied_to.append(comment.id)
      sleep(600 + current)
      current += 100
  
  with open("posts_replied_to.txt", "w") as f:
    for comment_id in posts_replied_to:
        f.write(comment_id + "\n")

def comment(reply_text, post_id):
  import praw

  reddit = praw.Reddit('redbot')
  submission = reddit.submission(id=post_id)
  print('\nCommenting on:\n')
  print("Title: ", submission.title)
  print("Text: ", submission.selftext)
  print("Score: ", submission.score)
  print("ID: ", submission.id)
  print("---------------------------------\n")
  submission.reply(reply_text)


def redditor_posts(redditor, posts):
  import praw

  reddit = praw.Reddit('redbot')
  for submission in reddit.redditor(redditor).new(limit=posts):
    try:
      print("Title: ", submission.title)
      print("Text: ", submission.selftext)
      print("Score: ", submission.score)
      print("ID: ", submission.id)
      print("---------------------------------\n")
    except:
      continue

def sendmail(redditor, title, message):
  import praw

  reddit = praw.Reddit('bonikku')
  reddit.redditor(redditor).message(title, message)


class AI:
  pass

  
