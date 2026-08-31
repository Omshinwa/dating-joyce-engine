# UPDATE, maxxer: -3 Lust, if it goes into negatives, -10 Lust instead.
# drink: +1 regardless of limite (can go into 4/3)

define cardList = { 
    # calling a method of game or date in a string doesnt work in browser


    "calm": {"txt":_("-3 Lust. Can go into negatives."), "eff":"renpy.call('label_card_calm')", "value":0, "sort":"200", "act":1},
    "maxcalm":{"txt":_("-10 Lust, add one STOP card in your hand."), "eff":"renpy.call('label_card_maxcalm')", "value":1, "sort":"201", "act":1},

    "fibonacci": {"txt": _("-1 Lust, this permanently increases by 1 every time it's played."), "eff":"renpy.call('label_card_fibonacci')", "value":3,"sort":"202", "act":1},
    
    "newday": {"txt":_("IF no card were played this turn: Change your Lust at random."), "eff":"renpy.call('label_card_newday')", "cond":"len(date.playedThisTurn) == 0", "value":2,"sort":"203", "act":1},

    "burial":{"txt":_("Discard a card of your choice. -10 Lust."), "eff":"renpy.call('label_card_burial', index)", "cond":"len(deck.hand)>1", "value":2, "sort":"204", "act":2},

    #, this ends your turn
    "slower": {"txt":_("Go much slower."), "eff":"renpy.call('label_card_slower')", "value":1, "sort":"21", "act":1},
    "slowsteady": {"txt":_("IF this is your leftmost card: \nGo much slower. -10 Lust."), "cond":"index == 0", "value":1, "sort":"22", "act":2}, #\nGo slower,\n-10 Lust.
    "fool": {"txt": _("IF you have 3 cards or less in hand: Go much slower. -10 Lust."), "cond":"len(deck.hand)<=3", "value":1, "sort":"23", "act":2}, # Go slower, -10 Lust.
    "faster": {"txt":_("Move the turn counter."), "eff":"renpy.call('label_card_faster')", "value":1, "sort":"24", "act":2}, #debug maybe go much faster?


    "drink" : {"txt":_("Fully refill your glass."), "eff":"renpy.call('label_card_drink')", "value":2, "sort":"40", "act":1}, #把杯子倒满
    "bottomsup" : {"txt":_("Refill 2/3 of your glass. Change the order of your cards."), "value":1, "sort":"41", "act":2},
    # "bottomsup" : {"txt":_("Add 2/3 to your glass, even if already full. Reverse your hand."), "value":1, "sort":"41", "act":2},

    "recycle": {"txt":_("Discard all the cards on the right of this card, then redraw as many +1."), "eff":"renpy.call('label_card_recycle', index)", "value":0,"sort":"42", "act":1},

    "draw2": {"txt":_("draw 2 cards"), "eff":"renpy.call('label_card_draw2')", "value":4,"sort":"44", "act":4},#
    "devil": {"txt":_("Draw 2 cards.\nDouble your Lust."), "eff":"renpy.call('label_card_devil')", "value":3,"sort":"444", "act":1},
    "pair": {"txt":_("IF you have a pair in your hand: draw 2 cards"), "cond":"deck.hasPair()>1", "eff":"renpy.call('label_card_pair')", "value":3,"sort":"4444", "act":1},
    "triple": {"txt":_("IF you have a triple in your hand: draw 3 cards."), "cond":"deck.hasPair()>2", "value":0,"sort":"4444", "act":3},

    "gamble": {"txt":_("Change all the cards in your hand with random cards."), "value":0,"sort":"50", "act":2},
    
    
    "sisyphus": {"txt":_("Choose a card in the discard pile: Put it back on top of your deck."), "eff":"renpy.call('label_card_sisyphus', index)", "value":3,"sort":"61", "act":1},
    "reload": {"txt":_("The most recent card in the discard pile is played again."), "cond":"len(deck.discard_pile)>0", "eff":"renpy.call('label_card_reload', index)", "value":3, "sort":"63", "act":1},

    # "ouroboros": {"txt":_("When drawn or played, reduce your lust by 5.")},


    "spaceout" : {"txt":_("does nothing"), "value":0, "sort":"640", "act":1}, #_("")
    "universeout" : {"txt":_("Turn any number of cards into Space Out. \nThen -5 Lust for each in hand."), "eff":"renpy.call('label_card_universeout')", "value":1, "sort":"641", "act":2},
    "darkhole" : {"txt":_("Draw every Space Out card from your deck and discard pile."), "eff":"renpy.call('label_card_darkhole')", "value":1, "sort":"642", "act":2},
    # "nova" : {"txt":_("Discard the rest of your hand.\n-5 Lust for each card."), "value":1, "sort":"643", "act":2},
    "nova" : {"txt":_("Send the cards in your hand to the bottom of your deck. -5 Lust for each card."), "value":2, "sort":"643", "act":2},
    #alternatively it could be every space out in deck hand and graveyard
    # Draw all your Space Out cards. Empties your glass.

    "offering" : {"txt":_("-25 Lust. Discard half your deck."),"value":2, "sort":"8", "act":2},
    "stall": {"txt":_("ONCE per date: This turn, you cannot lose."), "value":2,"sort":"81", "act":2},

    "exodia3" : {"txt":_("{b}WORLD{/b}\ninto Stamina.\nthe right\nthis effect."), "eff":"renpy.call('label_card_exodia', index)", "value":0,"rarity":0.5, "sort":"93", "act":2},
    "exodia2" : {"txt":_("{b}OF THE{/b}\ncurrent Lust\n3 pieces in\nactivate"), "eff":"renpy.call('label_card_exodia', index)", "value":0,"rarity":0.5, "sort":"92", "act":2},
    "exodia1" : {"txt":_("{b}ORIGIN{/b}\nConvert your\nYou need all\n order to"), "eff":"renpy.call('label_card_exodia', index)", "value":0, "rarity":"rare", "sort":"91", "act":2},


    "stop": {"txt":_("Can't be played"), "cond":"False", "eff":"pass", "value":-3,"sort":"yyy", "color":"bad", "act":2},
    "tired": {"txt":_("You're tired.\nWhen you have 4 in hand: you lose."), "cond":"False", "eff":"pass", "sort":"yyy", "color":"bad"},

    "peek": {"txt":_("you peek...\n+[difficulty(5)] Lust"), "eff":"renpy.call('label_card_peek')", "color":"lust"}, #"value":-1
    "peek2": {"txt":_("you peek...\n+[difficulty(10)] Lust"), "eff":"renpy.call('label_card_peek2')", "value":-1, "color":"lust", "act":2,}, 
    "peekred": {"txt":_("you peek...\n+[difficulty(15)] Lust"), "eff":"renpy.call('label_card_peekred')", "color":"lust"}, #"value":-2,
    "peekblue": {"txt":_("you peek...\n+[difficulty(15)] Lust"), "eff":"renpy.call('label_card_peekblue')", "color":"lust"}, #"value":-2,
    "peek4": {"txt":_("you peek...\n+[difficulty(20)] Lust"), "eff":"renpy.call('label_card_peek4')", "value":-2, "color":"lust", "act":2},
    "peek5": {"txt":_("you peek...\n+30 Lust"), "eff":"renpy.call('label_card_peek5')", "value":-3, "color":"lust", "act":2},


    "eyecontact": {"txt":_("+1 attraction"), "eff":"renpy.call('label_card_eyecontact')", "sort":"010", "color":"attraction"},
    "flirt": {"txt":_("+2 attraction"), "eff":"renpy.call('label_card_flirt')", "sort":"011", "color":"attraction"},
    "touchy" : {"txt":_("For the rest of this turn: double Attraction changes."), "sort":"012", "color":"attraction"}, #

    "kiss" : {"txt":_("+3 trust,\n+3 attraction,\nEnd your turn."), "sort":"020", "color":"joker"},

    "chat": {"txt":_("+1 trust"), "sort":"000", "color":"trust"}, #+1 trust
    "ask": {"txt":_("+2 trust"), "eff":"renpy.call('label_card_ask')", "sort":"001", "color":"trust"},
    "listen": {"txt":_("For the rest of this turn: double Trust changes."), "sort":"002", "color":"trust"},

    "awakening": {"txt":_("For the rest of this turn: double Lust changes."), "value":4,"sort":"30", "act":2},

    "undress" : {"txt":_("Take off clothes.\nDraw 1 card."), "value":1 , "act":3, "sort":"ww",},

    "powder" : {"txt":_("Mysterious powder..."), "sort":"zzz"},
    "sunscreen" : {"txt":_("+[difficulty(30)] Lust. Spread some sunscreen on Joyce. Goes back into the deck."), "sort":"zz",},

    ####            POKER MENU STUFF
    "newgame" : {"txt":_("Start a New Game"), "eff":"renpy.jump('label_start')","sort":"___", },

    "load" : {"txt":_("Load a Save file"),"sort":"___", },
    "prefs" : {"txt":_("Open Preferences Menu"), "sort":"___", },
    "lang" : {"txt":_("Change Language"), "sort":"___", },
    "achievement" : {"txt":_("Check Achievements")},
    "fullscreen": {"txt":_("Switch between Windowed and Fullscreen")},
    "contact": {"txt":_("Contact the developper")},

    "memory" : {"txt":_("Check Memories"), "sort":"1",},
    "unlockreplay":{"txt":_("Unlock Replay Mode in Memories"), "sort":"2",},
    "dressing":{"txt":_("Enter the dressing room"), "sort":"3",},
    "arcade":{"txt":_("Play the arcade mode"), "sort":"4",},
    "debug":{"txt":_("Debug mode"), "sort":"5",},
        }

