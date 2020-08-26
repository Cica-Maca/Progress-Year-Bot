import praw
from selenium import webdriver
from time import sleep

print(round(66.1231231321, 4))


def year_percentage():
    browser = webdriver.Firefox()
    browser.implicitly_wait(1)
    browser.get("https://hugovk.github.io/year-progress-bar/")
    percentage = browser.find_element_by_xpath("//*[@id='percent']").text
    print(percentage)
    browser.close()


def get_saved_comments():
    with open("comments_replied_to.txt", "r") as f:
        comments_replied = f.read()
        comments_replied = comments_replied.split("\n")
    return comments_replied


reddit = praw.Reddit(client_id="bVWZeUZbfk-ZSQ",
                     client_secret="BycAbnGHXvktwxfPTZQKUhBK4XY",
                     username="Progress-Year-Bot",
                     password="farismakarov",
                     user_agent="Progress-Year-Bot (showing percentage of the current year) 1.0 by u/Selj0cina")
subreddit = reddit.subreddit("memes")
keyphrase = "this year"
comments_replied = get_saved_comments()
print(comments_replied)


def bot(comments_replied):
    for comment in subreddit.stream.comments():
        if keyphrase in comment.body and not comment.parent().author == reddit.user.me() and not comment.author == reddit.user.me() and comment.id not in comments_replied:
            print(comment.created_utc)
            browser = webdriver.Firefox()
            browser.implicitly_wait(1)
            browser.get("https://hugovk.github.io/year-progress-bar/")
            percentage = browser.find_element_by_xpath("//*[@id='percent']").text
            print(percentage)
            browser.close()
            print("found")
            comment.reply("This year is " + "**" + percentage + "**" + " complete.")
            comments_replied.append(comment.id)
            sleep(630)

            with open("comments_replied_to.txt", "a") as f:
                f.write(comment.id + "\n")
        else:
            pass


bot(comments_replied)
