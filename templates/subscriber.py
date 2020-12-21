#ResponseCode = 'Y' - Subscriber, 'N' - Dependent
#SubscriberCode = '18' - Subscriber, 01 - Spouse, 19 - Child,
#MaintainceCode = keep "021" for now
#MaintainceReason = keep "AI" - No reason given
#StatusCode = "A" - Active(Default), "C" - Cobra
#MedicareStatusCode = Use "E" - No medicare
#EmployeeStatusCode = Use "FT" for Subscriber, "" - For dependents
#StudentStatusCode = Check if a member is student N, 'F', 'P'
SUBSCRIBER_DETAILS = '\nINS*{ResponseCode}*{SubscriberCode}*{MaintainceCode}*{MaintainceReason}*{StatusCode}*{MedicareStatusCode}**{EmployeeStatusCode}**{StudentStatusCode}~'

#This are same for all dependents
# SubscriberIdentifier = "100283XXX", sample random
# PolicyNumber = "2361XXX", sample random
SUBSCRIBER_DETAILS += '\nREF*0F*{SubscriberIdentifier}~'
SUBSCRIBER_DETAILS += '\nREF*1L*{PolicyNumber}~'

#This are same for all dependents
# DTP303DATE - random date
SUBSCRIBER_DETAILS += '\nDTP*303*D8*{DTP303DATE}~'
#EmploymentDate - only for subscriber
# EmploymentDate - random NearBy date
#EmploymentDate - only for subscriber
SUBSCRIBER_DETAILS += '\nDTP*336*D8*{EmploymentDate}~'

#EntityId = 'IL' - for now
#EntityTypeQualifier = '1' for now
#IdentificationCodeQualifier = '34' fow now
#MemberIdentifier = '029724XXX' random
SUBSCRIBER_DETAILS += '\nNM1*{EntityId}*{EntityTypeQualifier}*{FirstName}*{LastName}*{MiddleName}*{NamePrefix}**{IdentificationCodeQualifier}*{MemberIdentifier}~'

#CommunicationEmail = EmailID
#CommunicationNumber = random, 508395XXXX
SUBSCRIBER_DETAILS += '\nPER*IP**HP*{CommunicationNumber}*EM*{CommunicationEmail}~'

#This are same for all dependents
SUBSCRIBER_DETAILS += '\nN3*{AddressLine}~'
SUBSCRIBER_DETAILS += '\nN4*{City}*{State}*{PostalCode}~'

#Need Conditions, for example daughter birthdate cannot be before parents.
SUBSCRIBER_DETAILS += '\nDMG*D8*{BirthDate}*{Gender}*{MartialStatus}~'

# Only for subscriber keep as is
SUBSCRIBER_DETAILS += '\nEC*08~'

# HealthCode = 'U' - use for now
SUBSCRIBER_DETAILS += '\nHLH*{HealthCode}~'

# CoverageLeveCode - E5D - One or more dependent
SUBSCRIBER_DETAILS += '\nHD*021**HLT**{CoverageLeveCode}~'

#HealthCoverageDate = '2019XXXX' - random
SUBSCRIBER_DETAILS += '\nDTP*348*D8*{HealthCoverageDate}~'

#HealthCoveragePolicyNumber = 'XX1' - use for now
#HealthCoverageIdentifier = '0333XXX' - random
SUBSCRIBER_DETAILS += '\nREF*{HealthCoveragePolicyNumber}*{HealthCoverageIdentifier}~'
