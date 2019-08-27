import json
import re
from botocore.vendored import requests


SPARE_THE_AIR_URL = 'http://www.baaqmd.gov/Presentation/DotGov/Webservices/Widgets/AirQualityStatus.ashx?key=117c43da-3f15-453e-9a46-7d0bdb772241'


def get_burn_status():
    """
    Sample response:
    ({"Title":"SPARE THE AIR STATUS","AlertLink":"http://www.sparetheair.org/about/what-is-spare-the-air","AlertMode":"SummerWidgetNoAlertContent","AlertContent":"No Spare the Air Alert in Effect","Date":"Monday, 8/26","WidgetsLink":"http://www.baaqmd.gov/online-services/air-quality-widgets","WidgetsLinkDescription":"Air Quality Widgets"});
    """
    resp = requests.get(SPARE_THE_AIR_URL, headers={'Host': 'scooterbot.org'})
    matches = re.match(r'^\((.+)\);$', resp.text)
    if matches:
        json_data = json.loads(matches[1])
        message_text = json_data['AlertContent']
        if message_text.lower() == 'no spare the air alert in effect':
            return "It's OK to burn today"
        elif message_text.lower() == 'winter spare the air alert in effect':
            return "It's not legal to burn today"
    return "I don't know what to say"
