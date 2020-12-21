#FileType - 834, eligibility
#           837, claim
    #TransactionControlNumber - Keep 0001 for now
#ImplentationConventionReference = Keep '005010X220A1' for now
SPONSOR_DETAILS = '\nST*{FileType}*{TransactionControlNumber}*{ImplentationConventionReference}~'

#PurposeCode - Keep 00
#ReferenceID = 'XXX 00000XXXX 0001'
#CreationDate = Any Date (%Y%m%d), check if it has to be a past date
#CreationTime = Any Time ("%H%M")
#TimeZone = Keep "ES", can be changed later
#ActionCode = Keep "2" for now
SPONSOR_DETAILS += '\nBGN*{PurposeCode}*{ReferenceID}*{CreationDate}*{CreationTime}*{TimeZone}***{ActionCode}~'

# MasterPolicyNumber = From System, keep 38 for now
# ReferenceIDNumber = '99154XXXX', Might be from system, need to confirm
SPONSOR_DETAILS += '\nREF*{MasterPolicyNumber}*{ReferenceIDNumber}~'

# FileDateCode = 007 and 382, use in succession
# FileDateFormat = Use D8 ""
# DTPFileDate = Use same date for both rows
SPONSOR_DETAILS += '\nDTP*007*D8*{DTPFileDate}~'
SPONSOR_DETAILS += '\nDTP*382*D8*{DTPFileDate}~'

#SponserName = From SYstem, use "BWPO"
#InsuarerName = From SYstem, use "Allways Health PARTNERS"
#IdentificationCode = '24' - By Employer
                     # '94' - By Organization
                     # 'FI' - Federal
#RandIDNumbers = "123456789", random 9 digit numbers
SPONSOR_DETAILS += '\nN1*P5*{SponserName}*{EmployerIdentificationCode}*{EmployerRandIDNumbers}~'
SPONSOR_DETAILS += '\nN1*IN*{InsuarerName}*{IdentificationCode}*{RandIDNumbers}~'

SPONSOR_DETAILS += '{SUBSCRIBER_DETAILS}'
SPONSOR_DETAILS += '''\nSE*{SECount}*0001~'''
