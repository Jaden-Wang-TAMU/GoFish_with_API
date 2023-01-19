# import urllib.request
from urllib.request import Request, urlopen
import json
# from PIL import Image
import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from tkinter.ttk import *
import urllib.request
from PIL import Image
import PIL
import requests
import io
from io import BytesIO
from PIL import ImageTk,Image
 
import os
import requests
from io import BytesIO
from tkinter import messagebox
 
 
 
global root
global root2
 
moz='Mozilla/5.0'
 
 
req = Request('https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1', headers={'User-Agent': moz})
webpage = urlopen(req).read()
data=json.loads(webpage)
id=data['deck_id']
# print(id)
print(id)
for x in range(2):
    req = Request('https://deckofcardsapi.com/api/deck/'+id+'/draw/?count=5', headers={'User-Agent': moz})
    webpage = urlopen(req).read()
    data=json.loads(webpage)
    cards=data['cards']
    card_codes=""
    for card in cards:
        card_codes=card_codes+card['code']+","
    # card_codes.__substring__(0, len(card_codes)-2)
    card_codes=card_codes[:len(card_codes)-1]
    # print(card_codes)
 
    req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_'+str(x+1)+'/add/?cards='+card_codes, headers={'User-Agent': moz})
    webpage = urlopen(req).read()
 
# print("player_1")
req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_1/list/', headers={'User-Agent': moz})
webpage = urlopen(req).read()
player_1data=json.loads(webpage)
# print(player_1data)
player_1_cards=player_1data['piles']['player_1']['cards']
# print("p1 cards:")
# print(player_1_cards)
# print("p1_images:")
# print(p1_images)
 
p1_codes=[]
for car in player_1_cards:
    p1_codes.append(car['code'])
#Player 1's Pairs
p1_pairs=[]
for cod in p1_codes:
    for cod2 in p1_codes:
        if cod!=cod2 and cod[0:1]==cod2[0:1]:
            p1_pairs.append(cod)
            p1_pairs.append(cod2)
            p1_codes.remove(cod)
            p1_codes.remove(cod2)
print("p1_codes:")
print(p1_codes)
print("p1_pairs:")
print(p1_pairs)
 
# Not drawing Player's 1 pairs
card_codes=""
for card in p1_pairs:
    card_codes=card_codes+card+","
card_codes=card_codes[:len(card_codes)-1]
if(card_codes!=""):
    req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_1/draw/?cards='+card_codes, headers={'User-Agent': moz})
    webpage = urlopen(req).read()
    req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_1_pairs/add/?cards='+card_codes, headers={'User-Agent': moz})
    webpage = urlopen(req).read()
 
req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_1/list/', headers={'User-Agent': moz})
webpage = urlopen(req).read()
player_1data=json.loads(webpage)
player_1_cards=player_1data['piles']['player_1']['cards']
p1_images=[]
for car in player_1_cards:
    p1_images.append(car['image'])
 
 
# print("player_2")
req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_2/list/', headers={'User-Agent': moz})
webpage = urlopen(req).read()
player_2data=json.loads(webpage)
# print(player_2data)
player_2_cards=player_2data['piles']['player_2']['cards']
p2_images=[]
for car in player_2_cards:
    p2_images.append(car['image'])
 
p2_codes=[]
for car in player_2_cards:
    p2_codes.append(car['code'])
p2_pairs=[]
for cod in p2_codes:
    for cod2 in p2_codes:
        if cod!=cod2 and cod[0:1]==cod2[0:1]:
            p2_pairs.append(cod)
            p2_pairs.append(cod2)
            p2_codes.remove(cod)
            p2_codes.remove(cod2)
print("p2_codes:")
print(p2_codes)
print("p2_pairs:")
print(p2_pairs)
 
# Not drawing Player's 2 pairs
card_codes=""
for card in p2_pairs:
    card_codes=card_codes+card+","
card_codes=card_codes[:len(card_codes)-1]
 
if(card_codes!=""):
    req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_2/draw/?cards='+card_codes, headers={'User-Agent': moz})
    webpage = urlopen(req).read()
    req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_2_pairs/add/?cards='+card_codes, headers={'User-Agent': moz})
    webpage = urlopen(req).read()
 
req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_2/list/', headers={'User-Agent': moz})
webpage = urlopen(req).read()
player_2data=json.loads(webpage)
player_2_cards=player_2data['piles']['player_2']['cards']
p2_images=[]
for car in player_2_cards:
    p2_images.append(car['image'])
 
originalRoot=tk.Tk()
originalRoot.title("Go Fish")
fontStyle = tkFont.Font(family="Lucida Grande", size=15)
title = tk.Label(text="Welcome to our Go Fish Game!", font=fontStyle)
title.pack()
subtitle = tk.Label(text="Use our other windows to play as Player 1 and Player 2!\nPlayer 1 will go first, then Player 2 will go, and so on until someone wins!\nEach player will type a letter or number into their search window to ask for a card.\nCheck the key to know which number or letter correlates with which card.\nMost are intuitive, but in this game, the number 0 correlates with a 10 card!\nOnly type the number or letter: '1', '2', '3', 'J', 'K', 'A', etc.\nThe suit of the card does not matter.\nIf they guess wrong, they draw a card, and it's the next player's turn.\nOnce a player collects a pair, that pair will be moved to a different screen.\nA player's pairs can be viewed by clicking 'Change Screen'.\nThroughout the game and at the beginning, you can check to see which pairs you have!\nOnce a player collects 5 pairs, they win!", font=fontStyle)
subtitle.pack()
# originalRoot.withdraw()
 
root = tk.Toplevel()
root.title("Player 1 Hand")
p1_Turn=TRUE
game_ongoing=TRUE
# root.geometry("1500x1000")
 
Cardback=ImageTk.PhotoImage(Image.open("cardback.png"))
 
