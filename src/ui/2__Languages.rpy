# Acier < Plomb < Carrare < Martre < Cormier
# .add("DejaVuSans.ttf", 0x0400, 0x052F) is for cyrilic
define -99 config.font_name_map["font_cormier"] = FontGroup().add("AdobeHeitiStd-Regular.otf", 0x0000, 0xffff)
define -99 config.font_name_map["font_martre"] = FontGroup().add("AdobeHeitiStd-Regular.otf", 0x0000, 0xffff)
define -99 config.font_name_map["font_carrare"] = FontGroup().add("AdobeHeitiStd-Regular.otf", 0x0000, 0xffff)
define -99 config.font_name_map["font_plomb"] = FontGroup().add("AdobeHeitiStd-Regular.otf", 0x0000, 0xffff)
    
# define config.default_language = 'japanese'
define config.default_language = None

translate None python:
    set_latin_fonts()
    reload_renpy(resetLogs=False)
translate french python:
    set_latin_fonts()
    reload_renpy(resetLogs=False)

translate russian python:
    config.font_name_map["font_cormier"] = FontGroup().add("Venus+Cormier.otf", 0x0000, 0x0369).add("Roboto-Black.ttf", 0x0000, 0x04FF).add("AdobeHeitiStd-Regular.otf", 0x0000, 0xffff)
    config.font_name_map["font_martre"] = FontGroup().add("Venus+Martre.otf", 0x0000, 0x0369).add("Roboto-Bold.ttf", 0x0000, 0x04FF).add("AdobeHeitiStd-Regular.otf", 0x0000, 0xffff)
    config.font_name_map["font_carrare"] = FontGroup().add("Venus+Acier.otf", 0x002A,0x002A).add("Venus+Carrare.otf", 0x0000, 0x0369).add("Roboto-Medium.ttf", 0x0000, 0x04FF).add("AdobeHeitiStd-Regular.otf", 0x0000, 0xffff)
    config.font_name_map["font_plomb"] = FontGroup().add("Roboto-Regular.ttf", 0x0000, 0x04FF).add("AdobeHeitiStd-Regular.otf", 0x0000, 0xffff)
    gui.name_text_font = "DejaVuSans.ttf"
    set_interligne(-20)
    reload_renpy(resetLogs=False)
    
translate russian style style_card_effect:
    line_spacing -10

translate chinese python:
    config.font_name_map["font_cormier"] = FontGroup().add("Venus+Cormier.otf", 0x0000, 0x0369).add("Source Han Sans CN Heavy.otf", 0x0000, 0xffff)
    config.font_name_map["font_martre"] = FontGroup().add("Venus+Martre.otf", 0x0000, 0x0369).add("NotoSerifSC-Black.ttf", 0x0000, 0xffff)
    config.font_name_map["font_carrare"] = FontGroup().add("NotoSansSC-Regular.ttf", 0x002A,0x002A).add("Venus+Carrare.otf", 0x0000, 0x0369).add("NotoSansSC-Regular.ttf", 0x0000, 0xffff)
    config.font_name_map["font_plomb"] = FontGroup().add("Noto Sans CJK DemiLight.otf", 0x0000, 0xffff)
    set_interligne(0)
    reload_renpy(resetLogs=False)

translate chinese style style_card_effect:
    line_spacing 0

translate japanese python:
    config.font_name_map["font_cormier"] = FontGroup().add("Venus+Cormier.otf", 0x0000, 0x0369).add("GenJyuuGothic-Heavy.ttf", 0x0000, 0xffff)
    config.font_name_map["font_martre"] = FontGroup().add("Venus+Martre.otf", 0x0000, 0x0369).add("GenJyuuGothic-Bold.ttf", 0x0000, 0xffff)
    config.font_name_map["font_carrare"] = FontGroup().add("GenJyuuGothic-Medium.ttf", 0x0000, 0xffff)
    config.font_name_map["font_plomb"] = FontGroup().add("GenJyuuGothic-Normal.ttf", 0x0000, 0xffff)
    set_interligne(0)
    # style.default.line_leading = -15
    gui.text_size = 45
    style.default.language = "japanese-normal"
    reload_renpy(resetLogs=False)

translate japanese style style_card_effect:
    line_leading 0

init python:
    # note, im using dejavusans for the default cyrilic script (ending at 0x04FF)
    # im using AdobeHeitiStd-Regular for chinese/japanese (from 0x4E00)
    # u+200b missing (zero width char)
    def set_latin_fonts():
        config.font_name_map["font_cormier"] = FontGroup().add("Venus+Cormier.otf", 0x0000, 0x0369).add("DejaVuSans.ttf",0x0000, 0x04FF).add("AdobeHeitiStd-Regular.otf", 0x0000, 0xffff)
        config.font_name_map["font_martre"] = FontGroup().add("Venus+Martre.otf", 0x0000, 0x0369).add("DejaVuSans.ttf", 0x0000, 0x04FF).add("AdobeHeitiStd-Regular.otf", 0x0000, 0xffff)
        config.font_name_map["font_carrare"] = FontGroup().add("Venus+Acier.otf", 0x002A,0x002A).add("Venus+Carrare.otf", 0x0000, 0x0369).add("DejaVuSans.ttf", 0x0000, 0x04FF).add("AdobeHeitiStd-Regular.otf", 0x0000, 0xffff)
        #cararre doesnt have     0x0021 is !    002A is * 
        config.font_name_map["font_plomb"] = FontGroup().add("DejaVuSans.ttf", 0x002A, 0x002A).add("DejaVuSans.ttf", 0x00B2,0x00B2).add("Venus+Plomb.otf", 0x0000, 0x0369).add("DejaVuSans.ttf", 0x0000, 0x04FF).add("AdobeHeitiStd-Regular.otf", 0x0000, 0xffff)
        gui.name_text_font = config.font_name_map["font_martre"]
        # gui.interface_text_font = config.font_name_map["font_cormier"]
        set_interligne(0)

    def set_interligne(x):
        style.default.line_spacing = x
        style.default.line_leading = 0
        


