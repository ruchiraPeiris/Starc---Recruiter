import requests
import json




def count(repo,email,userName):

    comm_result = requests.get('https://api.github.com/repos/'+userName+'/'+repo+'/commits?client_id=2b010a4d4fce9da34253&client_secret=6ba2777c7086b32f9187ceeb8a2d43aeb5eded34')
    comm_data = json.loads(comm_result.content)
    count = 0
    for value in comm_data:
        if value['commit']['author']['email'] == email:
            count+=1

    return count

def findmax(email,userName):
    request_url = "https://api.github.com/users/" + userName + "/repos?client_id=2b010a4d4fce9da34253&client_secret=6ba2777c7086b32f9187ceeb8a2d43aeb5eded34"

    result = requests.get(request_url)
    repo_data = json.loads(result.content)

    max_commits = 0
    for item in repo_data:
        test = item['name']
        count2 = count(test,email,userName)
        if count2 > max_commits:
            max_commits = count2
            max_repo = item['name']
    print 'Maximum number of commits: '+max_commits.__str__()


    return max_repo

print 'Repository which has maximum commits: '+findmax('mohomedarshad1@gmail.com','ArshadFauzil')