from requests import get
from datetime import datetime


def fetch_users():
    r = get('http://api.randomuser.me/?results=5')
    res = r.json()
    users = res["results"]
    for user in users:
        r_date = datetime.strptime(
            user['registered']['date'], "%Y-%m-%dT%H:%M:%SZ")
        b_date = datetime.strptime(
            user['dob']['date'], "%Y-%m-%dT%H:%M:%SZ")
        print(
            f'Name: {user["name"]["title"].capitalize()} {user["name"]["first"].capitalize()} {user["name"]["last"].capitalize()}')
        print(f'Email: {user["email"]}')
        print(f'Username: {user["login"]["username"]}')
        print(f'Registration Date: {r_date.month}/{r_date.day}/{r_date.year}')
        print(f'Birth Date: {b_date.month}/{b_date.day}/{b_date.year}')
        print()


fetch_users()