img_list1 = []
panel1_list=[]
for x in range(len(p1_images)):
    img_url=p1_images[x]
    response = requests.get(img_url)
    img_data = response.content
    img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
    img_list1.append(img)
    panel = tk.Label(root, image=img_list1[x])
    panel1_list.append(panel)
for p in panel1_list:
    p.pack(side="left", fill="none", expand="no")
 
 
 
root2=tk.Toplevel()
root2.title("Player 2 Hand")
 
img_list2 = []
panel2_list=[]
for x in range(len(p2_images)):
    img_list2.append(Cardback)
    panel=tk.Label(root2, image=img_list2[x])
    panel2_list.append(panel)
#     img_url=p2_images[x]
#     response = requests.get(img_url)
#     img_data = response.content
#     img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
#     img_list2.append(img)
#     panel = tk.Label(root2, image=img_list2[x])
#     panel2_list.append(panel)
for p in panel2_list:
    p.pack(side="left", fill="none", expand="no")
 
 
rootKey= tk.Toplevel()
rootKey.title("Card Key")
TEXT = Text(rootKey, height=13,width=85)
TEXT.pack()
t= "A=Ace\n"
TEXT.insert(tk.END, t)
t= "2 = Two\n"
TEXT.insert(tk.END, t)
t= "3 = Three\n"
TEXT.insert(tk.END, t)
t= "4 = Four\n"
TEXT.insert(tk.END, t)
t= "5 = Five\n"
TEXT.insert(tk.END, t)
t= "6 = Six\n"
TEXT.insert(tk.END, t)
t= "7 = Seven\n"
TEXT.insert(tk.END, t)
t= "8 = Eight\n"
TEXT.insert(tk.END, t)
t= "9 = Nine\n"
TEXT.insert(tk.END, t)
t= "0 = Ten\n"
TEXT.insert(tk.END, t)
t= "J = Jack\n"
TEXT.insert(tk.END, t)
t= "Q = Queen\n"
TEXT.insert(tk.END, t)
t= "K = King\n"
TEXT.insert(tk.END, t)
 
 
def p1find():
    global p1_Turn
    global panel1_list
    global panel2_list
    global p1_codes
    global p2_codes
    global player_1_cards
    global player_2_cards
    global img_list1
    global img_list2
    global p1_pairs
    global p2_pairs
    global Cardback
    global p2_images
    p1_chosen=p1_entry.get()
    if p1_Turn and p1_chosen!="":
        not_Found=True
        for x in p2_codes:
            if p1_chosen==x[0:1]:
                for y in player_2_cards:
                    if y['code']==x:
                        req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_2/draw/?cards='+x, headers={'User-Agent': moz})
                        urlopen(req).read()
 
                        req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_1/add/?cards='+x, headers={'User-Agent': moz})
                        urlopen(req).read()
 
                        print("grabbed a "+x+" from player 2")
                        req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_1/list/', headers={'User-Agent': moz})
                        webpage=urlopen(req).read()
                        player_1data=json.loads(webpage)
                        player_1_cards=player_1data['piles']['player_1']['cards']
                        p1_codes=[]
                        for car in player_1_cards:
                            p1_codes.append(car['code'])
                        
                        temp_pairs=[]
                        for cod in p1_codes:
                            for cod2 in p1_codes:
                                if cod!=cod2 and cod[0:1]==cod2[0:1]:
                                    temp_pairs.append(cod)
                                    temp_pairs.append(cod2)
                                    p1_pairs.append(cod)
                                    p1_pairs.append(cod2)
                                    p1_codes.remove(cod)
                                    p1_codes.remove(cod2)
                        card_codes=""
                        for card in temp_pairs:
                            card_codes=card_codes+card+","
                        card_codes=card_codes[:len(card_codes)-1]
                        if(card_codes!=""):
                            req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_1/draw/?cards='+card_codes, headers={'User-Agent': moz})
                            urlopen(req).read()
                            req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_1_pairs/add/?cards='+card_codes, headers={'User-Agent': moz})
                            urlopen(req).read()
                            print("player 1 found pairs of "+card_codes)
                            req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_1/list/', headers={'User-Agent': moz})
                            webpage=urlopen(req).read()
                            player_1data=json.loads(webpage)
                            player_1_cards=player_1data['piles']['player_1']['cards']
                            if len(player_1_cards)==0:
                                req = Request('https://deckofcardsapi.com/api/deck/'+id+'/draw/?count=5', headers={'User-Agent': moz})
                                webpage = urlopen(req).read()
                                data=json.loads(webpage)
                                cards=data['cards']
                                card_codes=""
                                for card in cards:
                                    card_codes=card_codes+card['code']+","
                                card_codes=card_codes[:len(card_codes)-1]                        
                                req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_1/add/?cards='+card_codes, headers={'User-Agent': moz})
                                urlopen(req).read()
                                print("player 1 drew 5 new cards")
                                req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_1/list/', headers={'User-Agent': moz})
                                webpage=urlopen(req).read()
                                player_1data=json.loads(webpage)
                                player_1_cards=player_1data['piles']['player_1']['cards']
                                p1_codes=[]
                                for car in player_1_cards:
                                    p1_codes.append(car['code'])
                                temp_pairs=[]
                                for cod in p1_codes:
                                    for cod2 in p1_codes:
                                        if cod!=cod2 and cod[0:1]==cod2[0:1]:
                                            temp_pairs.append(cod)
                                            temp_pairs.append(cod2)
                                            p1_pairs.append(cod)
                                            p1_pairs.append(cod2)
                                            p1_codes.remove(cod)
                                            p1_codes.remove(cod2)
                                card_codes=""
                                for card in temp_pairs:
                                    card_codes=card_codes+card+","
                                card_codes=card_codes[:len(card_codes)-1]
                                if(card_codes!=""):
                                    req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_1/draw/?cards='+card_codes, headers={'User-Agent': moz})
                                    urlopen(req).read()
                                    req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_1_pairs/add/?cards='+card_codes, headers={'User-Agent': moz})
                                    urlopen(req).read()
                                    print("player 1 found pairs of "+card_codes)
                                    
 
 
                        req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_2/list/', headers={'User-Agent': moz})
                        webpage=urlopen(req).read()
                        player_2data=json.loads(webpage)
                        player_2_cards=player_2data['piles']['player_2']['cards']
                        if len(player_2_cards)==0:
                            req = Request('https://deckofcardsapi.com/api/deck/'+id+'/draw/?count=5', headers={'User-Agent': moz})
                            webpage = urlopen(req).read()
                            data=json.loads(webpage)
                            cards=data['cards']
                            card_codes=""
                            for card in cards:
                                card_codes=card_codes+card['code']+","
                            card_codes=card_codes[:len(card_codes)-1]                        
                            req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_2/add/?cards='+card_codes, headers={'User-Agent': moz})
                            urlopen(req).read()
                            print("player 2 drew 5 new cards")
                            req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_2/list/', headers={'User-Agent': moz})
                            webpage=urlopen(req).read()
                            player_2data=json.loads(webpage)
                            player_2_cards=player_2data['piles']['player_2']['cards']
                            p2_codes=[]
                            for car in player_2_cards:
                                p2_codes.append(car['code'])
                            temp_pairs=[]
                            for cod in p2_codes:
                                for cod2 in p2_codes:
                                    if cod!=cod2 and cod[0:1]==cod2[0:1]:
                                        temp_pairs.append(cod)
                                        temp_pairs.append(cod2)
                                        p2_pairs.append(cod)
                                        p2_pairs.append(cod2)
                                        p2_codes.remove(cod)
                                        p2_codes.remove(cod2)
                            card_codes=""
                            for card in temp_pairs:
                                card_codes=card_codes+card+","
                            card_codes=card_codes[:len(card_codes)-1]
                            if(card_codes!=""):
                                req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_2/draw/?cards='+card_codes, headers={'User-Agent': moz})
                                urlopen(req).read()
                                req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_2_pairs/add/?cards='+card_codes, headers={'User-Agent': moz})
                                urlopen(req).read()
                                print("player 2 found pairs of "+card_codes)
 
                        req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_1/list/', headers={'User-Agent': moz})
                        webpage = urlopen(req).read()
                        player_1data=json.loads(webpage)
                        player_1_cards=player_1data['piles']['player_1']['cards']
                        p1_images=[]
                        for car in player_1_cards:
                            p1_images.append(car['image'])
 
                        req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_2/list/', headers={'User-Agent': moz})
                        webpage = urlopen(req).read()
                        player_2data=json.loads(webpage)
                        # print(player_2data)
                        player_2_cards=player_2data['piles']['player_2']['cards']
                        p2_images=[]
                        for car in player_2_cards:
                            p2_images.append(car['image'])
 
                        p1_codes=[]
                        for car in player_1_cards:
                            p1_codes.append(car['code'])
                        print("p1_codes:")
                        print(p1_codes)
                        
                        p2_codes=[]
                        for car in player_2_cards:
                            p2_codes.append(car['code'])
                        print("p2_codes:")
                        print(p2_codes)
 
                        for p in panel1_list:
                            p.destroy()
                        for p in panel2_list:
                            p.destroy()

                        img_list1 = []
                        panel1_list=[]
                        for x in range(len(p1_images)):
                            img_url=p1_images[x]
                            response = requests.get(img_url)
                            img_data = response.content
                            img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
                            img_list1.append(img)
                            panel = tk.Label(root, image=img_list1[x])
                            panel1_list.append(panel)
                        for p in panel1_list:
                            p.pack(side="left", fill="none", expand="no")
                       
                        img_list2 = []
                        panel2_list=[]
                        for x in range(len(p2_images)):
                            img_list2.append(Cardback)
                            panel=tk.Label(root2, image=img_list2[x])
                            panel2_list.append(panel)
                            # img_url=p2_images[x]
                            # response = requests.get(img_url)
                            # img_data = response.content
                            # img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
                            # img_list2.append(img)
                            # panel = tk.Label(root2, image=img_list2[x])
                            # panel2_list.append(panel)
                        for p in panel2_list:
                            p.pack(side="left", fill="none", expand="no")
 
                        print("Guessed Correctly")
                        print("p1_codes:")
                        print(p1_codes)
                        print("p1_pairs:")
                        print(p1_pairs)
                        print("p2_codes:")
                        print(p2_codes)
                        print("p2_pairs:")
                        print(p2_pairs)
                        not_Found=False
                        if len(p1_pairs)>=10:
                            messagebox.showinfo("Winner!", "Congratulations! Player 1 wins!")
                        if len(p2_pairs)>=10:
                            messagebox.showinfo("Winner!", "Congratulations! Player 2 wins!")
                        break
                if not_Found==False:
                    break
        if not_Found:
            p1_Turn=False
            req = Request('https://deckofcardsapi.com/api/deck/'+id+'/draw/?count=1', headers={'User-Agent': moz})
            webpage = urlopen(req).read()
            data=json.loads(webpage)
            cards=data['cards']
            card_code=cards[0]['code']
            req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_1/add/?cards='+card_code, headers={'User-Agent': moz})
            urlopen(req).read()
            print('drew a '+card_code+'from deck')
 
            req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_1/list/', headers={'User-Agent': moz})
            webpage=urlopen(req).read()
            player_1data=json.loads(webpage)
            player_1_cards=player_1data['piles']['player_1']['cards']
            p1_codes=[]
            for car in player_1_cards:
                p1_codes.append(car['code'])
            
            temp_pairs=[]
            for cod in p1_codes:
                for cod2 in p1_codes:
                    if cod!=cod2 and cod[0:1]==cod2[0:1]:
                        temp_pairs.append(cod)
                        temp_pairs.append(cod2)
                        p1_pairs.append(cod)
                        p1_pairs.append(cod2)
                        p1_codes.remove(cod)
                        p1_codes.remove(cod2)
            card_codes=""
            for card in temp_pairs:
                card_codes=card_codes+card+","
            card_codes=card_codes[:len(card_codes)-1]
            if(card_codes!=""):
                req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_1/draw/?cards='+card_codes, headers={'User-Agent': moz})
                urlopen(req).read()
                req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_1_pairs/add/?cards='+card_codes, headers={'User-Agent': moz})
                urlopen(req).read()
                print("player 1 found pairs of "+card_codes)
                req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_1/list/', headers={'User-Agent': moz})
                webpage=urlopen(req).read()
                player_1data=json.loads(webpage)
                player_1_cards=player_1data['piles']['player_1']['cards']
                if len(player_1_cards)==0:
                    req = Request('https://deckofcardsapi.com/api/deck/'+id+'/draw/?count=5', headers={'User-Agent': moz})
                    webpage = urlopen(req).read()
                    data=json.loads(webpage)
                    cards=data['cards']
                    card_codes=""
                    for card in cards:
                        card_codes=card_codes+card['code']+","
                    card_codes=card_codes[:len(card_codes)-1]                        
                    req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_1/add/?cards='+card_codes, headers={'User-Agent': moz})
                    urlopen(req).read()
                    print("player 1 drew 5 new cards")
                    req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_1/list/', headers={'User-Agent': moz})
                    webpage=urlopen(req).read()
                    player_1data=json.loads(webpage)
                    player_1_cards=player_1data['piles']['player_1']['cards']
                    p1_codes=[]
                    for car in player_1_cards:
                        p1_codes.append(car['code'])
                    temp_pairs=[]
                    for cod in p1_codes:
                        for cod2 in p1_codes:
                            if cod!=cod2 and cod[0:1]==cod2[0:1]:
                                temp_pairs.append(cod)
                                temp_pairs.append(cod2)
                                p1_pairs.append(cod)
                                p1_pairs.append(cod2)
                                p1_codes.remove(cod)
                                p1_codes.remove(cod2)
                    card_codes=""
                    for card in temp_pairs:
                        card_codes=card_codes+card+","
                    card_codes=card_codes[:len(card_codes)-1]
                    if(card_codes!=""):
                        req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_1/draw/?cards='+card_codes, headers={'User-Agent': moz})
                        urlopen(req).read()
                        req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_1_pairs/add/?cards='+card_codes, headers={'User-Agent': moz})
                        urlopen(req).read()
                        print("player 1 found pairs of "+card_codes)
 
            req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_1/list/', headers={'User-Agent': moz})
            webpage = urlopen(req).read()
            player_1data=json.loads(webpage)
            player_1_cards=player_1data['piles']['player_1']['cards']
            p1_images=[]
            for car in player_1_cards:
                p1_images.append(car['image'])
            
            for p in panel1_list:
                p.destroy()
            img_list1 = []
            panel1_list=[]
            for x in range(len(p1_images)):
                img_list1.append(Cardback)
                panel=tk.Label(root, image=img_list1[x])
                panel1_list.append(panel)
                # img_url=p1_images[x]
                # response = requests.get(img_url)
                # img_data = response.content
                # img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
                # img_list1.append(img)
                # panel = tk.Label(root, image=img_list1[x])
                # panel1_list.append(panel)
            for p in panel1_list:
                p.pack(side="left", fill="none", expand="no")
            
            req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_2/list/', headers={'User-Agent': moz})
            webpage=urlopen(req).read()
            player_2data=json.loads(webpage)
            player_2_cards=player_2data['piles']['player_2']['cards']
            p2_images=[]
            for car in player_2_cards:
                p2_images.append(car['image'])
            for p in panel2_list:
                p.destroy()
            img_list2 = []
            panel2_list=[]
            for x in range(len(p2_images)):
                img_url=p2_images[x]
                response = requests.get(img_url)
                img_data = response.content
                img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
                img_list2.append(img)
                panel = tk.Label(root2, image=img_list2[x])
                panel2_list.append(panel)
            for p in panel2_list:
                p.pack(side="left", fill="none", expand="no")
            
            print("Guessed wrong, player 2's turn now")
            print("p1_codes:")
            print(p1_codes)
            print("p1_pairs:")
            print(p1_pairs)
            print("p2_codes:")
            print(p2_codes)
            print("p2_pairs:")
            print(p2_pairs)
            if len(p1_pairs)>=10:
                messagebox.showinfo("Winner!", "Congratulations! Player 1 wins!")
            if len(p2_pairs)>=10:
                messagebox.showinfo("Winner!", "Congratulations! Player 2 wins!")
 
 
