import requests

import pandas as pd
base_url = 'https://api.github.com/users'
resp = requests.get(base_url)
data = resp.json()#to get a value in a json format
df = pd.DataFrame([])


for user in data:#to store the data of 'data' in user variable
    if(user['id']%5 == 0):#To get the list of users which are divisible by 5
        user_name = requests.get('https://api.github.com/users/{}'.format(user['login'])).json()
        foll_details =  requests.get('https://api.github.com/users/{}/followers'.format(user['login'])).json()
        list=len(foll_details)
        for i in range(list):
            print(user['id'],user['login'],user_name['name'],foll_details[i]['id'],foll_details[i]['login'])
            df = df.append(pd.DataFrame({'User ID': user['id'], 'User Login': user['login'], 'User Name': user_name['name'], 'Follower_Id': foll_details[i]['id'], 'Follower_Login':foll_details[i]['login'] }, index=[0]), ignore_index=True)
            df.to_csv("D:\user_details\output.csv",index = False)
