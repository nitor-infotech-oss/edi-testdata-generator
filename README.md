# edi-generator


##### What is EDI?

Electronic Data Interchange (EDI) is the automated transfer of data between a care provider and a payer. Using EDI allows payers and care providers to send and receive information faster, often at a lower cost.

##### About edi-testdata-generator?
Python based EDI test data generator framework provides the ability to create edi files with test data and accelerate QA processes of data transfer between care provider and payer.


## Prerequisites:
    1. Python 3.6
    2. pip
    3. Create and activate virtualenv

## Steps to import package:
    1. git clone https://github.com/nitor-infotech-oss/edi-testdata-generator.git
    2. cd edi-testdata-generator
    3. pip install -r requirements.txt


#### How to use
```
#import package
from edi_generator import EDIGenerator

#create a dictionary with required parameters
params = {
    "sponsorName": "Sponsor XXX",
    "ploicyId": "201029XXXX",
    "befinciaryPlanName": "XXX20190290",
    "outputFilePath": './outputs/edi_testfile',
    "spouse": true,
    "childrenCount": 2,
    "effectiveDate": "01-01-2020",
    "count": 2,
    "min_age": 5,
    "max_age": 60,
    "partnerDetails": "Partner XXX"
}

#initialize class
edi = EDIGenerator(params)

#call generate method to create edi file with test data
edi.generate()
```
