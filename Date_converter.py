from calendar import isleap
from curses.ascii import isdigit

# month abbreviations per Chrony/AP style
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

def is_valid_date(date):
    """
    Lets us know whether or not a given date is valid based on criteria detailed in comments below.
    
    :param date: The date to be evaluated
    :type date: str
    :returns: an indication of whether or not a date is valid
    :rtype: bool
    """
    # does date follow requested format (mm/dd/yyyy)?
    if len(date) == 10:
        for idx, x in enumerate(date):
            if idx != 2 and idx != 5:
                if not isdigit(x):
                    return False
            elif x != '/':
                return False
    else: return False

    # does date respect no-zero rule (e.g. can't have 00/dd/yyyy or mm/00/yyyy)?
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
    """
    Converts a valid date into its AP-style-adhering counterpart
    
    :param date: The date to be converted
    :type date: str
    :returns: date in AP style
    :rtype: str
    """
    
    if not is_valid_date(date):
        return "Error: invalid date"

    dateArray = date.split('/')

    return months[dateArray[0]] + " " + dateArray[1].lstrip('0') + ", " + dateArray[2].lstrip('0')