default persistent.joyce_casino = "joyce outfitcasino hair_braids smile"

label label_anti_spoil(which):
    if not achievement.has('progress'):
        if which == 'arcade':
            "It seems like you haven't finished the game. This WILL spoil you."
        else:
            "It seems like you haven't finished the game. It might spoil you."
        menu:
            "Continue anyway?"
            "Yes":
                return
            "Go back":
                $ renpy.pop_call()
                return
    return
    

label label_card_dressing:
    call label_anti_spoil('dressing')

    hide screen screen_card_hand onlayer master
    hide screen screen_dating_deck_stack onlayer master
    with dissolve
    show fg:
        yoffset 0
        ease 1 yoffset 500
        ease 1 alpha 0
    show bg:
        alpha 1
        ease 1 alpha 0
    with dissolve
    hide joyce
    hide joyce_hand_poker
    show screen screen_dressing
    with dissolve
    call label_gameLoop
    jump start

label label_card_contact:
    hide screen screen_card_hand onlayer master with dissolve
    j "Sure, through what platform?"
    menu:
        "Itch.io":
            $ renpy.run(OpenURL("https://omshinwa18.itch.io/dating-joyce"))
        "Steam":
            $ renpy.run(OpenURL("https://store.steampowered.com/app/2832580/Dating_Joyce_a_Deckbuilding_Game/?utm_source=datingjoyce"))
        "Twitter":
            $ renpy.run(OpenURL("https://x.com/Omshinwa18"))
        "Discord":
            $ renpy.run(OpenURL("https://discord.gg/cwdMt3zsmT"))
        "Donate with Paypal":
            $ renpy.run(OpenURL("https://www.paypal.com/donate/?hosted_button_id=XLETNGHQGUEAU"))
            
    jump start

