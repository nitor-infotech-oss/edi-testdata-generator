#ResponseCode = 'Y' - Subscriber, 'N' - Dependent
#SubscriberCode = '18' - Subscriber, 01 - Spouse, 19 - Child,
#MaintainceCode = keep "021" for now
#MaintainceReason = keep "AI" - No reason given
#StatusCode = "A" - Active(Default), "C" - Cobra
#MedicareStatusCode = Use "E" - No medicare
#EmployeeStatusCode = Use "FT" for Subscriber, "" - For dependents
#StudentStatusCode = Check if a member is student N, 'F', 'P'
DEPENDENT_DETAILS = '\nINS*{ResponseCode}*{SubscriberCode}*{MaintainceCode}*{MaintainceReason}*{StatusCode}*{MedicareStatusCode}**{EmployeeStatusCode}**{StudentStatusCode}~'
#This are same for all dependents
# SubscriberIdentifier = "10028XXXX", sample random
# PolicyNumber = "236XXXX", sample random
DEPENDENT_DETAILS += '\nREF*0F*{SubscriberIdentifier}~'
DEPENDENT_DETAILS += '\nREF*1L*{PolicyNumber}~'
#This are same for all dependents
# DTP303DATE - random date
DEPENDENT_DETAILS += '\nDTP*303*D8*{DTP303DATE}~'
#EntityId = 'IL' - for now
#EntityTypeQualifier = '1' for now
#IdentificationCodeQualifier = '34' fow now
#MemberIdentifier = '02972XXXX' random
DEPENDENT_DETAILS += '\nNM1*{EntityId}*{EntityTypeQualifier}*{FirstName}*{LastName}*{MiddleName}*{NamePrefix}**{IdentificationCodeQualifier}*{MemberIdentifier}~'
#CommunicationEmail = EmailID
#CommunicationNumber = random, 5083951382
DEPENDENT_DETAILS += '\nPER*IP**HP*{CommunicationNumber}~'
#This are same for all dependents
DEPENDENT_DETAILS += '\nN3*{AddressLine}~'
DEPENDENT_DETAILS += '\nN4*{City}*{State}*{PostalCode}~'

#Need Conditions, for example daughter birthdate cannot be before parents.
DEPENDENT_DETAILS += '\nDMG*D8*{BirthDate}*{Gender}*{MartialStatus}~'

# HealthCode = 'U' - use for now
DEPENDENT_DETAILS += '\nHLH*{HealthCode}~'
DEPENDENT_DETAILS += '\nHD*021**HLT~'
#HealthCoverageDate = '20191216' - random
DEPENDENT_DETAILS += '\nDTP*348*D8*{HealthCoverageDate}~'
#HealthCoveragePolicyNumber = 'XX1' - use for now
#HealthCoverageIdentifier = '033XXXX' - random
DEPENDENT_DETAILS += '\nREF*{HealthCoveragePolicyNumber}*{HealthCoverageIdentifier}~'
