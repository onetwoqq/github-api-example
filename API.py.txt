import requests

response = requests.get('https://api.github.com/repos/octocat/Hello-World/stats/contributors')
print(response.json())