def p2find():
    global p1_Turn
    global panel1_list
    global panel2_list
    global p1_codes
    global p2_codes
    global player_1_cards
    global player_2_cards
    global img_list1
    global img_list2
    global p1_pairs
    global p2_pairs
    global p1_images
    p2_chosen=p2_entry.get()
    if p1_Turn==False and p2_chosen!="":
        not_Found=True
        for x in p1_codes:
            if p2_chosen==x[0:1]:
                for y in player_1_cards:
                    if y['code']==x:
                        req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_1/draw/?cards='+x, headers={'User-Agent': moz})
                        urlopen(req).read()
 
                        req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_2/add/?cards='+x, headers={'User-Agent': moz})
                        urlopen(req).read()
 
                        print("grabbed a "+x+" from player 1")
                        req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_2/list/', headers={'User-Agent': moz})
                        webpage=urlopen(req).read()
                        player_2data=json.loads(webpage)
                        player_2_cards=player_2data['piles']['player_2']['cards']
                        p2_codes=[]
                        for car in player_2_cards:
                            p2_codes.append(car['code'])
                        
                        temp_pairs=[]
                        for cod in p2_codes:
                            for cod2 in p2_codes:
                                if cod!=cod2 and cod[0:1]==cod2[0:1]:
                                    temp_pairs.append(cod)
                                    temp_pairs.append(cod2)
                                    p2_pairs.append(cod)
                                    p2_pairs.append(cod2)
                                    p2_codes.remove(cod)
                                    p2_codes.remove(cod2)
                        card_codes=""
                        for card in temp_pairs:
                            card_codes=card_codes+card+","
                        card_codes=card_codes[:len(card_codes)-1]
                        if(card_codes!=""):
                            req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_2/draw/?cards='+card_codes, headers={'User-Agent': moz})
                            urlopen(req).read()
                            req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_2_pairs/add/?cards='+card_codes, headers={'User-Agent': moz})
                            urlopen(req).read()
                            print("player 2 found pairs of "+card_codes)
                            req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_2/list/', headers={'User-Agent': moz})
                            webpage=urlopen(req).read()
                            player_2data=json.loads(webpage)
                            player_2_cards=player_2data['piles']['player_2']['cards']
                            if len(player_2_cards)==0:
                                req = Request('https://deckofcardsapi.com/api/deck/'+id+'/draw/?count=5', headers={'User-Agent': moz})
                                webpage = urlopen(req).read()
                                data=json.loads(webpage)
                                cards=data['cards']
                                card_codes=""
                                for card in cards:
                                    card_codes=card_codes+card['code']+","
                                card_codes=card_codes[:len(card_codes)-1]                        
                                req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_2/add/?cards='+card_codes, headers={'User-Agent': moz})
                                urlopen(req).read()
                                print("player 2 drew 5 new cards")
                                req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_2/list/', headers={'User-Agent': moz})
                                webpage=urlopen(req).read()
                                player_2data=json.loads(webpage)
                                player_2_cards=player_2data['piles']['player_2']['cards']
                                p2_codes=[]
                                for car in player_2_cards:
                                    p2_codes.append(car['code'])
                                temp_pairs=[]
                                for cod in p2_codes:
                                    for cod2 in p2_codes:
                                        if cod!=cod2 and cod[0:1]==cod2[0:1]:
                                            temp_pairs.append(cod)
                                            temp_pairs.append(cod2)
                                            p2_pairs.append(cod)
                                            p2_pairs.append(cod2)
                                            p2_codes.remove(cod)
                                            p2_codes.remove(cod2)

                                card_codes=""
                                for card in temp_pairs:
                                    card_codes=card_codes+card+","
                                card_codes=card_codes[:len(card_codes)-1]
                                if(card_codes!=""):
                                    req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_2/draw/?cards='+card_codes, headers={'User-Agent': moz})
                                    urlopen(req).read()
                                    req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_2_pairs/add/?cards='+card_codes, headers={'User-Agent': moz})
                                    urlopen(req).read()
                                    print("player 2 found pairs of "+card_codes)
 
                        req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_1/list/', headers={'User-Agent': moz})
                        webpage=urlopen(req).read()
                        player_1data=json.loads(webpage)
                        player_1_cards=player_1data['piles']['player_1']['cards']
                        if len(player_1_cards)==0:
                            req = Request('https://deckofcardsapi.com/api/deck/'+id+'/draw/?count=5', headers={'User-Agent': moz})
                            webpage = urlopen(req).read()
                            data=json.loads(webpage)
                            cards=data['cards']
                            card_codes=""
                            for card in cards:
                                card_codes=card_codes+card['code']+","
                            card_codes=card_codes[:len(card_codes)-1]                        
                            req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_1/add/?cards='+card_codes, headers={'User-Agent': moz})
                            urlopen(req).read()
                            print("player 1 drew 5 new cards")
                            req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_1/list/', headers={'User-Agent': moz})
                            webpage=urlopen(req).read()
                            player_1data=json.loads(webpage)
                            player_1_cards=player_1data['piles']['player_1']['cards']
                            p1_codes=[]
                            for car in player_1_cards:
                                p1_codes.append(car['code'])
                            temp_pairs=[]
                            for cod in p1_codes:
                                for cod2 in p1_codes:
                                    if cod!=cod2 and cod[0:1]==cod2[0:1]:
                                        temp_pairs.append(cod)
                                        temp_pairs.append(cod2)
                                        p1_pairs.append(cod)
                                        p1_pairs.append(cod2)
                                        p1_codes.remove(cod)
                                        p1_codes.remove(cod2)
                                        
                            card_codes=""
                            for card in temp_pairs:
                                card_codes=card_codes+card+","
                            card_codes=card_codes[:len(card_codes)-1]
                            if(card_codes!=""):
                                req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_1/draw/?cards='+card_codes, headers={'User-Agent': moz})
                                urlopen(req).read()
                                req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_1_pairs/add/?cards='+card_codes, headers={'User-Agent': moz})
                                urlopen(req).read()
                                print("player 1 found pairs of "+card_codes)
 
 
                        req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_2/list/', headers={'User-Agent': moz})
                        webpage = urlopen(req).read()
                        player_2data=json.loads(webpage)
                        # print(player_2data)
                        player_2_cards=player_2data['piles']['player_2']['cards']
                        p2_images=[]
                        for car in player_2_cards:
                            p2_images.append(car['image'])
 
                        req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_1/list/', headers={'User-Agent': moz})
                        webpage = urlopen(req).read()
                        player_1data=json.loads(webpage)
                        # print(player_1data)
                        player_1_cards=player_1data['piles']['player_1']['cards']
                        p1_images=[]
                        for car in player_1_cards:
                            p1_images.append(car['image'])
 
                        p1_codes=[]
                        for car in player_1_cards:
                            p1_codes.append(car['code'])
 
                        
                        p2_codes=[]
                        for car in player_2_cards:
                            p2_codes.append(car['code'])
 
                        for p in panel1_list:
                            p.destroy()
                        for p in panel2_list:
                            p.destroy()
                       
                        img_list1 = []
                        panel1_list=[]
                        for x in range(len(p1_images)):
                            img_list1.append(Cardback)
                            panel=tk.Label(root, image=img_list1[x])
                            panel1_list.append(panel)
                            # img_url=p1_images[x]
                            # response = requests.get(img_url)
                            # img_data = response.content
                            # img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
                            # img_list1.append(img)
                            # panel = tk.Label(root, image=img_list1[x])
                            # panel1_list.append(panel)
                        for p in panel1_list:
                            p.pack(side="left", fill="none", expand="no")
                        
                        img_list2 = []
                        panel2_list=[]
                        for x in range(len(p2_images)):
                            img_url=p2_images[x]
                            response = requests.get(img_url)
                            img_data = response.content
                            img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
                            img_list2.append(img)
                            panel = tk.Label(root2, image=img_list2[x])
                            panel2_list.append(panel)
                        for p in panel2_list:
                            p.pack(side="left", fill="none", expand="no")
 
                        print("Guessed Correctly")
                        print("p1_codes:")
                        print(p1_codes)
                        print("p1_pairs:")
                        print(p1_pairs)
                        print("p2_codes:")
                        print(p2_codes)
                        print("p2_pairs:")
                        print(p2_pairs)
                        not_Found=False
                        if len(p1_pairs)>=10:
                            messagebox.showinfo("Winner!", "Congratulations! Player 1 wins!")
                        if len(p2_pairs)>=10:
                            messagebox.showinfo("Winner!", "Congratulations! Player 2 wins!")
                        break
                if not_Found==False:
                    break
        if not_Found:
            p1_Turn=True
            req = Request('https://deckofcardsapi.com/api/deck/'+id+'/draw/?count=1', headers={'User-Agent': moz})
            webpage = urlopen(req).read()
            data=json.loads(webpage)
            cards=data['cards']
            card_code=cards[0]['code']
            req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_2/add/?cards='+card_code, headers={'User-Agent': moz})
            urlopen(req).read()
            print('player 2 drew a '+card_code+'from deck')
            
            req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_2/list/', headers={'User-Agent': moz})
            webpage=urlopen(req).read()
            player_2data=json.loads(webpage)
            player_2_cards=player_2data['piles']['player_2']['cards']
            p2_codes=[]
            for car in player_2_cards:
                p2_codes.append(car['code'])
                        
            temp_pairs=[]
            for cod in p2_codes:
                for cod2 in p2_codes:
                    if cod!=cod2 and cod[0:1]==cod2[0:1]:
                        temp_pairs.append(cod)
                        temp_pairs.append(cod2)
                        p2_pairs.append(cod)
                        p2_pairs.append(cod2)
                        p2_codes.remove(cod)
                        p2_codes.remove(cod2)

            card_codes=""
            for card in temp_pairs:
                card_codes=card_codes+card+","
            card_codes=card_codes[:len(card_codes)-1]
            if(card_codes!=""):
                req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_2/draw/?cards='+card_codes, headers={'User-Agent': moz})
                urlopen(req).read()
                req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_2_pairs/add/?cards='+card_codes, headers={'User-Agent': moz})
                urlopen(req).read()
                print("player 2 found new pair of "+card_codes)
                req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_2/list/', headers={'User-Agent': moz})
                webpage=urlopen(req).read()
                player_2data=json.loads(webpage)
                player_2_cards=player_2data['piles']['player_2']['cards']
                if len(player_2_cards)==0:
                    req = Request('https://deckofcardsapi.com/api/deck/'+id+'/draw/?count=5', headers={'User-Agent': moz})
                    webpage = urlopen(req).read()
                    data=json.loads(webpage)
                    cards=data['cards']
                    card_codes=""
                    for card in cards:
                        card_codes=card_codes+card['code']+","
                    card_codes=card_codes[:len(card_codes)-1]                        
                    req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_2/add/?cards='+card_codes, headers={'User-Agent': moz})
                    urlopen(req).read()
                    print("player 2 drew 5 new cards")
                    req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_2/list/', headers={'User-Agent': moz})
                    webpage=urlopen(req).read()
                    player_2data=json.loads(webpage)
                    player_2_cards=player_2data['piles']['player_2']['cards']
                    p2_codes=[]
                    for car in player_2_cards:
                        p2_codes.append(car['code'])
                    temp_pairs=[]
                    for cod in p2_codes:
                        for cod2 in p2_codes:
                            if cod!=cod2 and cod[0:1]==cod2[0:1]:
                                temp_pairs.append(cod)
                                temp_pairs.append(cod2)
                                p2_pairs.append(cod)
                                p2_pairs.append(cod2)
                                p2_codes.remove(cod)
                                p2_codes.remove(cod2)
                    card_codes=""
                    for card in temp_pairs:
                        card_codes=card_codes+card+","
                    card_codes=card_codes[:len(card_codes)-1]
                    if(card_codes!=""):
                        req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_2/draw/?cards='+card_codes, headers={'User-Agent': moz})
                        urlopen(req).read()
                        req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_2_pairs/add/?cards='+card_codes, headers={'User-Agent': moz})
                        urlopen(req).read()
                        print("player 2 found pairs of "+card_codes)
                        req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_2/list/', headers={'User-Agent': moz})
                        webpage=urlopen(req).read()
                        player_2data=json.loads(webpage)
                        player_2_cards=player_2data['piles']['player_2']['cards']    
            
            p2_images=[]
            for car in player_2_cards:
                p2_images.append(car['image'])
            p2_codes=[]
            for car in player_2_cards:
                p2_codes.append(car['code'])
            for p in panel2_list:
                p.destroy()
            img_list2 = []
            panel2_list=[]
            for x in range(len(p2_images)):
                img_list2.append(Cardback)
                panel=tk.Label(root2, image=img_list2[x])
                panel2_list.append(panel)
                # img_url=p2_images[x]
                # response = requests.get(img_url)
                # img_data = response.content
                # img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
                # img_list2.append(img)
                # panel = tk.Label(root2, image=img_list2[x])
                # panel2_list.append(panel)
            for p in panel2_list:
                p.pack(side="left", fill="none", expand="no")


            req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_1/list/', headers={'User-Agent': moz})
            webpage = urlopen(req).read()
            player_1data=json.loads(webpage)
            # print(player_1data)
            player_1_cards=player_1data['piles']['player_1']['cards']
            p1_images=[]
            for car in player_1_cards:
                p1_images.append(car['image'])
            for p in panel1_list:
                p.destroy()
            img_list1 = []
            panel1_list=[]
            for x in range(len(p1_images)):
                img_url=p1_images[x]
                response = requests.get(img_url)
                img_data = response.content
                img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
                img_list1.append(img)
                panel = tk.Label(root, image=img_list1[x])
                panel1_list.append(panel)
            for p in panel1_list:
                p.pack(side="left", fill="none", expand="no")
 
            print("Guessed Wrong, player 1's turn now")
            print("p1_codes:")
            print(p1_codes)
            print("p1_pairs:")
            print(p1_pairs)
            print("p2_codes:")
            print(p2_codes)
            print("p2_pairs:")
            print(p2_pairs)
            if len(p1_pairs)>=10:
                messagebox.showinfo("Winner!", "Congratulations! Player 1 wins!")
            if len(p2_pairs)>=10:
                messagebox.showinfo("Winner!", "Congratulations! Player 2 wins!")

