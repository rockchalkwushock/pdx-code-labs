import requests

headers = {
    "authorization": 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI1Mlc5R1MiLCJhdWQiOiIyMkQzSDQiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJhY3QgcnNldCBybG9jIHJ3ZWkgcmhyIHJwcm8gcm51dCByc2xlIiwiZXhwIjoxNTMwNjQ3NjE5LCJpYXQiOjE1MzAwNDI4MTl9.1NzMhp-GVItHFOXTBtGaDit9WHhTfFcxZy5YxGzKY_E'
}

r = requests.get(
    'https://api.fitbit.com/1/user/52W9GS/activities/date/2018-06-26.json', headers=headers)

# print(r.url)
# print(r.status_code)
response = r.json()
steps = response['summary']['steps']
fat_burn = response['summary']['heartRateZones'][1]['caloriesOut']

print(
    f'Current Steps: {steps}.\nCalories burned in Fat Burn zone: {round(fat_burn, 2)}.')

# {'activities': [],
#  'goals': {
#     'activeMinutes': 30,
#     'caloriesOut': 2978,
#     'distance': 8.05,
#     'floors': 10,
#     'steps': 10000
# },
#     'summary': {
#     'activeScore': -1,
#     'activityCalories': 198,
#     'caloriesBMR': 946,
#     'caloriesOut': 1106,
#     'distances': [
#         {'activity': 'total', 'distance': 1.22},
#         {'activity': 'tracker', 'distance': 1.22},
#         {'activity': 'loggedActivities', 'distance': 0},
#         {'activity': 'veryActive', 'distance': 0},
#         {'activity': 'moderatelyActive', 'distance': 0},
#         {'activity': 'lightlyActive', 'distance': 1.22},
#         {'activity': 'sedentaryActive', 'distance': 0}
#     ],
#     'elevation': 12.19,
#     'fairlyActiveMinutes': 0,
#     'floors': 4,
#     'heartRateZones': [
#         {'caloriesOut': 479.99493, 'max': 95, 'min': 30, 'minutes': 303, 'name': 'Out of Range'},
#         {'caloriesOut': 52.49004, 'max': 133, 'min': 95, 'minutes': 8, 'name': 'Fat Burn'},
#         {'caloriesOut': 0, 'max': 161, 'min': 133, 'minutes': 0, 'name': 'Cardio'},
#         {'caloriesOut': 0, 'max': 220, 'min': 161, 'minutes': 0, 'name': 'Peak'}
#     ],
#     'lightlyActiveMinutes': 41,
#     'marginalCalories': 118,
#     'restingHeartRate': 60,
#     'sedentaryMinutes': 745,
#     'steps': 1656,
#     'veryActiveMinutes': 0
# }
# }
