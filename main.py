import redbot
import praw
import datetime
import subprocess

class BonikkuCore:
  def monitor():
    reddit = praw.Reddit('bonikku')
    subreddit = reddit.subreddit('fl80')
    for submission in subreddit.stream.submissions():
      command = submission.title
      if submission.author == 'RaidTheWeb':
        print('Recieved Command:\n')
        print('Command: ' + submission.title)
        print('Arguments: ' + submission.selftext)
        print('Author: ' + str(submission.author))
        print('ID: ' + submission.id)
        print('---------------------------------\n')
        if submission.title.lower() == 'time':
          response = str(datetime.datetime.now())

        elif submission.title.lower() == 'useragent':
          response = 'Bonikku AI EN_NZ 1.0rc1'

        elif submission.title.lower() == 'sendmail':
          args = submission.selftext
          argslist = args.split(',')
          if len(argslist) == 3:
            redditor = argslist[0]
            title = argslist[1]
            message = argslist[2]
            redbot.sendmail(redditor, title, message)
            response = 'Sent {} to {}'.format(title, redditor)
          else:
            response = 'INFO: [bonikku]: not enough arguments.'
        elif submission.title.lower() == 'bash':
          response = subprocess.getoutput(submission.selftext)

        else:
          response = 'INFO: [bonikku]: unknown function.'


        print('Responding...\n')
        responder = reddit.submission(id=submission.id)
        responder.reply(response)
        print('Response: ' + response)


      else:
        print('WARNING: [bonikku]: unauthorized redditor active on r/fl80\n' + str(submission.author) + ' posted:\n')
        print('Recieved Command:\n')
        print('Command: ' + submission.title)
        print('Arguments: ' + submission.selftext)
        print('Author: ' + str(submission.author))
        print('ID: ' + submission.id)
        print('---------------------------------\n')
        print('Reporting...\n')
        redbot.sendmail('RaidTheWeb', 'WARNING: [bonikku]: unauthorized redditor active on r/fl80', 'At {} {} attempted to send a command to Bonikku. Take immediate action!'.format(datetime.datetime.now(),str(submission.author)))
        print('Infiltration reported to RaidTheWeb ( MODERATOR )')


bonikku = BonikkuCore
bonikku.monitor()