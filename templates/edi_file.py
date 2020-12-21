#Constant For Now
EDI_DETAILS = 'ISA*00*          *00*          *ZZ*{PartnerDetails}       *ZZ*PARTNERSXXX            *200108*0904*^*00501*000000279*0*T*:~'
#Constant Need confirmation
EDI_DETAILS += '\nGS*BE*{PartnerDetails}*PARTNERSXXX*20200108*0904*1*X*005010X220A1~'

EDI_DETAILS += '{SPONSOR_DETAILS}'
EDI_DETAILS += '''\nGE*{GECount}*1~\nIEA*1*000000279~'''
