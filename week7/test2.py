import requests

crime_url_template = 'https://data.police.uk/api/crimes-street/all-crime?lat={lat}&lng={lng}&date={data}'

latitude = '51.52369'
longitude = '-0.0395857'
date = '2018-11'



crime_url = crime_url_template.format(lat = latitude, lng = longitude, data = date)

resp = requests.get(crime_url)

if resp.ok:
    crimes = resp.json()
    #print(crimes)
    #print("loop if")

else:
    print(resp.reason)
    print("loop else")




categories_url_template = 'https://data.police.uk/api/crime-categories?date={date}'

resp = requests.get(categories_url_template.format(date = date))

if resp.ok:
    categories_json = resp.json()
else:
    print(resp.reason)

categories = {categ["url"]:categ["name"] for categ in categories_json}

crime_category_stats = dict.fromkeys(categories.keys(), 0)
crime_category_stats.pop("all-crime")

for crime in crimes:
    crime_category_stats[crime["category"]] += 1

#print(crime_category_stats)




crime_outcome_stats = {'None':0}
for crime in crimes:
    outcome = crime["outcome_status"]
    if not outcome:
        crime_outcome_stats['None'] += 1
    elif outcome['category'] not in crime_outcome_stats.keys():
        crime_outcome_stats.update({outcome['category']:1})
    else:
        crime_outcome_stats[outcome['category']] += 1

print(crime_outcome_stats)
