init python:

    class Card:
        def __init__(self, hash):

            self.name = hash

            self.illustration = CARD_IMG_DICT[hash]

            self.txt = cardList[hash]["txt"]
            if getattr(g,"difficulty",1) == 0.7 and "txt_easy" in cardList[hash]:
                self.txt = cardList[hash]["txt_easy"]
            
            self.updateArt()

            if "cond" in cardList[hash]:
                self.condition = cardList[hash]["cond"]
            else:
                self.condition = "True"

            if "eff" in cardList[hash]:
                self.eff = cardList[hash]["eff"]
            else:
                self.eff = "renpy.call('label_card_" + hash +"')"

            self.value = 0
            if "value" in cardList[hash] : self.value = cardList[hash]["value"] 


        def __lt__(self,other): #this makes operation with '<' possible, and so sorting cards are by names.
            if self.name in cardList and "sort" in cardList[self.name]:
                i = cardList[self.name]["sort"]
            else:
                i = self.name
            if other.name in cardList and "sort" in cardList[other.name]:
                j = cardList[other.name]["sort"]
            else:
                j = other.name
            return i<j
        
        def __repr__(self):
            return self.name

        def cond(self, index):
            return eval(self.condition.replace( "index" , str(index)))

        @staticmethod
        def get_random_card(customList=None, trueRandom=False):
            if customList == None or len(customList)==0:
                customList = [ key for key in cardList if "value" in cardList[key] ]
                return Card( renpy.random.choice( customList ) )
            else:
                if trueRandom:
                    return Card( random.choice(customList)) 
                else:
                    return Card( renpy.random.choice(customList))

        def updateArt(self):

            if _preferences.language in {"chinese", "japanese"}:

                i = re.sub(r"(\[.*?\]|\{.*?\})", "", renpy.translate_string(self.txt)) # get the length of the translated card effect (ignoring variable names in [bracket] and in {tags})
                if len(i)<15:
                    text_effect = Text(self.txt, style="style_card_effect", size=38) 
                else:
                    text_effect = Text(self.txt, style="style_card_effect", size= (38 - len(i)/2.7), layout="greedy") 
            else:
                if len(self.txt)<32:
                    text_effect = Text(self.txt, style="style_card_effect", size=32) 
                else:
                    text_effect = Text(self.txt, style="style_card_effect", size=35 - int(len(self.txt)/8), layout="greedy") 

            
            textbox = Window(text_effect, style="empty",  xysize=(200, 135), background=Color("#f9f5d4"), padding=(3,2))

            if "color" in cardList[self.name]:
                if cardList[self.name]["color"] == "bad":
                    text_effect.color = "#fff"

            if "color" not in cardList[self.name]:
                card_bg = Transform("cards/card_bg.webp", matrixcolor=TintMatrix("#e1ddd4"))
            else:
                if cardList[self.name]["color"] == "trust":
                    card_bg = Transform("cards/card_bg.webp", matrixcolor=TintMatrix("#93efff"))
                elif cardList[self.name]["color"] == "lust":
                    card_bg = Transform("cards/card_bg.webp", matrixcolor=TintMatrix("#ebef73"))
                elif cardList[self.name]["color"] == "attraction":
                    card_bg = Transform("cards/card_bg.webp", matrixcolor=TintMatrix("#ffa4e4"))
                elif cardList[self.name]["color"] == "joker":
                    card_bg = "cards/card_bg_joker.webp"
                elif cardList[self.name]["color"] == "bad":
                    card_bg = Transform("cards/card_bg.webp", matrixcolor=ColorizeMatrix("#bdc4c9","#131513"))

            self.img = Composite((230, 330), (0, 0), card_bg, (15,15), self.illustration, (15,174), textbox)
            self.img_hover =  Transform(self.img, matrixcolor=ColorizeMatrix("#005d36","#eeffee"))

            del text_effect, card_bg

        # #this is a getter 
        # def update_x_in_hand(self, index, cards_in_hand):
        #     self.x = int((index)* 230 + getCardPadding(cards_in_hand)*index)
         
    class Deck:
        def __init__(self):
            self.hand = []
            self.deck = [] # the deck during a game

            self.list = []
            self.discard_pile = []
        
        def add_to_hand(self, *cards):
            for card in cards:
                renpy.play("card/draw.mp3", channel='drawcard')
                self.hand.append(card)
            if len(deck.hand)>=10:
                grant_with_notification("greedy")

        def draw(self, number, delay=0.2):
            global ydisplace
            ydisplace = 0
            for i in range(0,number):
                if len(self.deck)>0: #si y a une carte dans le deck
                    self.add_to_hand( self.deck.pop(0) )
                    renpy.pause(delay)

        def __str__(self):
            txt = []
            for card in self.hand:
                txt.append(card.name)

            return ", ".join(txt)
        
        # return the highest number of cards in the hand that are the same.
        def hasPair(self):
            highest = 0
            for i in self.hand:
                current = 1
                for j in self.hand:
                    if i != j:
                        if i.name == j.name:
                            current+=1
                if current > highest:
                    highest = current
            return highest

        def shuffle(self):
            renpy.random.shuffle(self.deck)
            renpy.play("card/shuffle.mp3", channel='drawcard')
            renpy.pause(0.5)

        # discard card from hand
        def discard(self, index, delay=0.2):
            renpy.play("card/draw.mp3", channel='drawcard')
            self.discard_pile.append( self.hand.pop(index) )
            renpy.pause(delay)
        
        # remove a card from list
        def remove(self, name):
            for card in deck.list:
                if card.name == name:
                    deck.list.remove(card)
                    return

        def isThere(self, search:str, list="list", removeCard=False): # is there this card in the current list?
            list = getattr(self,list)
            for i, card in enumerate(list):
                if card.name == search:
                    if removeCard:
                        list.pop(i)
                    return True
            return False   

label playCard(card, index, playCardindex=0):
    $ date.lastPlayed = card
    $ commands = card.eff
    $ commands.replace("index", str(index))
    $ commands = commands.split("; ")
    while playCardindex < len(commands):
        $ exec(commands[playCardindex])
        $ playCardindex+=1
    if date.lastPlayed!=None and date.lastPlayed.name not in date.playedThisTurn:
        $ date.playedThisTurn.append(date.lastPlayed.name)
    return

label playCard_reload(card, index, playCardindex=0):
    if "reload" not in date.playedThisTurn:
        $ date.playedThisTurn.append(date.lastPlayed.name)
    $ date.lastPlayed = card
    $ commands = card.eff
    $ commands.replace("index", str(index))
    $ commands = commands.split("; ")
    while playCardindex < len(commands):
        $ exec(commands[playCardindex])
        $ playCardindex+=1
    if date.lastPlayed!=None and date.lastPlayed.name not in date.playedThisTurn:
        $ date.playedThisTurn.append(date.lastPlayed.name)
    return

label playCardfromHand(index):
    if deck.hand[index].cond(index):
        $ game.jeu_sensitive = False
        $ ydisplace = 0

        $ renpy.play("card/activate.mp3", channel='activatecard')
        $ card = deck.hand[index]
        $ deck.discard(index)

        # animation:
        # $ renpy.show('cardPlayed', what=card.img, at_list=[trans_card_played], zorder=2, layer="screens")
        # $ renpy.pause(0.5)
        $ renpy.hide('cardPlayed', layer="screens")

        call playCard(card, index) from _call_playCard
    else:
        $ raise Exception("playCardfromHand cond invalid")
    return
