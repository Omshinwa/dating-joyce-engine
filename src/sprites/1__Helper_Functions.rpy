# The runtime half of the sprite system.
#
# `1__Image_Definition.rpy` declares which layers are legal together. This file is what
# the script actually calls to change one part of the character without disturbing the
# rest — the common case being "keep everything as it is, but change the expression".
#
# `show()` is the interesting one. Ren'Py's own `show joyce smile` replaces attributes
# within a group and leaves the others alone, but that isn't enough here: several of the
# character's images are pose-specific, so "smile" during a `sitted` scene has to resolve
# to a different file than "smile" while standing. So `show()` reads the attributes
# currently on screen, folds the ones that matter into the requested image name, and
# probes with `renpy.can_show()` before committing — falling back to the plain image when
# no pose-specific variant was drawn. Callers stay ignorant of which variants exist.

init python:

    def joyce_has_attr_from_group(group):
        """True if any attribute currently shown on the character belongs to `group`."""
        for attr in renpy.get_attributes("joyce"):
            if group in renpy.get_registered_image('joyce').attribute_to_groups[attr]:
                return True
        return False

    def joyce_has_attribute(*args, mode="or", layer=None):
        """
        When you put several args, it checks in OR
        """
        if renpy.get_attributes("joyce", layer=layer) == None:
            return False

        #IF several args: OR OPERATOR
        if mode == "or":
            for arg in args:
                if arg in renpy.get_attributes("joyce"):
                    return True
            return False
        elif mode == "and":
            for arg in args:
                if not arg in renpy.get_attributes("joyce"):
                    return False
            return True

    def show(img:str, transition=True, throwError=True, at_list=[], layer="joyce"): #used to show face part usually smile and eyes
        """
        throwError will try to show the img even if it cannot
        """
        for attr in renpy.get_attributes("joyce"):
            # Pose attributes always force a variant: every face part was drawn per pose.
            if attr in ["sitted", "standup", "running", "holdbook", "swim", "prison", "sleep", "kiss", "dance"]:
                img += " " + attr

            # These have variants for some parts but not all, so probe first.
            elif attr in ["v2", "bare"]:
                if renpy.can_show(img + " " + attr):
                    img += " " + attr

            # Intermediate outfit states reuse the same art as the final one.
            elif attr in ["outfit6", "halfbare"]:
                if renpy.can_show(img + " bare"):
                    img += " bare"

            else: # only works if theres only 1 attr left to add
                if renpy.can_show(img + " " + attr):
                    img += " " + attr

        if throwError or renpy.can_show(img):
            # The character lives on a dedicated layer during scenes and on master
            # elsewhere; show it wherever it currently is.
            if layer == "joyce":
                if renpy.showing("joyce", layer="char"):
                    renpy.show(img, at_list=at_list, layer="char")
                elif renpy.showing("joyce", layer="master"):
                    renpy.show(img, at_list=at_list, layer="master")
            else:
                renpy.show(img, at_list=at_list, layer=layer)
            if transition:
                renpy.with_statement(dissolve)
