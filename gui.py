from tkinter import *
import instaloader
from instaloader import Post

import random

root = Tk()
root.geometry('500x500')
root.title("BeyondHelloWorld")

canvas = Canvas(root, height=500, width=500)
canvas.pack()

btn_getRandom = None
label = None

usernames = []

def getComments():
    # print("This function will get comments")

    global btn_getRandom
    global label
    global usernames

    L = instaloader.Instaloader()
    post = Post.from_shortcode(L.context, 'CDjK4YqA5r6')
    usernames = list(set([comment.owner.username for comment in post.get_comments()]))

    #shuffling the list randomly
    random.shuffle(usernames)

    btn_getInfo.destroy()

    btn_getRandom = Button(canvas, text = "Randomly Select a Winner", font=("Helvetica", 12), command=selectWinner)
    canvas.create_window(250,200,window=btn_getRandom)
    label = Label(text = "Winner will be displayed here", font=("Helvetica", 12))
    canvas.create_window(250,270,window=label)

    #let me remove my own account from the list :
    usernames.remove("femindharamshi")
    usernames.remove("beyondhelloworld")

    for user in sorted(usernames):
        print(user)

counter = 0
def selectWinner():
    global counter

    #adding some loop for entertainment
    randomInt = random.randint(0,len(usernames)) - 1
    label['text'] = usernames[randomInt]
    counter = counter + 1
    if(counter < 100):
        label.after(100, selectWinner)
    else:
        label['text'] = "Winner is @"+usernames[randomInt]
        label['font'] = ("Helvetica", 12, "bold")
    

btn_getInfo = Button(canvas, text = "Get Comments", font=("Helvetica", 12), command=getComments)

titleLabel = Label(canvas, text="BeyondHelloWorld Giveaway #01", font=("Helvetica", 12, "bold"))
canvas.create_window(250,250,window=btn_getInfo)
canvas.create_window(250,100,window=titleLabel)

root.mainloop()