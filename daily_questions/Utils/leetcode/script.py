import requests

# data.matchedUser.submitStats.acSubmissionNum[0].count

query = """{ matchedUser(username: "hartiksalaria") {
    username
    submitStats: submitStatsGlobal {
        acSubmissionNum {
            difficulty
            count
            submissions
            }
        }
    }
}"""

url = 'https://leetcode.com/graphql'
r = requests.post(url, json={'query': query})
print(r.text)
print(r.status_code)