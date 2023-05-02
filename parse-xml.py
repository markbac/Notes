import xml.etree.ElementTree as ET
import csv
import logging
import coloredlogs
import sys
import xmltodict
import pprint

logging.basicConfig()
logger = logging.getLogger(name='mylogger')

coloredlogs.install(logger=logger)
logger.propagate = False

def duration_to_seconds(duration):
    components = duration[2:].split('T')  # split duration into date and time components

    
    time_components = components[0] if len(components) >= 1 else ''  # extract time component
    days = components[0].split('D')[0] if 'D' in components[0] else '0'  # extract days component
    hours = time_components.split('H')[0] if 'H' in time_components else '0'  # extract hours component
    minutes = time_components.split('M')[0].split('H')[-1] if 'M' in time_components else '0'  # extract minutes component
    seconds = time_components.split('S')[0].split('M')[-1] if 'S' in time_components else '0'  # extract seconds component
    total_seconds = (int(days) * 86400) + (int(hours) * 3600) + (int(minutes) * 60) + int(seconds)  # calculate total seconds
    return total_seconds


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

xmlfile = "oaddr2.xml"

#open the file
fileptr = open(xmlfile,"r")


#read xml content from the file
xml_content= fileptr.read()

 
#change xml format to ordered dict
oadr_dict=xmltodict.parse(xml_content)


#Use contents of ordered dict to make python dictionary
oadrPayload= dict(oadr_dict['oadr:oadrPayload'])

oadrSignedObject = dict(oadrPayload['oadr:oadrSignedObject'])



if 'oadr:oadrRegisterReport' in oadr_dict['oadr:oadrPayload']['oadr:oadrSignedObject']:
    oadrReport = dict(oadr_dict['oadr:oadrPayload']['oadr:oadrSignedObject']['oadr:oadrRegisterReport']['oadr:oadrReport'])


if 'oadr:oadrUpdateReport' in oadr_dict['oadr:oadrPayload']['oadr:oadrSignedObject']:
    oadrReport = dict(oadr_dict['oadr:oadrPayload']['oadr:oadrSignedObject']['oadr:oadrUpdateReport']['oadr:oadrReport'])

pp.pprint(oadrReport['xcal:dtstart'])


intervalStart = oadrReport['xcal:dtstart']['xcal:date-time']

eiReportID = oadrReport['ei:eiReportID']
reportRequestID = oadrReport['ei:reportRequestID']
reportSpecifierID = oadrReport['ei:reportSpecifierID']
reportName = oadrReport['ei:reportName']
createdDateTime = oadrReport['ei:createdDateTime']

logger.debug (eiReportID)


filename = eiReportID.replace(":","-").replace("; ","_")


print(filename) # Output: "order-LD_frc-1_intervals-4_esa_id-ESA#1"

with open(f"{filename}.csv", mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["start_time", "duration", "power", "interruptible"])

    count = 1
    for eiinterval in oadrReport['strm:intervals']['ei:interval']:
        #pp.pprint(eiinterval)
        interruptible = 'true'
        logger.debug("interval %d",count)
        
        if "xcal:dstart" in eiinterval:
            intervalStart = eiinterval['xcal:dstart']['xcal:date-time']
            logger.debug("\t intervalStart %s",intervalStart)
        
        duration = eiinterval['xcal:duration']['xcal:duration']
        duration = duration_to_seconds(duration)
        logger.debug("\t duration %s",duration)
        
        oadrReportPayload =  dict(eiinterval['oadr:oadrReportPayload'])
        power = eiinterval['oadr:oadrReportPayload']['ei:payloadFloat']['ei:value']
        logger.debug("\t power %s",power)
        
        writer.writerow([intervalStart, duration, power, interruptible])

        count += 1
        intervalStart = ''
