import unittest
from Date_converter import convert

class January(unittest.TestCase):
    """
    Testing that every day in January is considered valid and is convereted to Chrony style correctly.
    """
    
    def test_days(self):
        """
        See January class documentation.
        """
        for i in range(1, 32, 1):
            day = str(i)
            if len(day) == 1:
                day = "0" + day
            date = "01/" + day + "/2022"
            self.assertEqual(convert(date), "Jan. " + str(i) + ", 2022", "Should be: Jan. " + str(i) + ", 2022")

    def test_out_of_bounds(self):
        """
        Testing invalid date with nonexisting day in January.
        """
        date = "01/32/2022"
        self.assertEqual(convert(date), "Error: invalid date", "Should be: Error: invalid date")

class February(unittest.TestCase):
    """
    Testing that every day in February is considered valid and is convereted to Chrony style correctly.
    """
    
    def test_days(self):
        """
        See February class documentation.
        """
        # non-leap
        for i in range(1, 28, 1):
            day = str(i)
            if len(day) == 1:
                day = "0" + day
            date = "02/" + day + "/2022"
            self.assertEqual(convert(date), "Feb. " + str(i) + ", 2022", "Should be: Feb. " + str(i) + ", 2022")
        # leap
        date = "02/29/2020"
        self.assertEqual(convert(date), "Feb. 29, 2020", "Should be: Feb. 29, 2020")

    def test_out_of_bounds(self):
        """
        Testing invalid date with nonexisting day in February.
        """
        # non-leap
        date = "02/29/2022"
        self.assertEqual(convert(date), "Error: invalid date", "Should be: Error: invalid date")
        #leap
        date = "02/30/2020"
        self.assertEqual(convert(date), "Error: invalid date", "Should be: Error: invalid date")

class March(unittest.TestCase):
    """
    Testing that every day in March is considered valid and is convereted to Chrony style correctly.
    """
    
    def test_days(self):
        """
        See March class documentation.
        """
        for i in range(1, 32, 1):
            day = str(i)
            if len(day) == 1:
                day = "0" + day
            date = "03/" + day + "/2022"
            self.assertEqual(convert(date), "March " + str(i) + ", 2022", "Should be: March " + str(i) + ", 2022")

    def test_out_of_bounds(self):
        """
        Testing invalid date with nonexisting day in March.
        """
        date = "03/32/2022"
        self.assertEqual(convert(date), "Error: invalid date", "Should be: Error: invalid date")

class April(unittest.TestCase):
    """
    Testing that every day in April is considered valid and is convereted to Chrony style correctly.
    """
    
    def test_days(self):
        """
        See April class documentation.
        """
        for i in range(1, 31, 1):
            day = str(i)
            if len(day) == 1:
                day = "0" + day
            date = "04/" + day + "/2022"
            self.assertEqual(convert(date), "April " + str(i) + ", 2022", "Should be: April " + str(i) + ", 2022")

    def test_out_of_bounds(self):
        """
        Testing invalid date with nonexisting day in April.
        """
        date = "04/31/2022"
        self.assertEqual(convert(date), "Error: invalid date", "Should be: Error: invalid date")

class May(unittest.TestCase):
    """
    Testing that every day in May is considered valid and is convereted to Chrony style correctly.
    """
    
    def test_days(self):
        """
        See May class documentation.
        """
        for i in range(1, 32, 1):
            day = str(i)
            if len(day) == 1:
                day = "0" + day
            date = "05/" + day + "/2022"
            self.assertEqual(convert(date), "May " + str(i) + ", 2022", "Should be: May " + str(i) + ", 2022")

    def test_out_of_bounds(self):
        """
        Testing invalid date with nonexisting day in May.
        """
        date = "05/32/2022"
        self.assertEqual(convert(date), "Error: invalid date", "Should be: Error: invalid date")

class June(unittest.TestCase):
    """
    Testing that every day in June is considered valid and is convereted to Chrony style correctly.
    """
    
    def test_days(self):
        """
        See June class documentation.
        """
        for i in range(1, 31, 1):
            day = str(i)
            if len(day) == 1:
                day = "0" + day
            date = "06/" + day + "/2022"
            self.assertEqual(convert(date), "June " + str(i) + ", 2022", "Should be: June " + str(i) + ", 2022")

    def test_out_of_bounds(self):
        """
        Testing invalid date with nonexisting day in June.
        """
        date = "06/31/2022"
        self.assertEqual(convert(date), "Error: invalid date", "Should be: Error: invalid date")

class July(unittest.TestCase):
    """
    Testing that every day in July is considered valid and is convereted to Chrony style correctly.
    """
    
    def test_days(self):
        """
        See July class documentation.
        """
        for i in range(1, 32, 1):
            day = str(i)
            if len(day) == 1:
                day = "0" + day
            date = "07/" + day + "/2022"
            self.assertEqual(convert(date), "July " + str(i) + ", 2022", "Should be: July " + str(i) + ", 2022")

    def test_out_of_bounds(self):
        """
        Testing invalid date with nonexisting day in July.
        """
        date = "07/32/2022"
        self.assertEqual(convert(date), "Error: invalid date", "Should be: Error: invalid date")

