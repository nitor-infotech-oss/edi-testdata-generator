import datetime
import random
from templates import dependent as d

class Dependent():
    def __init__(self, subscriber, spouse=False):
        self.__classname__     = 'Dependent'
        self.isSpouse          = spouse
        self.subscriber        = subscriber
        self.utils             = subscriber.utils
        self.cfg               = subscriber.cfg
        self.faker             = subscriber.faker

    def set_values(self):
        self.ResponseCode                     = 'N'
        self.SubscriberCode                   = '01' if (self.isSpouse) else '19'
        self.MaintainceCode                   = self.subscriber.MaintainceCode
        self.MaintainceReason                 = self.subscriber.MaintainceReason
        self.StatusCode                       = self.subscriber.StatusCode
        self.MedicareStatusCode               = self.subscriber.MedicareStatusCode
        self.EmployeeStatusCode               = ""
        self.StudentStatusCode                = 'N'
        self.SubscriberIdentifier             = self.subscriber.SubscriberIdentifier
        self.PolicyNumber                     = self.subscriber.PolicyNumber
        self.DTP303DATE                       = self.subscriber.DTP303DATE
        self.EntityId                         = self.subscriber.EntityId
        self.EntityTypeQualifier              = self.subscriber.EntityTypeQualifier
        self.HealthCode                       = self.subscriber.HealthCode
        self.IdentificationCodeQualifier      = self.subscriber.IdentificationCodeQualifier
        self.MemberIdentifier                 = self.utils.series(9)
        self.HealthCoverageDate               = self.subscriber.HealthCoverageDate
        self.HealthCoveragePolicyNumber       = self.cfg.get_value("HealthCoveragePolicyNumber", "Subscriber")
        self.HealthCoverageIdentifier         = '0003F'
        self.gender                           = ['male', 'female'][random.randrange(2)]
        self.age                              = random.randrange(26, 70)
        self.LastName                         = self.subscriber.LastName
        self.MiddleName                       = ''
        self.CommunicationNumber              = self.faker.msisdn()
        self.CommunicationEmail               = self.faker.free_email()
        self.AddressLine                      = self.subscriber.AddressLine
        self.City                             = self.subscriber.City
        self.State                            = self.subscriber.State
        self.PostalCode                       = self.subscriber.PostalCode
        # Harcoded for now, need to double check
        self.MartialStatus  = 'M'
        if (self.isSpouse and self.subscriber.gender == 'male'):
            self.gender     = 'female'
            self.Gender     = self.gender[0].upper()
        if (self.isSpouse and self.subscriber.gender == 'female'):
            self.gender     = 'male'
        if (not self.isSpouse):
            self.age        = random.randrange(1, self.subscriber.age - 23)
        if (self.gender == 'male'):
            self.NamePrefix = 'Mr' if (self.isSpouse) else ""
            self.FirstName  = self.faker.first_name_male()
        else:
            self.NamePrefix = 'Mrs' if (self.isSpouse) else ""
            self.FirstName  = self.faker.first_name_female()
        self.Gender     = self.gender[0].upper()
        self.BirthDate  = self.utils.date("%Y%m%d", self.age, self.age+1)

    def edi_string(self):
        ediString = d.DEPENDENT_DETAILS
        self.set_values()
        variableValues = self.__dict__
        ediString = self.utils.class_to_edi_string(variableValues, ediString)
        return ediString
