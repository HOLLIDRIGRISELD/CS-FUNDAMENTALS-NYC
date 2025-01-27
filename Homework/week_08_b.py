#Use the Bored API https://bored.api.lewagon.com/api/activity/  and suggest a
#random activity for person who cannot decide what to do with their spare time. Extract and
#display the “activity” element.

import requests

#get a random activity from the Bored API
response = requests.get("https://bored.api.lewagon.com/api/activity/")
data = response.json()
print(f"Random Activity Suggestion: {data['activity']}")    
