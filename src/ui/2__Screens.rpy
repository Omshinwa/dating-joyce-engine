screen screen_tutorial(disp, properties={}):
    add disp:
        properties properties

screen screen_deck_stack(screenToHide="screen_show_deck"):
    imagebutton:
        xalign 1.0
        idle "ui/exploring-deck_stack.webp"
        hover Transform("ui/exploring-deck_stack.webp", matrixcolor=TintMatrix("#ccccff"))
        action Show("screen_show_deck", dissolve, sorted(deck.list), var_label_callback=None, screen_xsize=1920, background="#0005", background2="#0000", screenToHide=screenToHide, saveZoom="g.card_per_line_deck")
        focus_mask True

    fixed:
        xpos 1780
        ypos 80
        xsize 30
        text str(len(deck.list)) size 60 xalign 0.5 style "outline_text"

screen screen_show_deck(what=deck.list, var_label_callback=None, instruction="", background="#000a", sortOnExit=True, screenToHide="screen_show_deck", screen_xsize=1920, screen_xalign=0.5, pad=None, label2="", label2color=color.blue, background2="#0005", saveZoom=True):

    sensitive game.jeu_sensitive # prevent clicking on a lot of cards
    modal game.jeu_sensitive

    default page = 0
    if pad == None:
        if screen_xsize < 1000:
            default padding = int(screen_xsize/12.8)
        else:
            default padding = int(screen_xsize*0.5/12.8)
    else:
        default padding = pad

    default scn_xsize = screen_xsize - padding
    
    if saveZoom:
        if label2 == "DECK":
            default card_per_line = int(g.card_per_line_deck * screen_xsize/1920)
            default card_per_line_target = "g.card_per_line_deck"
        elif label2 == "TREE":
            default card_per_line = g.card_per_line_tree
            default card_per_line_target = "g.card_per_line_tree"
        elif label2 == "TANK":
            default card_per_line = g.card_per_line_tree
            default card_per_line_target = "g.card_per_line_tree"
        else:
            if saveZoom == True:
                default card_per_line = int(g.card_per_line_deck * screen_xsize/1920) #g.card_per_line
                default card_per_line_target = "g.card_per_line_deck" #"g.card_per_line"
            elif type(saveZoom) is int:
                default card_per_line = saveZoom
                $ saveZoom = False
            else:
                default card_per_line = eval(saveZoom)
                default card_per_line_target = saveZoom

    else: # if saveZoom is False
        default card_per_line = max(2,int(screen_xsize/200))

    
    default scale = max(0.7, scn_xsize/1800)

    if instruction!="":
        default screen_ysize = 780
    else:
        default screen_ysize = 850

    
    $ zoom = scn_xsize/(g.card_xsize * card_per_line)
    $ line_per_page = max(1,int(screen_ysize / g.card_ysize / zoom))
    $ offset = card_per_line * line_per_page * page
    $ displayEverything = (page == 0)
    # $ displayEverything = False

    fixed:
        add background
        xsize scn_xsize + padding
        xalign screen_xalign

        viewport:
            xalign 0.5
            if screen_ysize < (g.card_ysize * zoom)*int((len(what)/card_per_line)+0.999):
                mousewheel True
            else:
                mousewheel False
            draggable True
            xsize scn_xsize
            ysize screen_ysize
            ypos 20
            if displayEverything:
                child_size (scn_xsize, (int(g.card_ysize*zoom)+5)*int((len(what))/card_per_line+0.999) )
            else:
                child_size (scn_xsize, (int(g.card_ysize*zoom)+5)*int((card_per_line * line_per_page)/card_per_line+0.999) )
            
            if len(what)>0:
                add background2

            fixed:

                for index, card in enumerate(what):
                    showif offset<=index<offset+(line_per_page*card_per_line) or displayEverything:
                        if displayEverything:
                            $ index2 = index
                        else:
                            $ index2 = index % (line_per_page*card_per_line)
                        fixed at trs_insane_animation(end={"xalign":index2%card_per_line / (card_per_line-1), "ypos":int(index2/card_per_line) * int(333*zoom)}):
                            xsize int(g.card_xsize*zoom)
                            ysize int(g.card_ysize*zoom) # i do -5 because otherwise you cant navigate using arrow keys, my guess is because of the int fucking some scaling
                        
                            fixed:
                                imagebutton:
                                    idle card.img
                                    hover card.img_hover
                                    if var_label_callback == None:
                                        action NullAction()
                                    else:
                                        action [SetVariable("game.jeu_sensitive",False), Call(var_label_callback, index)]
                                    at Transform(zoom=zoom)

        
        text label2:
            size 90
            ypos 940
            xpos 20
            style "style_fake_button"
            color label2color

        hbox:
            ypos 980
            yanchor 0.5
            xalign 0.5
            spacing int(20*scale)
            imagebutton:
                sensitive page>0
                idle Transform("ui/prev.webp", zoom=scale, matrixcolor=IdentityMatrix())
                insensitive Transform("ui/prev.webp", zoom=scale, matrixcolor=SaturationMatrix(0.0)) 
                hover Transform("ui/prev.webp", zoom=scale, matrixcolor=gui.matrix_green_colorize)
                action SetLocalVariable("page", page-1)
            imagebutton:
                idle Transform("ui/cancel.webp", zoom=scale, matrixcolor=IdentityMatrix()) 
                hover Transform("ui/cancel.webp", zoom=scale, matrixcolor=gui.matrix_green_colorize)
                if sortOnExit == True:
                    action [SetLocalVariable("page", 0), Hide(screenToHide), Function(what.sort), SetVariable("game.jeu_sensitive", True), Return()]
                elif sortOnExit == False:
                    action [SetLocalVariable("page", 0), Hide(screenToHide), SetVariable("game.jeu_sensitive", True), Return()]
                else:
                    action sortOnExit
            imagebutton:
                sensitive page+1 < len(what)/(card_per_line * line_per_page)
                insensitive Transform("ui/next.webp", zoom=scale, matrixcolor=SaturationMatrix(0.0))
                hover Transform("ui/next.webp", zoom=scale, matrixcolor=gui.matrix_green_colorize)
                action SetLocalVariable("page", page+1)
                idle Transform("ui/next.webp", zoom=scale, matrixcolor=IdentityMatrix())
                

        fixed:
            xalign 1.0
            yalign 0.95
            ysize 100
            xsize 300

            if card_per_line >= 3:
                imagebutton:
                    idle "ui/zoom-in.webp"
                    hover Transform("ui/zoom-in.webp", matrixcolor=gui.matrix_green_colorize)
                    if saveZoom:
                        action [SetLocalVariable("card_per_line", card_per_line-1), SetVariable(card_per_line_target, eval(card_per_line_target)-int(1920/screen_xsize))]
                        # using int(1920/screen_xsize) so it's relative to the screen size
                    else:
                        action SetLocalVariable("card_per_line", card_per_line-1)
            imagebutton:
                idle "ui/zoom-out.webp"
                hover Transform("ui/zoom-out.webp", matrixcolor=gui.matrix_green_colorize)
                if saveZoom:
                    action [SetLocalVariable("card_per_line", card_per_line+1), SetVariable(card_per_line_target, eval(card_per_line_target)+int(1920/screen_xsize)), SetLocalVariable("page", 0)]
                else:
                    action [SetLocalVariable("card_per_line", card_per_line+1), SetLocalVariable("page", 0)]
                xpos 100

            text str(page+1):
                size 80
                xpos 220
                ypos 20
                style "style_fake_button"
        
        if type(background) != type(Color()) or Color(background).hsv[1] == 0:
            text instruction xalign 0.5 style "quirky_command" ypos 790 xsize 1600 at trs_animated_text
        else: 
            text instruction xalign 0.5 style "quirky_command" ypos 790 xsize 1600 at trs_animated_text:
                outlines [ (8, "#181d2899", 0, 10), (10, Color(background).replace_opacity(1.0).replace_value(1.0).replace_hsv_saturation(1.0), 0, 0), (5, "#000000", 0, 0) ]
        transclude

screen screen_fullscreen(disp):
    # modal True
    button:
        xsize 1.0
        ysize 1.0
        action [Hide("screen_fullscreen", dissolve), Hide("screen_home_phone")]
    add "#000a"
    add disp:
        xalign 0.5
        yalign 0.5
