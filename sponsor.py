import datetime
from utilities import Utilites
from templates import sponsor as sd

class Sponsor():
    def __init__(self, cfg, SponserName, befinciaryPlanName):
        self.__classname__      = 'Sponsor'
        self.cfg                = cfg
        self.utils              = Utilites()
        self.SponserName        = SponserName
        self.befinciaryPlanName = befinciaryPlanName

    def set_values(self):
        self.FileType = 834
        self.TransactionControlNumber        = self.cfg.get_value("TransactionControlNumber", "Sponser")
        self.ImplentationConventionReference = self.cfg.get_value("ImplentationConventionReference", "Sponser")
        self.PurposeCode                     = self.cfg.get_value("PurposeCode", "Sponser")
        self.ReferenceID                     = self.befinciaryPlanName
        self.TimeZone                        = self.cfg.get_value("TimeZone", "Sponser")
        self.CreationDate                    = self.utils.date("%Y%m%d", 1, 10)
        self.CreationTime                    = self.utils.time("%H%M")
        self.ActionCode                      = self.cfg.get_value("ActionCode", "Sponser")
        self.MasterPolicyNumber              = self.cfg.get_value("MasterPolicyNumber", "Sponser")
        self.ReferenceIDNumber               = self.cfg.get_value("ReferenceIDNumber", "Sponser")
        self.DTPFileDate                     = self.utils.date("%Y%m%d", 1, 2)
        self.SponserName                     = self.SponserName
        self.EmployerIdentificationCode      = self.cfg.get_value("EmployerIdentificationCode", "Sponser")
        self.IdentificationCode              = self.cfg.get_value("IdentificationCode", "Sponser")
        self.InsuarerName                    = self.cfg.get_value("InsuarerName", "Sponser")
        self.EmployerRandIDNumbers           = self.utils.series(9)
        self.RandIDNumbers                   = self.utils.series(9)

    def edi_string(self):
        ediString = sd.SPONSOR_DETAILS
        self.set_values()
        variableValues = self.__dict__
        ediString = self.utils.class_to_edi_string(variableValues, ediString)
        return ediString
