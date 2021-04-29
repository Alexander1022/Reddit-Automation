import praw, requests, json, time

subreddit_choice = 'Python'
config_file = 'config.json'

with open(config_file) as f:
    credentials = json.load(f)

reddit = praw.Reddit(client_id = credentials['client_id'],
                    client_secret=credentials['client_secret'],
                    user_agent=credentials['user_agent'],
                    redirect_uri=credentials['redirect_uri'],
                    refresh_token=credentials['refresh_token'])

if not credentials['refresh_token']:
    print("Please fill the config file.")
    exit()

subreddit = reddit.subreddit(subreddit_choice)
print("You are posting to \"" + str(subreddit_choice) + "\"")

title=input("What title do you want: ")
content = input("What text do you want (you can leave it empty in some subs): ")
nsfw_check = input("Is the post NSFW: ")

if(nsfw_check == 'yes'):
    nsfw = True
else:
    nsfw = False

subreddit.submit(title, selftext = content, nsfw = nsfw)
reddit.validate_on_submit = True

print("[POSTING]\n" + "Title: " + str(title) + "\n" + "Content: " + str(content) + "\n" + "NSFW: " + str(nsfw))

# reddit posts the content after about 3 seconds
time.sleep(3)
print("[POSTED]")