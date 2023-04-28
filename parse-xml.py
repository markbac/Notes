import ast
import xml.etree.ElementTree as ET

import logging
import coloredlogs
import sys
import xmltodict
import pprint

logging.basicConfig()
logger = logging.getLogger(name='mylogger')

coloredlogs.install(logger=logger)
logger.propagate = False


coloredFormatter = coloredlogs.ColoredFormatter(
    fmt='[%(name)s] %(asctime)s %(funcName)s %(lineno)-3d  %(message)s',
    level_styles=dict(
        debug=dict(color='green'),
        info=dict(color='blue'),
        warning=dict(color='yellow', bright=True),
        error=dict(color='red', bold=True, bright=True),
        critical=dict(color='black', bold=True, background='red'),
    ),
    field_styles=dict(
        name=dict(color='magenta'),
        asctime=dict(color='cyan'),
        funcName=dict(color='white'),
        lineno=dict(color='magenta'),
    )
)

ch = logging.StreamHandler(stream=sys.stdout)
ch.setFormatter(fmt=coloredFormatter)
logger.addHandler(hdlr=ch)
logger.setLevel(level=logging.DEBUG)

#logger.debug(msg="this is a debug message")
#logger.info(msg="this is an info message")
#logger.warning(msg="this is a warning message")
#logger.error(msg="this is an error message")
#logger.critical(msg="this is a critical message")

tree = None 

pp = pprint.PrettyPrinter(indent=4)

xmlfile = "CEM-updatereport-ForecastProfileIntendedOperations.xml"

#open the file
fileptr = open(xmlfile,"r")


#read xml content from the file
xml_content= fileptr.read()

 
#change xml format to ordered dict
oadr_dict=xmltodict.parse(xml_content)


#Use contents of ordered dict to make python dictionary
oadrPayload= dict(oadr_dict['oadr:oadrPayload'])



oadrSignedObject = dict(oadrPayload['oadr:oadrSignedObject'])



oadrRegisterReport = dict(oadrSignedObject['oadr:oadrRegisterReport'])


oadrReport = dict(oadr_dict['oadr:oadrPayload']['oadr:oadrSignedObject']['oadr:oadrRegisterReport']['oadr:oadrReport'])

logger.debug ("xcal:date-time %s ", oadrReport['xcal:dstart']['xcal:date-time'])


#pp.pprint(interval)

eiReportID = oadrReport['ei:eiReportID']
reportRequestID = oadrReport['ei:reportRequestID']
reportSpecifierID = oadrReport['ei:reportSpecifierID']
reportName = oadrReport['ei:reportName']
createdDateTime = oadrReport['ei:createdDateTime']

logger.debug("eiReportID %s",eiReportID)
logger.debug("reportRequestID %s",reportRequestID)
logger.debug("reportSpecifierID %s",reportSpecifierID)
logger.debug("reportName %s",reportName)
logger.debug("createdDateTime %s",createdDateTime)

count = 1
for eiinterval in oadrReport['strm:intervals']['strm:interval']['ei:interval']:
    #pp.pprint(eiinterval)
    logger.debug("interval %d",count)
    
    if "xcal:dstart" in eiinterval:
        intervalStart = eiinterval['xcal:dstart']['xcal:date-time']
        logger.debug("\t intervalStart %s",intervalStart)
    
    duration = eiinterval['xcal:duration']['xcal:duration']
    logger.debug("\t duration %s",duration)
    
    oadrReportPayload =  dict(eiinterval['oadr:oadrReportPayload'])
    power = eiinterval['oadr:oadrReportPayload']['ei:payloadFloat']['ei:value']
    logger.debug("\t power %s",power)
    
    count += 1
