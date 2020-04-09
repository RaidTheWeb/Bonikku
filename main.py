import redbot
import praw
import datetime
import subprocess
import os
import time

class BonikkuCore:
  def monitor(monitored):
    while True:
      reddit = praw.Reddit('bonikku')
      subreddit = reddit.subreddit(monitored)
      for submission in subreddit.stream.submissions():
        command = submission.title
        print('Recieved Command:\n')
        print('Command: ' + submission.title)
        print('Arguments: ' + submission.selftext)
        print('Author: ' + str(submission.author))
        print('ID: ' + submission.id)
        print('---------------------------------\n')
        if submission.title.lower() == 'bonikku:time':
          response = str(datetime.datetime.now())

        elif submission.title.lower() == 'bonikku:useragent':
          response = 'Bonikku AI EN_NZ 1.0rc1'

        elif submission.title.lower() == 'bonikku:sendmail':
          args = submission.selftext
          argslist = args.split(',')
          if len(argslist) == 3:
            redditor = argslist[0]
            title = argslist[1]
            message = argslist[2]
            redbot.sendmail(redditor, title, message)
            response = 'Sent {} to {}'.format(title, redditor)
          else:
            response = 'INFO: [bonikku]:  not enough arguments.'
        elif submission.title.lower() == 'bonikku:bash':
            response = subprocess.getoutput(submission.selftext)
        elif submission.title.lower() == 'bonikku:python':
          temp = open('tmp.py', 'w+')
          f = submission.selftext
          temp.write(f)
          temp.close()
          cmd = subprocess.run(["python", "tmp.py"], capture_output=True)
          response = cmd.stdout.decode()
        elif submission.title.lower() == 'bonikku:monitor':
          args = submission.selftext
          monitored = args
          response = 'Changed monitor target subreddit to r/{}.'.format(monitored)

        else:
          if submission.title.lower().startswith('bonikku:'):
            response = 'INFO: [bonikku]: unknown function.'
          else:
            continue

        try:
          print('Responding...\n')
          responder = reddit.submission(id=submission.id)
          responder.reply(response)
          print('Response: ' + response)
          break
        except:
          pass


bonikku = BonikkuCore
bonikku.monitor('fl80')