p1screen = False
p2screen = False
 
def changeP1Screen():
    print("changing p1screen")
    global p1screen
    global panel1_list
    global img_list1
    global p1_pairs
    if len(p1_pairs)>0:
        if p1screen:
            p1screen = False
            for p in panel1_list:
                p.destroy()
            req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_1/list/', headers={'User-Agent': moz})
            webpage=urlopen(req).read()
            player_1_pairdata=json.loads(webpage)
            player_1_pairs=player_1_pairdata['piles']['player_1']['cards']
            player1_pairimages = []
            for car in player_1_pairs:
                player1_pairimages.append(car['image'])
            img_list1 = []
            panel1_list=[]
            for x in range(len(player1_pairimages)):
                img_url=player1_pairimages[x]
                response = requests.get(img_url)
                img_data = response.content
                img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
                img_list1.append(img)
                panel = tk.Label(root, image=img_list1[x])
                panel1_list.append(panel)
            for p in panel1_list:
                p.pack(side="left", fill="none", expand="no")
    
        else:
            p1screen = True
            for p in panel1_list:
                p.destroy()
            req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_1_pairs/list/', headers={'User-Agent': moz})
            webpage=urlopen(req).read()
            player_1_pairdata=json.loads(webpage)
            player_1_pairs=player_1_pairdata['piles']['player_1_pairs']['cards']
            player1_pairimages = []
            for car in player_1_pairs:
                player1_pairimages.append(car['image'])
            img_list1 = []
            panel1_list=[]
            for x in range(len(player1_pairimages)):
                img_url=player1_pairimages[x]
                response = requests.get(img_url)
                img_data = response.content
                img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
                img_list1.append(img)
                panel = tk.Label(root, image=img_list1[x])
                panel1_list.append(panel)
            for p in panel1_list:
                p.pack(side="left", fill="none", expand="no")
    
