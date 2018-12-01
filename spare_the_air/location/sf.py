from datetime import datetime
from datetime import timedelta
from datetime import tzinfo
import re

from botocore.vendored import requests


def get_burn_status():
    resp = requests.get('http://www.sparetheair.org')
    html = resp.text
    message_html = re.search(r'<div[^>]+sta-day[^>]*>(.*?)<div[^>]+sta-day', html, re.DOTALL).group(1)
    matches = re.search(r'<div[^>]*>(.*?)</div>.*?<a [^>]*>(.*)</a>', message_html, re.DOTALL)
    now = datetime.now(PDT())
    message_date = datetime.strptime(matches.group(1) + '/' + str(now.year), '%A, %m/%d/%Y')

    message_text = remove_tags(matches.group(2))
    if message_text.lower() == 'no spare the air alert in effect':
        message_text = 'It\'s OK to burn'
    elif message_text.lower() == 'winter spare the air alert in effect':
        message_text = 'It\'s not legal to burn'

    if message_date.toordinal() == now.toordinal():
        message_text += ' today'
    else:
        message_text += ' for ' + message_date.strftime('%A, %B %-d')

    return message_text


class PDT(tzinfo):
    def utcoffset(self, dt):
        return timedelta(hours=-7)

    def tzname(self, dt):
        return "PDT"

    def dst(self, dt):
        return timedelta(hours=-7)


def remove_tags(text):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', text)).strip()
