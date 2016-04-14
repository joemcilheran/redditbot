import time
import praw
import urllib.request
user_agent= 'windows:pullwallpaper:v1 (by /u/gimligloinson)'
mybot = praw.Reddit(user_agent = user_agent)
mybot.login('gimligloinson','M3czpgbe',disable_warning = True)

def download(url,filename):
    image = urllib.request.urlretrieve(url,filename)
    print(image,filename)
    
    

subreddit = mybot.get_subreddit('wallpapers')
while True:
    for submission in subreddit.get_hot(limit =25):
        if "Space" in (submission.title):
            filename = (submission.title) + '.jpg'
            url = submission.url
            download(url,filename)
        
    time.sleep(43200)
    

    
    


                                    