label label_card_load:
    $ renpy.run(ShowMenu('load'))
    jump start

label label_card_unlockreplay:
    "Replay Mode unlocked!"
    $ persistent.unlockreplay = True
    return

label label_card_prefs:
    $ renpy.run(ShowMenu('preferences'))
    return

label label_card_debug:
    call screen screen_debug_menu
    return

init python:
    CARD_IMG_DICT = {}
    for card in cardList:
        CARD_IMG_DICT[card] = Image("cards/"+card+".webp")

label label_card_fullscreen:
    if game.debug_mode:
        call screen screen_debug_menu
        return
    if preferences.fullscreen:
        $ renpy.run(Preference("display", "window"))
    else:
        $ renpy.run(Preference("display", "fullscreen"))
    return

label label_card_lang:
    menu:
        "English":
            $ renpy.change_language(None, True)
        "Français":
            $ renpy.change_language("french", True)
        "中文":
            $ renpy.change_language("chinese", True)
        "日本語":
            $ renpy.change_language("japanese", True)
        # "русский":
        #     $ renpy.change_language("russian", True)
        # "українська":
        #     $ renpy.change_language("ukrainian", True)
    $ deck.hand.append(Card("lang"))
    return

label label_card_achievement:
    if g.demo:
        j "Sorry, this feature is unavailable in the demo." id label_card_achievement_219dbf92
        return

    if persistent.achievement_tutorial:
        show screen screen_achievement with dissolve
        show expression "#0006" as black onlayer screens with dissolve
        play sound "rpg/tutorial.wav"
        "This is the Achievement Screen."
        "Every time you complete [casino_achievement_req] achievement, you draw 1 more card in the casino!"
        window auto hide
        show expression "#000" as black onlayer screens
        hide screen screen_achievement
        with dissolve
        $ persistent.achievement_tutorial = False
    $ achievement.sync()
    call screen screen_achievement with dissolve
    return

label label_card_memory:
    scene
    call screen screen_gallery with dissolve
    return
