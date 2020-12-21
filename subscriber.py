import random
import datetime
from faker import Faker
from templates import subscriber as s
from address import Address
import dateutil.parser


class Subscriber():
    def __init__(self, sponsor, ploicyId, effectiveDate, minAge, maxAge):
        self.__classname__     = 'Subscriber'
        self.sponsor            = sponsor
        self.cfg               = sponsor.cfg
        self.utils             = sponsor.utils
        self.ploicyId          = ploicyId
        self.effectiveDate     = effectiveDate
        self.faker             = Faker()
        self.address           = Address()
        self.minAge            = minAge
        self.maxAge            = maxAge

    def set_values(self):

        EffectiveDate = dateutil.parser.parse(self.effectiveDate)
        self.ResponseCode                     = self.cfg.get_value("ResponseCode", "Subscriber")
        self.SubscriberCode                   = self.cfg.get_value("SubscriberCode", "Subscriber")
        self.MaintainceCode                   = self.cfg.get_value("MaintainceCode", "Subscriber")
        self.MaintainceReason                 = self.cfg.get_value("MaintainceReason", "Subscriber")
        self.StatusCode                       = self.cfg.get_value("StatusCode", "Subscriber")
        self.MedicareStatusCode               = self.cfg.get_value("MedicareStatusCode", "Subscriber")
        self.EmployeeStatusCode               = self.cfg.get_value("EmployeeStatusCode", "Subscriber")
        self.StudentStatusCode                = self.cfg.get_value("StudentStatusCode", "Subscriber")
        self.SubscriberIdentifier             = self.utils.series(9)
        self.PolicyNumber                     = self.ploicyId
        self.DTP303DATE                       = EffectiveDate.strftime("%Y%m%d")
        # self.effectiveDate.replace("-","") if self.effectiveDate else None
        # self.DTP303DATE                       = self.utils.date("%Y%m%d", 1, 10)
        self.EmploymentDate                   = self.utils.date("%Y%m%d", 1, 2)
        self.EntityId                         = self.cfg.get_value("EntityId", "Subscriber")
        self.EntityTypeQualifier              = self.cfg.get_value("EntityTypeQualifier", "Subscriber")
        self.HealthCode                       = self.cfg.get_value("HealthCode", "Subscriber")
        self.CoverageLeveCode                 = self.cfg.get_value("CoverageLeveCode", "Subscriber")
        self.IdentificationCodeQualifier      = self.cfg.get_value("IdentificationCodeQualifier", "Subscriber")
        self.MemberIdentifier                 = self.utils.series(9)
        self.HealthCoverageDate               = self.DTP303DATE
        # self.utils.date("%Y%m%d", 1, 2)

        # from datetime import datetime
        # self.HealthCoverageDate               = datetime.strptime(self.effectiveDate,'%Y-%m-%d').strftime("%Y%m%d")


        self.HealthCoveragePolicyNumber       = self.cfg.get_value("HealthCoveragePolicyNumber", "Subscriber")
        # self.HealthCoverageIdentifier         = self.utils.series(7, 'alphanum')
        self.HealthCoverageIdentifier         = '0003F'
        self.gender                           = ['male', 'female'][random.randrange(2)]
        self.age                              = random.randrange(self.minAge, self.maxAge)
        self.LastName                         = self.faker.last_name()
        self.FirstName                        = self.faker.first_name()
        self.MiddleName                       = self.faker.first_name()
        self.CommunicationNumber              = self.faker.msisdn()
        self.CommunicationEmail               = self.faker.free_email()
        self.addressRow                       = self.address.get_address_row()
        self.AddressLine                      = self.addressRow['AddressLine']
        self.City                             = self.addressRow['City']
        self.State                            = self.addressRow['State']
        self.PostalCode                       = self.addressRow['Zip']
        self.BirthDate                        = self.utils.date("%Y%m%d", self.age, self.age+1)
        self.Gender                           = self.gender[0].upper()
        # Harcoded for now, need to double check
        self.MartialStatus = 'M'
        self.NamePrefix                       = ''

    def edi_string(self):
        ediString = s.SUBSCRIBER_DETAILS
        self.set_values()
        variableValues = self.__dict__
        ediString = self.utils.class_to_edi_string(variableValues, ediString)
        return ediString

    def edi_string(self):
        ediString = s.SUBSCRIBER_DETAILS
        self.set_values()
        variableValues = self.__dict__
        ediString = self.utils.class_to_edi_string(variableValues, ediString)
        return ediString
