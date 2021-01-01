# MiniProject-UsersDetails
# Aim

 With the help of reference url we need to get the users and their followers details
 
## Requests and Pandas

     Requests is a Python library  allows you to send HTTP requests using Python.
     
     Pandas is a Python package that provides fast, flexible, and expressive data structures designed to make working with structured (tabular, multidimensional, potentially heterogeneous) and time series data both easy and intuitive.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Requests & Pandas.

```
pip install requests
pip install pandas
```
## importing
In order to use the package we need to import the package in our python file
```
import requests
import pandas
```

## Usage

```python
import requests

requests.get('https://api.github.com/users') #get the data from the url
pandas.DataFrame([]) #to define the empty dataframe for saving the csv file
```
## working
```
base_url = 'https://api.github.com/users'
resp = requests.get(base_url)
data = resp.json()
df = pd.DataFrame([])
```
The above code shows that we get the data from the target url using requests pakage and stores it as a JSON format.
And to define the empty dataframe for saving the csv file
```
for user in data: #to store the data of 'data' in user variable
    if(user['id']%5 == 0):  #To get the list of users which are divisible by 5
 ```
 ```
 #To get a users details with the help of requests package by using the target url with passing user_login and stores it as JSON data
 user_name = requests.get('https://api.github.com/users/{}'.format(user['login'])).json()
 
 #To get a user's follower details with the help of requests package by using the target url with passing user_login and stores it as JSON data
 foll_details =  requests.get('https://api.github.com/users/{}/followers'.format(user['login'])).json()
 ```
 
 
 ```
  df = df.append(pd.DataFrame({'User ID': user['id'], 'User Login': user['login'], 'User Name': user_name['name'], 'Follower_Id': foll_details[i]['id'], 'Follower_Login':foll_details[i]['login'] }, index=[0]), ignore_index=True)
  df.to_csv("D:\user_details\output.csv",index = False)
  ```
  The above code is used to store the result in a csv file

