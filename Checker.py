import re

class MarkedUp:

    errors = {}
    good = {}
    words = []

    def __init__(self, text):
        self.text = text
        words = text.split(" ")

    def u_reference_check(text):
        # where "University of Utah" and "the U" occur in text
        instances_u_of_u = [m.start() for m in re.finditer("University of Utah", text, re.IGNORECASE)]
        instances_u = [m.start() for m in re.finditer("the U", text, re.IGNORECASE)]
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
        first_u_of_u = instances_u_of_u[0]
        bad = []
        good = []
        for x in instances_u:
            if x < first_u_of_u:
                bad.append(x)
            else: good.append(x)

        # bad = instances_u[ : instances_u.index(first_u_of_u) - 1]
        # good = instances_u[instances_u.index(first_u_of_u) : ]

        # adding good and bad "University of Utah"
        bad.append(instances_u_of_u[1:])
        good.append(instances_u_of_u[0])

        return good

def main():
    text = input("Insert text: ")
    print(MarkedUp.u_reference_check(text))

if __name__ == "__main__":
    main()
