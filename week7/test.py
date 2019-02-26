import requests

crime_url_template = 'https://data.police.uk/api/crimes-street/all-crime?lat={lat}&lng={lng}&date={data}'

latitude = '51.52369'
longitude = '-0.0395857'
date = '2018-11'

crime_url = crime_url_template.format(lat = latitude, lng = longitude, data = date)

resp = requests.get(crime_url)

if resp.ok:
    crimes = resp.json()
    print(crimes)
    print("loop if")

else:
    print(resp.reason)
    print("loop else")
