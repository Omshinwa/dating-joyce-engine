# Event gating.
#
# Most of what the player does during a date is a repeatable action — chat, ask a
# question, flirt, make eye contact. Each one should produce dialogue that changes as the
# story advances rather than repeating, and each one has a different idea of how long
# "already seen this" should last.
#
# `done_flag` is the whole mechanism: a dict of sets, keyed by reset lifetime. A flag put
# in `oncePerDay` survives until the next morning; one in `oncePerAct` survives until the
# story advances an act; `onceEveryDate` clears at the start of every date. Nothing has to
# know when it will be cleared — the reset happens in one place per lifetime, and any
# script line can gate itself with `if if_not_done("some_flag")`.
#
# `label_reaction_common` is the shared prologue every reactive event calls into. It does
# the two things that would otherwise be copy-pasted 400 times: refuse to fire twice in
# one turn, and refuse to fire content the player hasn't earned yet. The story-progression
# clamp (`game.progress[0]*2 < value`) is what makes repeating an action yield new
# dialogue as the game advances instead of exhausting the pool immediately.
#
# `renpy.pop_call()` is doing real work here. These labels are `call`ed from inside card
# effects, so returning normally would resume the caller mid-effect. Popping the call
# stack first makes the `return` unwind two frames instead of one, which is how a gate
# aborts the whole event rather than just itself.
#
# `label_common_date_card_effect` is the dispatch: a card looks for a scene-specific label
# first (`label_bubbleTea_chat`), then a generic one (`label_reaction_chat`). Writing new
# content for an existing card in a new scene means adding a label with the right name —
# no registration, no table.

default done_flag = {"buttons":Set(), "oncePerDay":Set(),"oncePerAct":Set(),"oncePerDate":Set(),"onceEveryDate":Set(),"ask":Set(),"flirt":Set()}

#oncePerAct: reset after every act
#oncePerDate: reset in label_check_isWin (after date.label_name_Win and before call label_newDay)
#onceEveryDate: reset at every label_beginDuel_common


label label_reaction_common(what = None):
    if what in date.playedThisTurn or renpy.get_attributes("joyce")==None:
        $ renpy.pop_call()
        return

    if what == None:
        if hasattr(date.lastPlayed, "name"):
            $ what = date.lastPlayed.name
    
    if what not in done_flag:
        $ done_flag[what] = 0

    $ value = done_flag[what]
    # if the value exceed the story progression, double return
    if game.act < 2:
        if what == "chat":
            if game.progress[0]*2 < value:
                $ renpy.pop_call()
                return
        elif what == "ask":
            if game.progress[0]*2 < len(done_flag[what]):
                $ renpy.pop_call()
                return
        elif what == "flirt":
            if game.progress[0]*2 < len(done_flag[what]):
                $ renpy.pop_call()
                return
        elif what == "touchy":
            if done_flag[what]>game.progress[0]*2:
                $ renpy.pop_call()
                return
        elif what == "eyecontact":
            if done_flag[what]>game.progress[0]*2:
                $ renpy.pop_call()
                return

    # elif what == "eyecontact" or what == "touchy":
    #     if game.progress[0] < value:
    #         $ renpy.pop_call()
    #         return
    
    call label_cutscene_start from _call_label_cutscene_start_45

    if what == "kiss": # called after label_cutscene because we use i and trs_joyce
        if renpy.get_image_bounds("joyce")[1] == -45:
            $ i = trs_anim_depied
            $ trs_joyce = trs_depied
        else:
            $ i = trs_anim_sitting 
            $ trs_joyce = trs_sitting

    return


label label_common_date_card_effect(cardName):
    if cardName != "peek":
        if game.state == "encounter" and game.act == 2:
            call label_reaction_encounter from _call_label_reaction_encounter
            $ renpy.pop_call()
            return
        elif game.state == "encounter": #DLC
            $ renpy.pop_call()
            return
    if cardName in date.playedThisTurn: 
        return
    if renpy.has_label(date.label_name + "_"+cardName):
        $ renpy.jump(date.label_name + "_"+cardName) 
    else:
        if renpy.has_label("label_reaction_"+cardName):
            $ renpy.jump("label_reaction_"+cardName)
    return

label label_reaction_commonEND(what):
    show screen screen_date_ui with dissolve
    if type(done_flag[what]) == type(0):
        $ done_flag[what] += 1
    return

init python:
    # the logic behind ("flirt", increase_menuID()) if get_menu_options("flirt", reset=True)
    # is complicated
    # increase_menuID() is evaluated on compilation (so it increases 0 to 10)
    # the args are passed to the choice screen
    # if theres 2 args, a condition is triggered that will callback update_menu_options(menuId)
    # if it's clicked.
    #
    # but if get_menu_options("flirt", reset=True) is called on runtime, so we have to reset the
    # menuId variable.

    def increase_menuID(reset = False):
        global menuId
        menuId+=1

        if reset:
            menuId = 0
        return menuId

    # for FLIRT and ASK
    def get_menu_options(what, reset=False):
        global i
        # if reset:
        #     menuId = -1
        if i >= 2: # if we already have 2 speech bubbles
            return False
        i += 1
        return True
        # menuId+=1
        # if menuId in done_flag[what]:
        #     i+=1
        #     return True
        # else:
        #     return False

    def update_menu_options(what, index):
        # change the index of the bubble that contains question INDEX with max +1 
        done_flag[what][done_flag[what].index(index)] = max(done_flag[what]) + 1

        #if a question hasnt been selected for 3 times, it gets removed.
        # if max([x for x in done_flag[what] if x != max(done_flag[what])]) - min(done_flag[what]) > 3:
        #     done_flag[what][done_flag[what].index( min(done_flag[what]) )] = max(done_flag[what]) + 1
        if max(done_flag[what]) - min(done_flag[what]) > 3:
            done_flag[what][done_flag[what].index( min(done_flag[what]) )] = max(done_flag[what]) + 1


init python:

    def if_not_done(flag:str, which=None) -> bool:
        """
        The gate itself. Returns True the first time it sees a flag within the current
        lifetime, False after that, and records the flag on the way out — so a script line
        reads `if if_not_done("joyce_noticed_the_rain"):` with no bookkeeping around it.

        Because it mutates on read, it has to be tested last in a compound condition:
        short-circuiting past it is fine, but testing it before a condition that fails
        would burn the flag on an event that never fired.

        :which: "oncePerAct" "oncePerDate" "onceEveryDate"
        """
        if which == None:
            # Default the lifetime to whatever the current game state implies.
            if game.state == "living":
                which = "oncePerAct"
            else:
                which = "oncePerDate"
        if flag not in done_flag[which]:
            done_flag[which].add(flag)
            return True
        else:
            return False
