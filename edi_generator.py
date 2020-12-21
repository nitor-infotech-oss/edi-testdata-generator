import sys
import random
import datetime
from sponsor import Sponsor
from subscriber import Subscriber
from dependent import Dependent
from templates import edi_file as edi
from config_value_generator import ConfigValueGenerator
import argparse

class EDIGenerator():
    def __init__(self, parameters):
        self.__classname__      = 'EDIGenerator'
        self.cfg                = ConfigValueGenerator()
        self.outputFilePath     = parameters["outputFilePath"]
        self.generateCount      = parameters["count"]
        self.addSpouse          = parameters["spouse"]
        self.edi_string         = edi.EDI_DETAILS
        self.childrenCount      = parameters["childrenCount"]
        self.SponserName        = parameters["sponsorName"]
        self.befinciaryPlanName = parameters["befinciaryPlanName"]
        self.ploicyId           = parameters["ploicyId"]
        self.effectiveDate      = parameters["effectiveDate"]
        self.minAge             = parameters["min_age"]
        self.maxAge             = parameters["max_age"]
        self.partnerDetails     = parameters["partnerDetails"]
        self.edi_string         = edi.EDI_DETAILS.replace('{PartnerDetails}', self.partnerDetails)

    def generate(self):
        cl = Sponsor(self.cfg, self.SponserName, self.befinciaryPlanName)
        allSponsersSubscribersEDIString = ''
        for i in range(self.generateCount):
            sponsorEDIString = cl.edi_string()
            sub = Subscriber(cl, self.ploicyId, self.effectiveDate, self.minAge, self.maxAge)
            subscriberEDIString = sub.edi_string()
            dependentStringPresent = False
            if(self.addSpouse == "Yes"):
                # Spouse as a dependent
                dep = Dependent(sub, spouse = True)
                dependentEDIString = dep.edi_string()
                dependentStringPresent = True
            if(self.childrenCount > 0):
                for i in range(0, self.childrenCount):
                    if sub.age > 23:
                        dep = Dependent(sub)
                        if(dependentStringPresent):
                            dependentEDIString += dep.edi_string()
                        else:
                            dependentEDIString = dep.edi_string()
            if(self.childrenCount > 0 or self.addSpouse == "Yes"):
                subscriberEDIString = subscriberEDIString + dependentEDIString
            sponsorEDIString = sponsorEDIString.replace('{SUBSCRIBER_DETAILS}', subscriberEDIString)
            sponsorEDIString = sponsorEDIString.replace('{SECount}', str(len(sponsorEDIString.split('\n')) - 1))
            allSponsersSubscribersEDIString += sponsorEDIString
        GEEDIstring = self.edi_string.replace('{GECount}', str(self.generateCount))
        completeEDIString = GEEDIstring.replace('{SPONSOR_DETAILS}', allSponsersSubscribersEDIString)
        self.saveFile(completeEDIString)
        return None

    def saveFile(self, completeEDIString):
        filename = self.outputFilePath
        file = open(filename,"w")
        file.write(completeEDIString)
        suffix = "."
        finalMsg = "Successfully created edi file - {} for {} subscribers{}".format(filename, str(self.generateCount), suffix)
        print(finalMsg)
        return None
