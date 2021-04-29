# Reddit Automation with Python


This project is called **Reddit Automation**.  You can post in Reddit from the terminal. It's faster and easier.  

```
![Reddit Logo](reddit-logo.png)
```

# Files

In the project you have 3 files:
 

 1. **main** - run in the end when you are done with the files bellow
 2. **generate-key** - with this file you can generate **refresh token**
 3. **config** - in this file you have to write you client id, secret key and refresh token that you generated with **generate-key** file

## How to use
1. Go to [Reddit Apps Page](https://www.reddit.com/prefs/apps) and create a new app. 
2. Look for CLIENT ID and SECRET KEY.
3. Run `python generate-key.py` to generate a refresh token.
4. Run `python main.py` and follow the steps. 
*Disclaimer: by default the subreddit is set to **Python**. You can change it from main.py.*

Enjoy! :)
