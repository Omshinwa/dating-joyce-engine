# Steamworks achievements, and the reward loop built on top of them.
#
# The achievement table is data, like the card table: an id mapped to a translatable name
# and description. The id is also the art filename (`achievements/<id>.jpg` and
# `<id>_locked.jpg`), so adding an achievement is one dict entry plus two images — the
# grid screen below needs no edit, and neither does the Steam sync.
#
# `grant_with_notification` wraps `achievement.grant` with the three things that always
# have to happen alongside it: play the sound, show the toast with the *translated* name,
# and sync to Steam. It's installed onto Ren'Py's `achievement` object at init, so all the
# call sites reach it through the same namespace as the stock API and there's no way to
# grant an achievement while forgetting to notify.
#
# The `if g.demo: return` guard matters more than it looks. The demo is built from this
# same tree via build classifiers, and it ships without the Steam appid — granting there
# would either no-op noisily or fire a toast for progress the player can't actually keep.
#
# The reward loop is the reason achievements aren't just cosmetic here: every Nth one
# unlocks an extra starting card. Because the main menu is itself a hand of cards, that
# reward is delivered by literally dealing the player one more card on the title screen,
# and `persistent.joyceGivesOneMore` defers it to the next visit so the character can hand
# it over in dialogue rather than it appearing silently.

define config.steam_appid = 2832580

# How many achievements between each extra-card reward.
define casino_achievement_req = 1

default persistent.joyceGivesOneMore = False # when you get 3 achievements you draw one more.

init 2 python:
    basic_achievements = {
        "progress2":(_("Progress!"), _("Finish the second act."),),
        "progress":(_("Together Forever"), _("Finish the game."),) ,
        "exodia":(_("Exodia"), _("Play Origin of the World.")),
        "suspicious":(_("Suspicious"), _("Avoid getting drugged."),),
        "greedy":(_("Greedy"), _("Have 10 cards in hand."), ),
        "explosive":(_("Explosive"), _("Change one of your stats by 50 or more in one go."), ),
        "speeddating":(_("Speed Dating"), _("Finish the first act in 40 days or less in normal difficulty."), ),
        "stamina":(_("Stamina"), _("Clear every date in the final act."), ),
        "tommygun":(_("Tommy Gun"), _("Play Reload that triggers a Reload that triggers a Reload."), ),
        "bigbrain":(_("Big Brain"), _("Solve all the Shop's puzzles (then go see the owner)."))

        # Plant lover: have like 10 plant cards in your deck.

        # (_("Space Conquest"), _("Make a Space themed deck")),
        # (_("Garbage Boy"), _("Have your empty bin be full."))
    }

    def grant_with_notification(achievment_id):
        if g.demo:
            return
        
        if not achievement.has(achievment_id):
            renpy.sound.play("ui/achievement_kettei-01.wav")
            renpy.notify(__("Got the achievement:") + " " + renpy.translate_string(basic_achievements[achievment_id][0]))
            achievement.grant(achievment_id)
            achievement.sync()
            renpy.pause(0.3)

            
            nb_of_achievements = 0
            for key, value in basic_achievements.items():
                if achievement.has(key):
                    nb_of_achievements += 1
            
            if nb_of_achievements % casino_achievement_req == 0:
                persistent.joyceGivesOneMore = True

    achievement.grant_with_notification = grant_with_notification

screen screen_achievement():

    key [ 'mouseup_3'] action MainMenu(confirm=False,save=False)

    tag menu
    default delete_everything = 0
    modal True
    
    $ nb_of_achievements = 0
    for key, value in basic_achievements.items():
            if achievement.has(key):
                $ nb_of_achievements += 1

    if nb_of_achievements >= len(basic_achievements): 
        add color.pink
    else:
        add "#222"
    vpgrid rows 6:
        xalign 0.5
        yalign 0.1
        xsize 1700
        xfill True
        for key, value in basic_achievements.items():
            hbox:
                if achievement.has(key):
                    $ nb_of_achievements += 1
                    add "achievements/" + key + ".jpg" xsize 128 ysize 128
                else:
                    add "achievements/" + key + "_locked.jpg" xsize 128 ysize 128

                if achievement.has(key):
                    text "{color=#ff6}" + renpy.translate_string(value[0]) + "{/color}\n{size=-10}{color=#fff}" + renpy.translate_string(value[1]) + "{/color}"
                else:
                    text "{color=#777}???\n{size=-10}" + renpy.translate_string(value[1]) + "{/color}"
    
    textbutton _("Return"):
        style "style_text_button"
        action MainMenu(confirm=False,save=False)
        yalign 1.0
        xalign 0.0

    if delete_everything == 0:
        textbutton _("Forget Everything(!)"):
            text_size 40
            xalign 0.5
            yalign 1.0
            style "style_text_button"
            action SetScreenVariable("delete_everything", 1)
    elif delete_everything == 1:
        textbutton _("Are you sure?"):
            text_size 40
            xalign 0.5
            yalign 1.0
            style "style_text_button"
            action [Function(persistent._clear), Function(achievement.clear_all), SetScreenVariable("delete_everything", 2)]
    else:
        textbutton _("Done!"):
            text_size 40
            xalign 0.5
            yalign 1.0
            style "style_text_button"

