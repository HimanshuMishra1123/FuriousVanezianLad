import praw
import time
import os
import config

REPLY_MESSAGE = "Melone, I am on the FUCKING edge right now! You're trying to say \"Well done\" but the phrase \"Di Molto\" means \"A lot of\"! The correct Italian phrase you're looking for is \"Molto Bene\"! YOU SHOULD FUCKING KNOW THIS BECAUSE WE'RE ITALIAN! For the love of God, Melone, I AM BEGGING YOU SHOW SOME ITALIAN PRIDE AND GET IT RIGHT YOU RAPIST PIECE OF SHIT!"

def authenticate():
    print("Authenticating...")
    reddit = praw.Reddit(client_id = config.client_id,
                    client_secret = config.client_secret,
                    username = config.username,
                    password = config.password,
                    user_agent = 'FuriousVanezianLad by /u/FuriousVanezianLad')
    print("Authenticated as {}".format(reddit.user.me()))
    return reddit
    

def main():
    reddit = authenticate()
    while True:
            run_bot(reddit)
            
            
def run_bot(reddit):
    print("Obtaining 25 comments...")
    try:
        for comment in reddit.subreddit('ShitPostCrusaders+BlursedJojo+cursedjojo+expectedjojo+UnexpectedJoJo+QualityPostCrusaders+wholesomemudad+blursedimages+ghiaccio_irl').stream.comments(skip_existing=True):
            if "Di Molto" in comment.body and comment.author != reddit.user.me():
                print('String with "Di Molto" found in comment {}',format(comment.id))
                comment.reply(REPLY_MESSAGE)
                print("Replied to comment " + comment.id)
            if "Di Molto!" in comment.body and comment.author != reddit.user.me():
                print('String with "Di Molto" found in comment {}',format(comment.id))
                comment.reply(REPLY_MESSAGE)
                print("Replied to comment " + comment.id)
            if "di molto" in comment.body and comment.author != reddit.user.me():
                print('String with "Di Molto" found in comment {}',format(comment.id))
                comment.reply(REPLY_MESSAGE)
                print("Replied to comment " + comment.id)
            if "DI MOLTO" in comment.body and comment.author != reddit.user.me():
                print('String with "Di Molto" found in comment {}',format(comment.id))
                comment.reply(REPLY_MESSAGE)
                print("Replied to comment " + comment.id)
            if "di molto!" in comment.body and comment.author != reddit.user.me():
                print('String with "Di Molto" found in comment {}',format(comment.id))
                comment.reply(REPLY_MESSAGE)
                print("Replied to comment " + comment.id)
            if "DI MOLTO!" in comment.body and comment.author != reddit.user.me():
                print('String with "Di Molto" found in comment {}',format(comment.id))
                comment.reply(REPLY_MESSAGE)
                print("Replied to comment " + comment.id)
    except Exception as e:
        print("Got exception:{}".format(e))
        print("Sleeping for 10 seconds...")
        time.sleep(10)
    
    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
