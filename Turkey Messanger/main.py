from twilio.rest import Client
cellphone = ""
twilio_number= ""
import random
from tkinter import *
from tkinter import Radiobutton
import pygame 

pygame.mixer.init()


root = Tk()
root.configure(bg="orange")
root.title('Innovative Rich: Turkey Telegrame')
root.geometry('600x600')
trkyimg = PhotoImage(file= "assets/trkyimg.png")
large_font = ('Helvetica',50)
small_font = ('verdana',10)

GENERAL_TURKEY_MESSAGES = [
    "We are so grateful for you and your family! Sending you peace and warmth during this crazy time. ",
    "We all have so much to be thankful for! Sending you and your family a harvest of blessings this Thanksgiving. ",
    "Happy Thanksgiving! We know this year has been rough, but we see your strength and wish you all the best this Thanksgiving.",
    "May you enjoy the warmth of family this season and the harvest of the feast! Happy Thanksgiving!",
    "Sending you laughter, joy and lots of stuffing this Thanksgiving. ",
    "We hope you and your family have been able to get together this year and are enjoying a Thanksgiving feast together! ",
    "Wishing you a Happy Thanksgiving from across the street!" ,
    "What a crazy ride this year has been! We are so thankful for you and your family. Happy Thanksgiving!",
    ]
FAMILYFRIENDS_TURKEY_MESSAGES =[
    "Wishing you a day of feasting, laughing and loving one another. Happy Thanksgiving! Grateful for each and every one of you!",
    "Thankful to call you family — this and every year! Happy Thanksgiving.",
    "Sending you all my love from across the [country, state, world etc.]! I/we am so grateful to have you all in my life and wish I could be there feasting with you all. Have some extra pumpkin pie for me.",
    "It’s been one hell of a year and I cannot be more grateful for you all as you stuck by me each and every step of the way. Happy Thanksgiving!",
    "I am beyond thankful to have you all in my life, this and every year! Sending my love!",
    "Your family is a true blessing in my/our life! Thanking my lucky stars this season that you are all well and healthy. Happy Thanksgiving!",
    "What a year! I am stunned at the level of support you’ve shown me/us and am beyond grateful for you. Happy Thanksgiving!",
    "Hope you and your family enjoy a delicious feast! Grateful that everyone is well and healthy!",
    "Thinking of you this Thanksgiving season and wishing you all peace and love.",
 ]
COLLEAGUES_TURKEY_MESSAGES =[
    "Taking this opportunity to formally thank you for being such a pleasure to work with. Happy Thanksgiving!",
    "Thank you for always supporting me and having my back. Happy Thanksgiving!",
    "I could not have asked for a better work-mate, thanks for everything and happy Thanksgiving. ",
    "Wishing you and your family lots of good eats and gratitude this season!",
    "Grateful for your partnership this year and looking forward to continuing our rebuild next year! Happy Thanksgiving!",
    "Thank you for staying by our side this year. Your loyalty is truly appreciated and we look forward to working with you soon.",
    ]
CLIENT_TURKEY_MESSAGES =[
    "Thank you for supporting our small business through the trials of this year. We are grateful for your loyalty and wish you a very Happy Thanksgiving!",
    "Our gratitude goes out to you and your family this Thanksgiving. Thank you for your business in 2021!",
    "We appreciate your business this and every year! Happy Thanksgiving!",
    "The small team at [Company X] thanks you for your patronage in 2021 and wishes you a very delicious Thanksgiving feast!",
    "Happy Thanksgiving from your local [X] business! Thank you for being a loyal customer.",
    ]
FUNNY_TURKEY_MESSAGES=[
    "The best part of the holidays is getting to see you! And pie, gotta be grateful for pie. ",
    "Happy Spanxgiving! Hope you’ve prepared your coziest, stretchiest pants for the sleepiest day of the year! Can’t wait to feast with you!",
    "Happy Thanksgiving! We’ve been training for this all year… Let’s feast!",
    "This year, I’m grateful for you… And adult beverages. Happy Thanksgiving!",
    "Who’s ready to feast?! ",
    "You bring the turkey, I’ll bring the side dishes… By which I mean booze and lots of it. Happy Thanksgiving!",
    ]
