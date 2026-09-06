# The character sprite, declared as a layered image.
#
# Every visible state of the character is a set of attributes drawn from 12 groups
# (outfit, hair, arm, base, accessories, face, skin, eyes, brow, mouth, ...), and the
# groups are ordered here to double as the paint order: back hair, back arm, base body,
# front arm, front hair, face.
#
# The interesting part is the conditional rules. An arm pose is not one image — it is a
# different image per outfit, per hair variant, and sometimes per sitting/standing base.
# Rather than drawing every combination, each `attribute` line states which image to use
# and under what conditions:
#
#   attribute armhip                             "joyce_arm_right_back"
#   attribute armhip if_any "outfitsport"        "joyce_arm_right_sport"
#   attribute armhip if_all "outfit5"            "joyce_arm_armhip_5"
#
# The renderer walks these top to bottom and keeps whichever lines match the requested
# tag set, so `show joyce outfitsport armhip smile` resolves to a legal composite without
# any of the callers knowing which art files exist. `if_not` is used the other way, to
# suppress a layer that a given outfit already includes.
#
# ~100 attributes and ~290 conditional rules cover a combination space far larger than the
# 1,200 source images backing it. The `variant "back"` / `variant "front"` groups are the
# same logical group appearing twice in the paint order, once behind the body and once in
# front of it, which is how arms wrap around the character.

