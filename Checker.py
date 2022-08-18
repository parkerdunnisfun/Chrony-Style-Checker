from cgitb import text
import re

class MarkedUp:
    """
    Text that has position of Chrony style accuracies and errors identified.

    Attributes:
        errors  dict holding starting index of error and type of error
        good    dict holding starting index of accuracy and type of accuracy
        text    the text we're marking up
    """

    errors = {}
    good = {}
    text = ""

    def __init__(self, words):
        """
        Setting our text.
        """
        MarkedUp.text = words

    def clear(self):
        """
        Clears errors and good dicts.
        """
        self.errors.clear()
        self.good.clear()

    def u_reference_check(self):
        """
        Locates instances of "University of Utah" and "the U" then identifies which are good and bad.
        """
        # where "University of Utah" and "the U" occur in text
        instances_u_of_u = [m.start() for m in re.finditer("University of Utah", MarkedUp.text, re.IGNORECASE)]
        instances_u = [m.start() for m in re.finditer("the U", MarkedUp.text, re.IGNORECASE)]

        # remove intersection from instances_u ("The University of Utah" contains "The U")
        to_remove = []
        for x in instances_u_of_u:
            for y in instances_u:
                if x - y == 4:
                    to_remove.append(y)

        for x in to_remove:
            instances_u.remove(x)

        # any "the U" that comes before first "University of Utah" should be put into errors array; any after into good array
        if not instances_u_of_u:
            first_u_of_u = len(self.text)
        else: 
            first_u_of_u = instances_u_of_u[0]
        bad_u = []
        good_u = []
        for x in instances_u:
            if x < first_u_of_u:
                bad_u.append(x)
            else: good_u.append(x)

        # adding good and bad "University of Utah"
        if not not instances_u_of_u:
            bad_u_of_u = instances_u_of_u[1:]
            good_u_of_u = instances_u_of_u[0]
        else:
            bad_u_of_u = []
            good_u_of_u = -1

        # move accuracies and errors to appropriate dicts
        for x in bad_u:
            self.errors[(x, x+4)] = "u"
        for x in good_u:
            self.good[(x, x+4)] = "u"
        for x in bad_u_of_u:
            self.errors[(x, x+17)] = "uofu"
        if good_u_of_u != -1:
            self.good[(good_u_of_u, good_u_of_u+17)] = "uofu"