class August(unittest.TestCase):
    """
    Testing that every day in August is considered valid and is convereted to Chrony style correctly.
    """
    
    def test_days(self):
        """
        See August class documentation.
        """
        for i in range(1, 32, 1):
            day = str(i)
            if len(day) == 1:
                day = "0" + day
            date = "08/" + day + "/2022"
            self.assertEqual(convert(date), "Aug. " + str(i) + ", 2022", "Should be: Aug. " + str(i) + ", 2022")

    def test_out_of_bounds(self):
        """
        Testing invalid date with nonexisting day in August.
        """
        date = "08/32/2022"
        self.assertEqual(convert(date), "Error: invalid date", "Should be: Error: invalid date")

class September(unittest.TestCase):
    """
    Testing that every day in September is considered valid and is convereted to Chrony style correctly.
    """
    
    def test_days(self):
        """
        See September class documentation.
        """
        for i in range(1, 31, 1):
            day = str(i)
            if len(day) == 1:
                day = "0" + day
            date = "09/" + day + "/2022"
            self.assertEqual(convert(date), "Sept. " + str(i) + ", 2022", "Should be: Sept. " + str(i) + ", 2022")

    def test_out_of_bounds(self):
        """
        Testing invalid date with nonexisting day in September.
        """
        date = "09/31/2022"
        self.assertEqual(convert(date), "Error: invalid date", "Should be: Error: invalid date")

class October(unittest.TestCase):
    """
    Testing that every day in October is considered valid and is convereted to Chrony style correctly.
    """
    
    def test_days(self):
        """
        See October class documentation.
        """
        for i in range(1, 32, 1):
            day = str(i)
            if len(day) == 1:
                day = "0" + day
            date = "10/" + day + "/2022"
            self.assertEqual(convert(date), "Oct. " + str(i) + ", 2022", "Should be: Oct. " + str(i) + ", 2022")

    def test_out_of_bounds(self):
        """
        Testing invalid date with nonexisting day in October.
        """
        date = "10/32/2022"
        self.assertEqual(convert(date), "Error: invalid date", "Should be: Error: invalid date")

class November(unittest.TestCase):
    """
    Testing that every day in November is considered valid and is convereted to Chrony style correctly.
    """
    
    def test_days(self):
        """
        See November class documentation.
        """
        for i in range(1, 31, 1):
            day = str(i)
            if len(day) == 1:
                day = "0" + day
            date = "11/" + day + "/2022"
            self.assertEqual(convert(date), "Nov. " + str(i) + ", 2022", "Should be: Nov. " + str(i) + ", 2022")

    def test_out_of_bounds(self):
        """
        Testing invalid date with nonexisting day in November.
        """
        date = "11/31/2022"
        self.assertEqual(convert(date), "Error: invalid date", "Should be: Error: invalid date")

class December(unittest.TestCase):
    """
    Testing that every day in December is considered valid and is convereted to Chrony style correctly.
    """
    
    def test_days(self):
        """
        See December class documentation.
        """
        for i in range(1, 32, 1):
            day = str(i)
            if len(day) == 1:
                day = "0" + day
            date = "12/" + day + "/2022"
            self.assertEqual(convert(date), "Dec. " + str(i) + ", 2022", "Should be: Dec. " + str(i) + ", 2022")

    def test_out_of_bounds(self):
        """
        Testing invalid date with nonexisting day in December.
        """
        date = "12/32/2022"
        self.assertEqual(convert(date), "Error: invalid date", "Should be: Error: invalid date")

class NonDates(unittest.TestCase):
    """
    Testing that invalid dates give error messages.
    """

    def test_zeroes(self):
        """
        Testing invalid dates with zeroes
        """
        date = "00/00/0000"
        self.assertEqual(convert(date), "Error: invalid date", "Should be: Error: invalid date")
        date = "00/00/0001"
        self.assertEqual(convert(date), "Error: invalid date", "Should be: Error: invalid date")
        date = "00/01/0000"
        self.assertEqual(convert(date), "Error: invalid date", "Should be: Error: invalid date")
        date = "00/01/0001"
        self.assertEqual(convert(date), "Error: invalid date", "Should be: Error: invalid date")
        date = "01/00/0000"
        self.assertEqual(convert(date), "Error: invalid date", "Should be: Error: invalid date")
        date = "01/00/0001"
        self.assertEqual(convert(date), "Error: invalid date", "Should be: Error: invalid date")
        date = "01/01/0000"
        self.assertEqual(convert(date), "Error: invalid date", "Should be: Error: invalid date")

    def test_random_chars(self):
        """
        Testing invalid dates with random chars.
        """
        date = "abcdefghij"
        self.assertEqual(convert(date), "Error: invalid date", "Should be: Error: invalid date")
        date = "ab/cd/efgh"
        self.assertEqual(convert(date), "Error: invalid date", "Should be: Error: invalid date")
        date = "abc"
        self.assertEqual(convert(date), "Error: invalid date", "Should be: Error: invalid date")
        date = "xyzxyzxyzxyzxyz"
        self.assertEqual(convert(date), "Error: invalid date", "Should be: Error: invalid date")
        date = "03/16/99999"
        self.assertEqual(convert(date), "Error: invalid date", "Should be: Error: invalid date")
        date = ""
        self.assertEqual(convert(date), "Error: invalid date", "Should be: Error: invalid date")
        date = "11.04.1972"
        self.assertEqual(convert(date), "Error: invalid date", "Should be: Error: invalid date")

    def test_out_of_bounds_month(self):
        """
        Testing invalid date with nonexisting month.
        """
        date = "13/22/2018"
        self.assertEqual(convert(date), "Error: invalid date", "Should be: Error: invalid date")

if __name__ == '__main__':
    unittest.main()