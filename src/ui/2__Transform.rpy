# Transforms — the animation vocabulary the rest of the game is written in.
#
# Ren'Py transforms are reusable ATL blocks, so this file is where every repeated motion
# lives exactly once: idle breathing on the sprite, the sitting/standing anchor pairs that
# keep the character's head at the same screen position whichever base is showing, the
# background blur with an alpha-masked focal cutout, and the card motion set (played from
# hand, floating in a picker, flying between piles).
#
# Two things worth pointing out:
#
# `trs_bg_blur` composites rather than filters — it draws the sharp child, then draws a
# blurred copy through a soft-edged alpha mask on top, which is what keeps the centre of
# the frame readable while the edges fall away. The mask is a parameter, so the same
# transform does hard and soft vignettes.
#
# The anchor arithmetic in `trs_sitting` / `trs_standing` / `trs_shock` is the awkward part
# of layered sprites: the composite's bounding box changes with the pose, so a naive
# `align` makes the character jump when the base swaps. Anchoring to a fixed pixel offset
# inside the sprite instead pins the same anatomical point regardless of which layers are
# resolved. `get_joyce_zoom` reads the live image bounds to tell the two bases apart.


#        ::::::::::: ::::::::  :::   :::  ::::::::  :::::::::: 
#            :+:    :+:    :+: :+:   :+: :+:    :+: :+:        
#            +:+    +:+    +:+  +:+ +:+  +:+        +:+        
#            +#+    +#+    +:+   +#++:   +#+        +#++:++#   
#            +#+    +#+    +#+    +#+    +#+        +#+        
#        #+# #+#    #+#    #+#    #+#    #+#    #+# #+#        
#         #####      ########     ###     ########  ########## 


transform trs_fastbreath:
    yoffset 0 zoom 1.0
    linear 0.45 zoom 1.005
    linear 0.45 zoom 1.00
    repeat

transform trs_slowbreath: # applied to a layer
    align (0.5,0.5)
    subpixel True
    linear 0.8 zoom 1.003
    linear 0.8 zoom 1.00
    repeat

# transform trs_slowbreath:
#     subpixel True
#     block:
#         yoffset 0 yzoom 1.0
#         ease 3 yzoom 1.005 xzoom 1.005
#         ease 3 yzoom 1.0 xzoom 1.0
#         repeat

transform trs_depied:
    zoom 0.9 
    # anchor (int(550*0.9), int(625*0.9))
    anchor (495, 562)
    xpos 960
    ypos 517

transform trs_anim_depied(xpos, ypos):
    ypos int(ypos*0.9)-15
    xpos int((xpos-960)*0.9+960) # idk why 1000
    anchor (0.5,0.5)
    zoom 0.9

transform trs_anim_sitting(xpos, ypos):
    xpos xpos
    ypos ypos
    anchor (0.5,0.5)
    zoom 1.0

# question, why cant i define everything with yanchor 0.0?
# trying with anchor 0.0 ...
transform trs_standing: #thats just trs_sitting but when they get up
    anchor (550, 625)
    ypos 455
    xpos 960
    zoom 1.0
    
    # ypos -170
    # zoom 1.0
    # xpos 405 #xalign 0.5 #

transform trs_sitting:
    anchor (550, 625)
    xpos 960
    ypos 595
    zoom 1.0

transform trs_joyce_kiss_sitting:
    zoom 1.5 align (0.5, 0.25)

transform trs_joyce_kiss_depied:
    zoom 1.5 xpos int(945/1.5) ypos 0.338


    # ypos -30
    # yanchor 0.0
    # xanchor 0.0
    # xpos 405
    # zoom 1.0

transform trs_lighting_bbt:
    # matrixcolor IdentityMatrix()
    matrixcolor ColorizeMatrix(Color(hsv=(0,0,-0.1)),Color(rgb=(1.0, 1.03, 1.01))) #BrightnessMatrix(-0.15)

transform trs_bg_blur(strength=4,mask="hard", child=None, invert=False): #mask can be 'hard', 'soft' or 'none'
    contains:
        child
    contains:
        AlphaMask(child,"bg_mask_"+mask, invert=invert)
        blur strength

init python:
    def get_joyce_zoom(i):
        if renpy.get_image_bounds("joyce")[1] == -45:
            return 0.9
        else:
            return 1.0

transform trs_shock(offset, image_bound):
    anchor (550*offset/image_bound[2], 625*offset/image_bound[3])
    # anchor (550*offset/1166.8, 625*offset/1173.2)
    zoom offset
    linear 0.1 zoom offset-0.04
    linear 0.1 zoom offset
    anchor (int(550*offset), int(625*offset))