layeredimage joyce:

    group outfits: #make sure you cant have two different outfit at the same time
        attribute outfit1 null
        attribute outfit2 null
        attribute outfitred null
        attribute outfitblue null
        attribute outfit5 null
        attribute night null
        attribute night2 null
        attribute night3 null
        attribute night4 null
        attribute night5 null
        attribute night6 null
        attribute night7 null
        attribute night8 null
        attribute night9 null
        attribute sitted-outfit3 null
        attribute sitted-swimsuit null
        attribute sitted-swimsuit2 null
        attribute standup-outfit3 null
        attribute swimsuit null

        attribute outfit3 null
        attribute outfit4 null
        attribute outfitcasino null
        attribute outfitsport null
        attribute outfitsport2 null
        attribute outfitsport3 null

        attribute outfit6 null

        attribute wet null

    group hair variant "back":
        attribute hair default: 
            "joyce_hair_back" 
        attribute wet: 
            "joyce_hair_back" 
        attribute wethair "joyce_hair_back" 
        attribute green_hair:
            "joyce_hair_back_green" 
        attribute hair_braids
        attribute outfitsport if_not ["hair", "hair_braids", "wethair", "green_hair"]
        attribute outfitsport2 if_not ["hair", "hair_braids", "wethair", "green_hair"]:
            "joyce_hair_back_outfitsport"
        attribute outfitsport3 if_not ["hair", "hair_braids", "wethair", "green_hair"]:
            "joyce_hair_back_outfitsport"
        attribute sporthair:
            "joyce_hair_back_outfitsport"

    group arm variant "back":

        attribute arm default: #the default argument means we're always including the attribute "arm"
            null

        attribute arm if_not ["outfitcasino", "night4", "night5", "holdbook"]:
            "joyce_arm"
        attribute hide1:
            "joyce_arm_hide_back"
        attribute arm if_any "outfit1":
            "joyce_arm_1"
        attribute arm if_any "night":
            "joyce_arm_night"
        attribute arm if_any "outfitcasino":
            "joyce_arm_casino"
        attribute arm if_any "outfitsport":
            "joyce_arm_sport"
        attribute arm if_any "outfit5" "joyce_arm_right_back_5"
        attribute arm if_any "outfit5" "joyce_arm_left_back_5"
        attribute arm if_any "night4":
            "joyce_arm_hide_back"

        attribute arm if_any "holdbook" "joyce_arm_holdbook_back"

        attribute armbehind
        attribute armbehind if_any "outfitsport" "joyce_arm_armbehind_sport"

        attribute armcheek
        attribute armcheek "joyce_arm_left_back"
        attribute armcheek if_any "outfit5" "joyce_arm_left_back_5"
        attribute armcheek if_any "night" "joyce_arm_left_back_night"
        attribute armcheek if_any "outfitsport" "joyce_arm_left_back_sport"

        attribute armmouth "joyce_arm_back_armcheek"
        attribute armmouth "joyce_arm_left_back"
        attribute armmouth if_any "outfit5" "joyce_arm_left_back_5"
        attribute armmouth if_any "night" "joyce_arm_left_back_night"
        attribute armmouth if_any "outfitsport" "joyce_arm_left_back_sport"

        attribute armhip
        attribute armhip "joyce_arm_right_back"
        attribute armhip if_all "outfit5" "joyce_arm_armhip_5"
        attribute armhip if_all "outfit5" "joyce_arm_right_back_5"
        attribute armhip if_any "night" "joyce_arm_armhip_night"
        attribute armhip if_any "outfitsport" "joyce_arm_right_sport"
        attribute armhip if_any "outfitsport" "joyce_arm_armhip_sport"

        attribute armthink "joyce_arm_armthink_back"

        attribute handover "joyce_arm_right_back"
        attribute handover if_any "outfit1" "joyce_arm_right_1"
        attribute handover if_any "outfitsport" "joyce_arm_right_sport"

        attribute pose:
            "joyce_arm_back_right_half"
        attribute pose:
            "joyce_arm_back_left_half"

        attribute defend:
            "joyce_arm_defend_back"

        attribute holdglasses if_any "sitted":
            "joyce_arm_back_right_half"
        attribute holdglasses if_not "sitted" "joyce_arm_right_back"

        attribute reveal-1 if_not "night":
            "joyce_arm_left_back"
        attribute reveal-1 if_any "night":
            "joyce_arm_left_back_night"
        attribute reveal-2 if_any "night":
            "joyce_arm_left_back_night"
        attribute reveal-2 if_not ["night","night3", "night4", "night5"]:
            "joyce_arm_left_back"

        attribute armprison "joyce_arm_hide_back"

        attribute push "joyce_arm_right_back"
        attribute push if_any "outfit5" "joyce_arm_right_back_5"
        attribute push if_any "outfitsport" "joyce_arm_right_sport"


        attribute key "joyce_arm_key"
        attribute key "joyce_arm_right_back"
        attribute key if_any "outfit5" "joyce_arm_key_5"
        attribute key if_any "outfit5" "joyce_arm_right_back_5"

        attribute armcross:
            "joyce_arm_armcross_back"

        attribute running if_not ["outfitsport"]:
            "joyce_arm_back_diagonal"
        attribute running if_any ["outfitsport"]:
            "joyce_arm_back_diagonal_sport"

            
        attribute shh "joyce_arm_whisper_back"
        attribute shh if_not "holdbook" "joyce_arm_right_back"
        attribute shh if_any "outfit1" "joyce_arm_right_1"
        attribute shh if_any "outfit5" "joyce_arm_right_back_5"
        attribute shh if_any "outfitsport" "joyce_arm_right_sport"
        
        attribute throwWater "joyce_arm_right_back"
        attribute wave "joyce_arm_back_diagonal_right"
        attribute wave "joyce_arm_left_back"
        attribute wave if_all "outfitsport" "joyce_arm_left_back_sport"
        attribute wave if_all "outfitsport" "joyce_arm_back_diagonal_right_sport"
        attribute wave if_all "outfit1" "joyce_arm_left_1"
        attribute pointer "joyce_arm_pointer_back_5"
        attribute whisper "joyce_arm_whisper_back"
        attribute whisper if_not "holdbook" "joyce_arm_right_back"
        attribute whisper if_any "outfit5" "joyce_arm_right_back_5"

    group base variant "defend" if_any "defend" auto
    group base variant "reveal-2" if_any "reveal-2" auto
    group base variant "reveal" if_any "reveal" auto

    group base auto:
        attribute night6 default
        attribute outfitred if_not ["reveal-2", "defend"]
        attribute outfitblue if_not "reveal-2"
        attribute night if_not "reveal-2"
        attribute night2 if_not "reveal-2"
        attribute night3 if_not "reveal-2"
        attribute night4 if_not "reveal-2"
        attribute night5 if_not "reveal-2"
        attribute outfitsport if_not "changing"
        attribute outfitsport if_all "changing" "joyce_base_outfitsport_changing"
        attribute outfitsport2 if_not "changing" 
        attribute outfitsport2 if_all "changing" "joyce_base_outfitsport2_changing"
        
    
    group accessories:
        attribute hat  "joyce_accessories-hat_back"
        attribute hat2 "joyce_accessories-hat_back"
        attribute hat3 "joyce_accessories-hat_back"

    group face:
        attribute face default:
            "joyce_face"
        attribute sweaty
        attribute sweaty2

    group skin:
        attribute null_skin if_any "null" null
        attribute blush
        attribute halfblush

    group eyes auto:
        attribute null_eyes default:
            "img_blink" #null
        attribute upset
        attribute worried
        attribute eyeside
        attribute foxy
        attribute wink
        attribute happy
        attribute eyesdown
        attribute squint
        attribute bored

    attribute jawOpen "joyce_jawopen" default if_any ["smile", "breath", "mouthahegao", "biglick"]
    attribute holdbook null
    attribute tears
    attribute halftears
    attribute halfslapped
    attribute slapped
    attribute poches

    group mouth auto: #if_not "null":
        attribute null_mouth default:
            "joyce_mouth_normal"
        attribute smile 
        attribute smirk
        attribute tongue
        attribute bite
        attribute breath
        attribute mouthopen

    group arm: #  variant "front" BEHIND HAIR

        attribute arm if_any "sitted" "joyce_arm_front_sitted_right"
        attribute arm if_any "sitted" "joyce_arm_front_sitted_left"
        attribute arm if_any "holdbook" "joyce_arm_holdbook"

        # attribute armcross if_any ["sitted-swimsuit2", "night4", "night5", "night6", "outfitsport3", "night9"] "joyce_arm_armfolded"
        attribute armcross if_not ["outfit1"] "joyce_arm_armcross_front"        
        attribute armcross if_all ["outfitsport"] "joyce_arm_armcross_front_sport"        
        attribute armcross if_any ["outfit1"] "joyce_arm_armcross_1"
        attribute armcross if_any ["outfit2"] "joyce_arm_armcross_2"
        attribute armcross if_any "night" "joyce_arm_armcross_night"
        attribute armcross if_any "outfit5" "joyce_arm_armcross_5"
        attribute armcross if_any "outfit4" "joyce_arm_armcross_4"
        attribute armcross if_any ["sitted-swimsuit2", "night4", "night5", "night6", "outfitsport3", "night9"]  "joyce_arm_armcross_bare"

        attribute armthink if_any ["sitted-swimsuit2", "night4", "night5", "night6", "outfitsport3", "night9"] "joyce_arm_armfolded"

        attribute reveal-1 if_not ["night"]:
            "joyce_arm_right_reveal (1)"
        attribute reveal-1 if_any ["night"]:
            "joyce_arm_right_reveal (1)_night"
        attribute reveal-2 if_not ["night","night3", "night4", "night5"]:
            "joyce_arm_right_reveal (2)"
        attribute reveal-2 if_any ["night"]:
            "joyce_arm_right_reveal (2)_night"
        attribute armsopen "joyce_arm_front_armsopen"

        attribute pose:
            "joyce_arm_front_sitted_right"
        attribute pose:
            "joyce_arm_front_sitted_left"
        attribute pose if_any "outfitsport" "joyce_arm_pose_sport"
        attribute pose if_any "outfit5" "joyce_arm_pose_5"
        
        attribute arm if_any "night4":
            "joyce_arm_hide_front"
        attribute arm if_any "night5" "joyce_arm_hide2_night5"
        attribute hide1:
            "joyce_arm_hide_front"
        attribute hide1 if_any "night" "joyce_arm_hide_night"
        attribute hide1 if_any "outfitsport"  "joyce_arm_hide_sport"
        attribute hide2 if_not ["night5"] "joyce_arm_hide2"
        attribute hide2 if_any ["night5"] "joyce_arm_hide2_night5"

        attribute holdglasses if_any "sitted" "joyce_arm_front_sitted_right"

        attribute running if_not ["outfitsport"]:
            "joyce_arm_front_running"
        attribute running if_any ["outfitsport"]:
            "joyce_arm_front_running_sport"

    group accessories:
        attribute outfitred if_not "no_accessory":
            "joyce_accessories_pearls"
        attribute outfitblue if_not "no_accessory":
            "joyce_accessories_pearls"
        attribute pearls

    group overlay auto

    group hair variant "front":
        attribute hair: 
            "joyce_hair_front" 
        attribute hair_braids
        attribute green_hair:
            "joyce_hair_front_green"
        attribute outfitsport if_not ["hair", "hair_braids", "wethair", "green_hair"]
        attribute outfitsport2 if_not ["hair", "hair_braids", "wethair", "green_hair"]:
            "joyce_hair_front_outfitsport"
        attribute outfitsport3 if_not ["hair", "hair_braids", "wethair", "green_hair"]:
            "joyce_hair_front_outfitsport"
        attribute sporthair:
            "joyce_hair_front_outfitsport"
        attribute wet
        attribute wethair "joyce_hair_front_wet"

    
    group accessories auto:
        attribute no_accessory null
        attribute outfit5 if_not ["no_accessory", "sunglasses", "sunglasses2", "glasses", "hat2"]:
            "joyce_glasses_5"
        attribute mask "joyce_glasses_5"
        attribute pearls null
        attribute sweaty:
            "joyce_sweaty"
        attribute sweaty2:
            "joyce_sweaty2"
        attribute sunglasses
        attribute sunglasses2

    group arm: #variant "in front of hair"

        attribute armcheek
        attribute armcheek if_any "outfit5" "joyce_arm_armcheek_5"
        attribute armcheek if_any "night" "joyce_arm_armcheek_night"
        attribute armcheek if_any "outfit4" "joyce_arm_armcheek_4"
        attribute armcheek if_any "outfitsport" "joyce_arm_armcheek_sport"

        attribute armmouth
        attribute armmouth if_any "outfit5" "joyce_arm_armmouth_5"
        attribute armmouth if_any "night" "joyce_arm_armmouth_night"
        attribute armmouth if_any "outfit4" "joyce_arm_armmouth_4"
        attribute armmouth if_any "outfitsport" "joyce_arm_armmouth_sport"

        attribute armprison "joyce_arm_armprison"
        
        attribute armthink "joyce_arm_armthink"
        attribute armthink if_any "night" "joyce_arm_armthink_night"
        attribute armthink if_any "outfitsport" "joyce_arm_armthink_sport"
        attribute armthink if_any "outfit1" "joyce_arm_armthink_1"
        attribute armthink if_any "outfit5" "joyce_arm_armthink_5"
        attribute armthink if_any "outfit4" "joyce_arm_armthink_4"
        
        attribute pointer:
            "joyce_arm_pointer_front_5"
        attribute push "joyce_arm_push"
        attribute push if_any "outfit5" "joyce_arm_push_5"
        attribute push if_any "night" "joyce_arm_push_night"
        attribute push if_any "outfitsport" "joyce_arm_push_sport"
        attribute defend:
            "joyce_arm_defend_front"
        # attribute defend if_any "outfitblue":
        #     "joyce_blue_defend"
        attribute defend if_any "outfitsport":
            "joyce_arm_defend_front_sport"
        attribute defend if_any "night":
            "joyce_arm_defend_night"
        attribute defend if_any "outfit4" "joyce_arm_defend_4"
        attribute defend if_any "outfit1" "joyce_arm_defend_1"
        attribute defend if_any ["sitted-swimsuit2", "night4", "night5", "night6", "outfitsport3", "night9"] "joyce_arm_defend_bare"

        attribute handover "joyce_arm_handover"
        attribute handover if_any "outfit1" "joyce_arm_handover_1"
        attribute handover if_any "outfit4" "joyce_arm_handover_4"
        attribute handover if_any "outfitsport" "joyce_arm_handover_sport"
        attribute holdglasses:
            "joyce_arm_holdglasses"

        attribute shh "joyce_arm_right_shh"
        attribute shh if_all "holdbook" "joyce_arm_holdbook_right"
        attribute shh if_any "outfit1" "joyce_arm_shh_1"
        attribute shh if_any "night" "joyce_arm_shh_night"
        attribute shh if_any "outfit5" "joyce_arm_shh_5"
        attribute shh if_any "outfitsport" "joyce_arm_shh_sport"

        attribute throwWater:
            "joyce_arm_throwwater"
        attribute changing:
            "joyce_arm_changing"
        attribute changing if_any ["outfitsport"]:
            "joyce_arm_front_sport_changing"
        attribute changing if_any ["outfitsport2"]:
            "joyce_arm_changing_sport2"
        
        attribute wave "joyce_arm_wave"
        attribute wave if_all "outfitsport" "joyce_arm_wave_sport"
        attribute wave if_all "outfit1" "joyce_arm_wave_1"
        attribute wave if_all "night" "joyce_arm_wave_night"
        attribute whisper:
            "joyce_arm_whisper_front"
        attribute whisper if_all "holdbook":
            "joyce_arm_holdbook_right"
        attribute whisper if_any "night" "joyce_arm_whisper_night"
        attribute whisper if_any "outfitsport" "joyce_arm_whisper_sport"
        attribute whisper if_any "outfit5" "joyce_arm_whisper_5"
