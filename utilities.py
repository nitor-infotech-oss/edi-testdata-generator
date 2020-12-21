import datetime
import random
import string

class Utilites():
    def __init__(self):
        self.__classname__     = 'Utilites'

    def date(self, format, mindiff=1, maxdiff=65):
        randomDaysDiff   = random.randrange(mindiff*365, maxdiff*365)
        randomDate       = datetime.date.today() - datetime.timedelta(days=randomDaysDiff)
        return randomDate.strftime(format)

    def time(self, format):
        randomDateTime = datetime.datetime.now() - datetime.timedelta(minutes=random.randrange(3600))
        return randomDateTime.strftime(format)

    def series(self, len, seriesType="num"):
        randValues = string.digits
        if seriesType == 'alphanum':
            randValues = string.ascii_letters + string.digits
        return ''.join((random.choice(randValues) for i in range(len)))

    def class_to_edi_string(self, variableValues, ediString):
        for key in variableValues.keys():
            stringKeyword = '{'+key+'}'
            if (stringKeyword) in ediString:
                stringValue = str(variableValues[key])
                ediString = ediString.replace(stringKeyword, stringValue)
        return ediString
