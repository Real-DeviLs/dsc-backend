import requests
from time import time

def checkCodechefSubmission(username, problem_link):

    # Calculates contest ID and index from given link

    prb_link = problem_link.split('/')
    prb_link= prb_link[-3:]

    INDEX = prb_link[-1]

    if prb_link[-3].isdigit():
        CONTEST_ID = prb_link[-3]
    else:
        CONTEST_ID = prb_link[-2]


    apiUrl = "https://codeforces.com/api/user.status"

    parameters = {"handle": username,
                   "from":1,
                   'count':1000
                }

    try:
        res = requests.get(url=apiUrl, params=parameters, timeout=100)

        res = res.json()

        if(res['status'] == 'OK'):

            data = res['result']

            # Checks each submission made

            for i in range(len(data)):

                # Checks if the submission was made in last 24 hours

                if "creationTimeSeconds" in data[i]:
                    if time() - data[i]["creationTimeSeconds"] > 86400:
                        print('Not submitted in last 24 hrs')
                        return False

                contest_id = str(data[i]["problem"]["contestId"])
                idx = data[i]["problem"]["index"]

                if(data[i]["verdict"] == 'OK') and contest_id == CONTEST_ID and idx == INDEX:
                    return True
             
            return False
                    
    except requests.exceptions.RequestException as error:
        print(error)


# username = input()
# username = 'namans777'
# problem_link = input()
# problem_link = 'https://codeforces.com/contest/1613/problem/B'

# initial = time()
# print(checkCodechefSubmission(username, problem_link))
# print(time()- initial)

# Input Format-
# Enter CodeForces Username
# Paste question link