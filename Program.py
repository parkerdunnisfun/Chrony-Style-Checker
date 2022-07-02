from calendar import isleap
from curses.ascii import isdigit

months = {
        "01": "Jan.",
        "02": "Feb.",
        "03": "March",
        "04": "April",
        "05": "May",
        "06": "June",
        "07": "July",
        "08": "Aug.",
        "09": "Sept.",
        "10": "Oct.",
        "11": "Nov.",
        "12": "Dec.",
    }

def isValidDate(date):    
    # does date follow requested format?
    if len(date) == 10:
        for idx, x in enumerate(date):
            if idx != 2 and idx != 5:
                if not isdigit(x):
                    return False
            elif x != '/':
                return False
    else: return False

    # dose date respect no-zero rule?
    if int(date[0:2]) == 0 or int(date[3:5]) == 0 or int(date[6:]) == 0:
        return False

    # does date respect maximum months rule?
    if int(date[0:2]) > 12:
        return False

    # does date respect maximum days rule?
    if int(date[1]) % 2 == 0:
        #if month is february
        if int(date[1]) == 2 and int(date[0]) == 0:
            if int(date[3:5]) > 28:
                if not isleap(int(date[6:10])):
                    return False
                elif int(date[3:5]) > 29:
                    return False
        # month is not february
        elif int(date[0:2]) < 8:
            if int(date[3:5]) > 30:
                return False
        elif int(date[3:5]) > 31:
            return False
    elif int(date[0:2]) >= 8:
        if int(date[3:5]) > 30:
            return False
    elif int(date[3:5]) > 31:
        return False

    return True

def convert(date):
    
    if not isValidDate(date):
        return "Error: invalid date"

    dateArray = date.split('/')

    return months[dateArray[0]] + " " + dateArray[1].lstrip('0') + ", " + dateArray[2].lstrip('0')

def main():
    date = input("Type a date in mm/dd/yyyy format: ")
    print(convert(date))

if __name__ == "__main__":
    main()