INSPIRATIONAL_TURKEY_MESSAGES=[
    "“Feeling gratitude and not expressing it is like wrapping a present and not giving it.”  — William Arthur Ward",
    "“As we express our gratitude, we must never forget that the highest appreciation is not to utter words but to live by them.” — John F. Kennedy",
    "“He is a wise man who does not grieve for the things which he has not, but rejoices for those which he has.” —  Epictetus",
    "“Joy is the simplest form of gratitude.” – Karl Barth",
    "“Silent gratitude isn’t very much to anyone.” — Gertrude Stein",
    "“Piglet noticed that even though he had a Very Small Heart, it could hold a rather large amount of Gratitude.” — A.A. Milne",
    "“We often take for granted the very things that most deserve our gratitude.” – Cynthia Ozick",
    "“Gratitude helps you to grow and expand; gratitude brings joy and laughter into your life and into the lives of all those around you.” – Eileen Caddy",
    "“The only people with whom you should try to get even are those who have helped you.” — John E. Southard",
    "“In life, one has a choice to take one of two paths: to wait for some special day–or to celebrate each special day.” —  Rasheed Ogunlaru]",
    ]
testmessage = "This is just a test"




def send_message(value):
    if value == 1:
        quote =  GENERAL_TURKEY_MESSAGES[random.randint(0,len(GENERAL_TURKEY_MESSAGES))]
    if value == 2:
        quote =  FAMILYFRIENDS_TURKEY_MESSAGES[random.randint(0,len(FAMILYFRIENDS_TURKEY_MESSAGES))]
    if value == 3:
        quote =  COLLEAGUES_TURKEY_MESSAGES[random.randint(0,len(COLLEAGUES_TURKEY_MESSAGES))]
    if value == 4:
        quote =  CLIENT_TURKEY_MESSAGES[random.randint(0,len(CLIENT_TURKEY_MESSAGES))]
    if value == 5:
        quote =  FUNNY_TURKEY_MESSAGES[random.randint(0,len(FUNNY_TURKEY_MESSAGES))]
    if value == 6:
        quote =  INSPIRATIONAL_TURKEY_MESSAGES[random.randint(0,len(INSPIRATIONAL_TURKEY_MESSAGES))]
    if value == 7:
        quote = cusmessage.get()
    cellphone = phoneentry.get()        
    account=""
    token=""
    client = Client(account,token)
    client.messages.create(to="+1"+cellphone,
                           from_=twilio_number,
                           body=quote)
    messagebox.showinfo(title="Success", message="The message has been sent")
    pygame.mixer.music.load("assets/sent.mp3")
    pygame.mixer.music.play(loops=0)
    
lbl = Label(root, bg='orange',text="Enter the Number Below",fg="white",font=large_font)    
lbl.pack()
phoneentry = Entry(root)
phoneentry.pack()

lbl2 = Label(root, bg='orange',text="Select a Message Type",fg="white",font=large_font)    
lbl2.pack()
r = IntVar()
r.set("2")
radiobtn = Radiobutton(root,variable=r,value=1,command=lambda:send_message, text="General Message",bg="orange",fg="white",font=small_font)
radiobtn.pack(anchor=W)
radiobtn = Radiobutton(root,variable=r,value=2,command=lambda:send_message,text="Family & Friends Message",bg="orange",fg="white",font=small_font)
radiobtn.pack(anchor=W)
radiobtn = Radiobutton(root,variable=r,value=3,command=lambda:send_message,text="Colleagues Message",bg="orange",fg="white",font=small_font)
radiobtn.pack(anchor=W)
radiobtn = Radiobutton(root,variable=r,value=4,command=lambda:send_message,text="Client Message",bg="orange",fg="white",font=small_font)
radiobtn.pack(anchor=W)
radiobtn = Radiobutton(root,variable=r,value=5,command=lambda:send_message,text="Funny Message",bg="orange",fg="white",font=small_font)
radiobtn.pack(anchor=W)
radiobtn = Radiobutton(root,variable=r,value=6,command=lambda:send_message,text="Inspiration Message",bg="orange",fg="white",font=small_font)
radiobtn.pack(anchor=W)
radiobtn = Radiobutton(root,variable=r,value=7,command=lambda:send_message,text="Custom Message",bg="orange",fg="white",font=small_font)
radiobtn.pack(anchor=W)
cusmessage = Entry(width=40)
cusmessage.pack(padx=10,pady=10)

msgbtn = Button(root,image= trkyimg,highlightthickness = 0, bd = 0, borderwidth=0,command=lambda: send_message(r.get()))
msgbtn.pack()

root.mainloop() 