def changeP2Screen():
    print("changing p2screen")
    global p2screen
    global panel2_list
    global img_list2
    global p1_pairs
    if len(p2_pairs)>0:
        if p2screen:
            p2screen = False
            for p in panel2_list:
                p.destroy()
            req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_2/list/', headers={'User-Agent': moz})
            webpage=urlopen(req).read()
            player_2_pairdata=json.loads(webpage)
            player_2_pairs=player_2_pairdata['piles']['player_2']['cards']
            player2_pairimages = []
            for car in player_2_pairs:
                player2_pairimages.append(car['image'])
            img_list2 = []
            panel2_list=[]
            for x in range(len(player2_pairimages)):
                img_url=player2_pairimages[x]
                response = requests.get(img_url)
                img_data = response.content
                img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
                img_list2.append(img)
                panel = tk.Label(root2, image=img_list2[x])
                panel2_list.append(panel)
            for p in panel2_list:
                p.pack(side="left", fill="none", expand="no")
    
        else:
            p2screen = True
            for p in panel2_list:
                p.destroy()
            req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_2_pairs/list/', headers={'User-Agent': moz})
            webpage=urlopen(req).read()
            player_2_pairdata=json.loads(webpage)
            player_2_pairs=player_2_pairdata['piles']['player_2_pairs']['cards']
            player2_pairimages = []
            for car in player_2_pairs:
                player2_pairimages.append(car['image'])
            img_list2 = []
            panel2_list=[]
            for x in range(len(player2_pairimages)):
                img_url=player2_pairimages[x]
                response = requests.get(img_url)
                img_data = response.content
                img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
                img_list2.append(img)
                panel = tk.Label(root2, image=img_list2[x])
                panel2_list.append(panel)
            for p in panel2_list:
                p.pack(side="left", fill="none", expand="no")
    
