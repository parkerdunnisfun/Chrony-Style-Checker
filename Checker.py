from cgitb import text
import re

class MarkedUp:

    errors = {}
    good = {}
    warnings = {}
    text = ""

    def __init__(self, words):
        MarkedUp.text = words
        # words = text.split(" ")

    def clear(self):
        self.errors.clear()
        self.good.clear()
        self.warnings.clear()

    def u_reference_check(self):
        # where "University of Utah" and "the U" occur in text
        instances_u_of_u = [m.start() for m in re.finditer("University of Utah", MarkedUp.text, re.IGNORECASE)]
        instances_u = [m.start() for m in re.finditer("the U", MarkedUp.text, re.IGNORECASE)]
        # remove intersection from instances_u
        to_remove = []
        for x in instances_u_of_u:
            for y in instances_u:
                if x - y == 4:
                    to_remove.append(y)

        for x in to_remove:
            instances_u.remove(x)


        # intersection = list(set(instances_u_of_u) & set(instances_u))
        # instances_u.remove(intersection)

        # any "the U" that comes before should be put into errors arrray; any after into good array
        if not instances_u_of_u:
            first_u_of_u = len(self.text)
        else: 
            first_u_of_u = instances_u_of_u[0] # TO-DO: check for cases where there is no u of u
        bad_u = []
        good_u = []
        for x in instances_u:
            if x < first_u_of_u:
                bad_u.append(x)
            else: good_u.append(x)

        # bad = instances_u[ : instances_u.index(first_u_of_u) - 1]
        # good = instances_u[instances_u.index(first_u_of_u) : ]

        # adding good and bad "University of Utah"
        if not not instances_u_of_u:
            bad_u_of_u = instances_u_of_u[1:]
            good_u_of_u = instances_u_of_u[0]
        else:
            bad_u_of_u = []
            good_u_of_u = -1

        # add bad to errors dict and good to good list, university of utah
        for x in bad_u:
            self.errors[(x, x+4)] = "u"
        for x in good_u:
            self.good[(x, x+4)] = "u"
        for x in bad_u_of_u:
            self.errors[(x, x+17)] = "uofu"
        if good_u_of_u != -1:
            self.good[(good_u_of_u, good_u_of_u+17)] = "uofu"

    def oxford_comma_check(self):
        oxcommas_and = [m.start() for m in re.finditer(", and ", MarkedUp.text, re.IGNORECASE)]
        oxcommas_or = [m.start() for m in re.finditer(", or ", MarkedUp.text, re.IGNORECASE)]

        for x in oxcommas_and:
            self.warnings[(x, x)] = "oxc"
        for x in oxcommas_or:
            self.warnings[(x, x)] = "oxc"

# def main():
#     text = input("Insert text: ")
#     print(MarkedUp.u_reference_check(text))

# if __name__ == "__main__":
#     main()