transform shaking(offset=1.0):    
    yoffset 0 zoom offset
    linear 0.05 zoom offset + 0.01
    repeat
#        ::::::::   ::::::::  :::::::::  :::::::::: :::::::::: ::::    ::: 
#       :+:    :+: :+:    :+: :+:    :+: :+:        :+:        :+:+:   :+: 
#       +:+        +:+        +:+    +:+ +:+        +:+        :+:+:+  +:+ 
#       +#++:++#++ +#+        +#++:++#:  +#++:++#   +#++:++#   +#+ +:+ +#+ 
#              +#+ +#+        +#+    +#+ +#+        +#+        +#+  +#+#+# 
#       #+#    #+# #+#    #+# #+#    #+# #+#        #+#        #+#   #+#+# 
#        ########   ########  ###    ### ########## ########## ###    #### 


transform trs_transition_dissolve:
    on hide:
        linear .25 alpha 0.0
    on show:
        linear .25 alpha 1.0

transform trs_transition_meter_fill_up(croppedSize):
    subpixel True
    corner1 (0, 0)
    linear 0.5 corner2 (croppedSize, 120) 

transform trsfm_cards_go_down:
    ease 0.2 yoffset 0

transform trsfm_cards_go_up:
    ease 0.2 yoffset -156



transform trans_card_played(xfrom=0.5, yfrom=1080, xto=0.5, yto=450): #when card is played from hand
    xanchor 0.5 yanchor 0.5 xpos xfrom ypos yfrom
    ease 0.4 xpos xto ypos yto

transform trans_show_card_2(displayable, offset=0): #floating up and down card
    displayable
    xanchor 0.5 yanchor 0.5 xpos 800 ypos 550
    block:
        ease 1.0 xpos 300 ypos 500
        ease 1.0 xpos 300 ypos 550
        repeat

transform trans_show_card_1(displayable, offset=0): #floating up and down card, card from deck
    displayable
    xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 550
    block:
        ease 1.0 xpos 1600 ypos 550
        ease 1.0 xpos 1600 ypos 500
        repeat

transform trans_anim_move_card(xfrom, yfrom, xto, yto, pauseTime=0, speed=1):
    xanchor 0.5 yanchor 0.5 xpos xfrom ypos yfrom
    ease 0.4*speed zoom 1.5 xpos 960 ypos 350
    pause pauseTime
    ease 0.4*speed zoom 0.2 xpos xto ypos yto alpha 0.0

transform trs_animated_text:
    zoom 1.2
    yoffset -50
    alpha 0.0
    ease 0.3 yoffset 0 zoom 1.0 alpha 1.0

transform trs_insane_animation(end):
    easein 0.5 xalign end["xalign"] ypos end["ypos"]
    # on appear:
    #     ease 1.0 xalign end["xalign"] ypos end["ypos"]
    # ease 1.0 xalign end["xalign"] ypos end["ypos"] #xsize end["xsize"] ysize end["ysize"]
    # xalign end["xalign"] ypos end["ypos"]
    # on hide:
    #     xalign 0.0 ypos 0.0



#        ::::    ::::  ::::::::::: ::::::::   ::::::::  
#        +:+:+: :+:+:+     :+:    :+:    :+: :+:    :+: 
#        +:+ +:+:+ +:+     +:+    +:+        +:+        
#        +#+  +:+  +#+     +#+    +#++:++#++ +#+        
#        +#+       +#+     +#+           +#+ +#+        
#        #+#       #+#     #+#    #+#    #+# #+#    #+# 
#        ###       ### ########### ########   ########  


transform trs_phone:
    on show:
        ypos -1000 xalign 0.9
        ease 0.5 ypos 100
    on hide:
        ypos 100 xalign 0.9
        ease 0.5 ypos -1000

transform throw_away_home(a, b, c):
    zoom 4.0 xalign 0.5 yalign 0.5 rotate 0
    ease 1.0 zoom 0.5 rotate a xalign b yalign c

transform trans_flush_card:
    parallel:
        rotate 0
        pause 0.8
        ease 2.0 rotate 360
    parallel:
        zoom 4.0 xpos 0.5 ypos 0.5 xanchor 0.5 yanchor 0.5
        ease 1.0 zoom 1.0



transform image_qui_defile:
    ypos 0
    linear 30 ypos -3570 
    repeat

transform give_cards_to_rat:
    zoom 0.7 xpos 1820 ypos 120 xanchor 0.5 yanchor 0.5
    easein 0.5 xpos 700 ypos 800
    function renpy.curry(play_sound)(filename="card/draw.mp3") #hacky
    ease 0.1 xpos 680 ypos 820
    alpha 0.0

