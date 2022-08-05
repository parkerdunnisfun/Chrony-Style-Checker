import re

class MarkedUp:

    errors = {}
    good = {}
    text = ""
    click_count = 0

    def __init__(self, words):
        MarkedUp.text = words
        # words = text.split(" ")

    def clear(self):
        self.errors.clear()
        self.good.clear()

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

        bad_u_of_u = instances_u_of_u[1:]
        good_u_of_u = instances_u_of_u[0]

        # add bad to errors dict and good to good list, university of utah
        for x in bad_u:
            self.errors[(x, x+4)] = "u"
        for x in good_u:
            self.good[(x, x+4)] = "u"
        for x in bad_u_of_u:
            self.errors[(x, x+17)] = "uofu"
        self.good[(good_u_of_u, good_u_of_u+17)] = "uofu"

        # return MarkedUp.errors

# def main():
#     text = input("Insert text: ")
#     print(MarkedUp.u_reference_check(text))

# if __name__ == "__main__":
#     main()
