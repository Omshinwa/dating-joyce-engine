define config.modal_blocks_pause = False # setting modal on screen made pausing with time not work
# define config.say_attribute_transition_layer = "char" # doing that when you show joyce in the prison, by default it's on char and its color matrix is already set
define config.say_attribute_transition_layer = "master"
# define config.tag_layer = { "joyce":"char", "bg":"bg" }

define config.say_attribute_transition = Dissolve(.2)


init python:
    renpy.add_layer("bg", below="master", menu_clear=False)
    renpy.add_layer("char", below="master", menu_clear=False)
    def clear_layers(layer):
        if layer == "master":
            renpy.scene("bg")
            renpy.scene("char")
            renpy.show_layer_at([], layer='bg', reset=True, camera=True)
            renpy.show_layer_at([], layer='char', reset=True, camera=True)
        # maybe is needed?
        # renpy.show_layer_at(at_list, layer='master', reset=True, camera=False)
        #

# Transitions used to show and hide the dialogue window
define config.scene_callbacks = [clear_layers]
define config.window_auto_hide = [ "scene", "call screen", "menu", "say-centered", "say-bubble", "pause", 'show screen', 'hide screen', 'hide', 'play', 'call', 'show'] #new

define config.window_show_transition = { "screens" : Dissolve(.2) }
define config.window_hide_transition = { "screens" : Dissolve(.2) }


define gui.matrix_green_colorize = ColorizeMatrix("#009f5d","#dfd")

style default:
    properties gui.text_properties()
    language gui.language
    font config.font_name_map["font_carrare"]

style style_fake_button:
    font config.font_name_map["font_cormier"]
    size gui.interface_text_size
    color gui.selected_color

style outline_text:
    color "#000000"
    outlines [ (5, "#ffffff", 0, 2) ]
    font config.font_name_map["font_cormier"]

style outline_dyslexic:
    color "#fff"
    outlines [ (4, "#050505", 0, 2) ]
    font config.font_name_map["font_cormier"]

style style_small_numbers:
    color "#fff"
    outlines [ (4, "#050505", 0, 2) ]
    font config.font_name_map["font_carrare"]

style style_card_effect:
    xalign 0.5
    yalign 0.4
    adjust_spacing True
    textalign 0.5
    font config.font_name_map["font_plomb"]

style quirky_command:
    color "#ffffff"
    # outlines [ (8, "#181d2899", 0, absolute(10)), (absolute(10), "#25d7ff", 0, 0), (5, "#000000", 0, 0) ]
    outlines [ (8, "#181d2899", 0, 10), (10, gui.hover_color, 0, 0), (5, "#000000", 0, 0) ]
    font config.font_name_map["font_carrare"]
    size 100
    adjust_spacing True

style style_text_button:
    # color "#fff"
    xalign 0.5
    yalign 0.5

style style_text_button_text: #this will affect the text of text_buttons
    hover_color color.sky
    selected_color color.green
    size 80
    color "#fff" 

# define wipeup = ImageDissolve("gui/wipeup.webp", 0.5, reverse=True)
init python:
    def wipeup(time=0.5, drink=False):
        if drink:
            return ImageDissolve("gui/wipedrink.webp", time, reverse=True)
        return ImageDissolve("gui/wipeup.webp", time, reverse=True)

define wipedown = ImageDissolve("gui/wipeup.webp", 0.7)
define pointillisme = ImageDissolve("gui/mask_pointillisme.webp", 0.5)

init python:
    # def tintImg(img, color):
    #     return Transform(img, matrixcolor=TintMatrix(color))

    def colorizeImg(img, color):
        return Transform(img, matrixcolor=ColorizeMatrix(color[0],color[1]))

    def bwImg(img, value=0.0):
        return Transform(img, matrixcolor=SaturationMatrix(value))

transform tintImg(child, color): #DOES NOT WORK IF THE IMAGE ISNT FULL SCREEN, use this on hover when idle uses showInteractible(), if not, just use Transform()
    # contains:
    child
    matrixcolor TintMatrix(color)

transform showInteractible(child, pos=(0.5,0.5)):
    matrixcolor IdentityMatrix()
    contains:
        child
    contains:
        "trs_click_me"
        anchor (0.5, 0.5)
        pos pos
        alpha (0.0 if child in done_flag["buttons"] else 1.0)

image trs_click_me:
    "images/ui/click-me/click-me_00.webp" with Dissolve(0.5)
    0.5
    "images/ui/click-me/click-me_05.webp" with Dissolve(0.5)
    0.5
    "images/ui/click-me/click-me_11.webp" with Dissolve(0.5)
    0.5
    "images/ui/click-me/click-me_17.webp" with Dissolve(0.5)
    0.5
    "images/ui/click-me/click-me_23.webp" with Dissolve(0.5)
    0.5
    "images/ui/click-me/click-me_29.webp" with Dissolve(0.5)
    0.5
    repeat

style _default: # this is the font used for accessibility screen and console and debug menu
    font "font_plomb"