my_menu=Menu(root)
root.config(menu=my_menu)
my_menu.add_command(label="Change Screen", command = changeP1Screen)
 
 
 
my_menu2=Menu(root2)
root2.config(menu=my_menu2)
my_menu2.add_command(label="Change Screen", command = changeP2Screen)
 
def Reset():
    print("reset")
    global id
    global p1_Turn
    global panel1_list
    global panel2_list
    global p1_codes
    global p2_codes
    global player_1_cards
    global player_2_cards
    global img_list1
    global img_list2
    global p1_pairs
    global p2_pairs
    global game_ongoing
    global p1screen
    global p2screen
    p1screen=False
    p2screen=False
    p1_Turn=True
    game_ongoing=True
    req = Request('https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1', headers={'User-Agent': moz})
    webpage = urlopen(req).read()
    data=json.loads(webpage)
    id=data['deck_id']
    print(id)
    for x in range(2):
        req = Request('https://deckofcardsapi.com/api/deck/'+id+'/draw/?count=5', headers={'User-Agent': moz})
        webpage = urlopen(req).read()
        data=json.loads(webpage)
        cards=data['cards']
        card_codes=""
        for card in cards:
            card_codes=card_codes+card['code']+","
        card_codes=card_codes[:len(card_codes)-1]
    
        req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_'+str(x+1)+'/add/?cards='+card_codes, headers={'User-Agent': moz})
        urlopen(req).read()
    
    req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_1/list/', headers={'User-Agent': moz})
    webpage = urlopen(req).read()
    player_1data=json.loads(webpage)
    player_1_cards=player_1data['piles']['player_1']['cards']
    p1_codes=[]
    for car in player_1_cards:
        p1_codes.append(car['code'])
 
    #Player 1's Pairs
    p1_pairs=[]
    for cod in p1_codes:
        for cod2 in p1_codes:
            if cod!=cod2 and cod[0:1]==cod2[0:1]:
                p1_pairs.append(cod)
                p1_pairs.append(cod2)
                p1_codes.remove(cod)
                p1_codes.remove(cod2)
    print("p1_codes:")
    print(p1_codes)
    print("p1_pairs:")
    print(p1_pairs)
    
    # Not drawing Player's 1 pairs
    card_codes=""
    for card in p1_pairs:
        card_codes=card_codes+card+","
    card_codes=card_codes[:len(card_codes)-1]
    if(card_codes!=""):
        req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_1/draw/?cards='+card_codes, headers={'User-Agent': moz})
        urlopen(req).read()
        req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_1_pairs/add/?cards='+card_codes, headers={'User-Agent': moz})
        urlopen(req).read()
    
    req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_1/list/', headers={'User-Agent': moz})
    webpage = urlopen(req).read()
    player_1data=json.loads(webpage)
    player_1_cards=player_1data['piles']['player_1']['cards']
    p1_images=[]
    for car in player_1_cards:
        p1_images.append(car['image'])
    
 
    req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_2/list/', headers={'User-Agent': moz})
    webpage = urlopen(req).read()
    player_2data=json.loads(webpage)
    player_2_cards=player_2data['piles']['player_2']['cards']
    p2_images=[]
    for car in player_2_cards:
        p2_images.append(car['image'])
    
    p2_codes=[]
    for car in player_2_cards:
        p2_codes.append(car['code'])
    p2_pairs=[]
    for cod in p2_codes:
        for cod2 in p2_codes:
            if cod!=cod2 and cod[0:1]==cod2[0:1]:
                p2_pairs.append(cod)
                p2_pairs.append(cod2)
                p2_codes.remove(cod)
                p2_codes.remove(cod2)
    print("p2_codes:")
    print(p2_codes)
    print("p2_pairs:")
    print(p2_pairs)
    
    # Not drawing Player's 2 pairs
    card_codes=""
    for card in p2_pairs:
        card_codes=card_codes+card+","
    card_codes=card_codes[:len(card_codes)-1]
    
    if(card_codes!=""):
        req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_2/draw/?cards='+card_codes, headers={'User-Agent': moz})
        urlopen(req).read()
        req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_2_pairs/add/?cards='+card_codes, headers={'User-Agent': moz})
        urlopen(req).read()
    
    req = Request('https://deckofcardsapi.com/api/deck/'+id+'/pile/player_2/list/', headers={'User-Agent': moz})
    webpage = urlopen(req).read()
    player_2data=json.loads(webpage)
    player_2_cards=player_2data['piles']['player_2']['cards']
    p2_images=[]
    for car in player_2_cards:
        p2_images.append(car['image'])
    
    for p in panel1_list:
        p.destroy()
    for p in panel2_list:
        p.destroy()
 
    img_list1 = []
    panel1_list=[]
    for x in range(len(p1_images)):
        img_url=p1_images[x]
        response = requests.get(img_url)
        img_data = response.content
        img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
        img_list1.append(img)
        panel = tk.Label(root, image=img_list1[x])
        panel1_list.append(panel)
    for p in panel1_list:
        p.pack(side="left", fill="none", expand="no")
    
    img_list2 = []
    panel2_list=[]
    for x in range(len(p2_images)):
        img_url=p2_images[x]
        response = requests.get(img_url)
        img_data = response.content
        img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
        img_list2.append(img)
        panel = tk.Label(root2, image=img_list2[x])
        panel2_list.append(panel)
    for p in panel2_list:
        p.pack(side="left", fill="none", expand="no")
 
my_original_menu=Menu(originalRoot)
originalRoot.config(menu=my_original_menu)
my_original_menu.add_command(label="Reset Game", command = Reset)
 
 
 
root_p_choice=tk.Toplevel()
root_p_choice.title("Player 1 Search")
p1_choice = tk.Label(root_p_choice, text="Enter the card you guess:", font=fontStyle)
p1_choice.pack()
p1_entry = tk.Entry(root_p_choice)
p1_entry.pack()
p1B = tk.Button(root_p_choice, text ="Find", command = p1find)
p1B.pack()
 
 
root2_p_choice=tk.Toplevel()
root2_p_choice.title("Player 2 Search")
p2_choice = tk.Label(root2_p_choice, text="Enter the card you guess:", font=fontStyle)
p2_choice.pack()
p2_entry = tk.Entry(root2_p_choice)
p2_entry.pack()
p2B = tk.Button(root2_p_choice, text ="Find", command = p2find)
p2B.pack()
 
originalRoot.resizable(False, False)
root.resizable(False, False)
root2.resizable(False, False)
rootKey.resizable(False, False) 
 
originalRoot.mainloop()
root.mainloop()
root2.mainloop()
rootKey.mainloop()
