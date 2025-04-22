# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 22:43:28 2024

@author: 90530
"""


"""

ghp_123456789


github personal acccess token



"""

import requests

headers = {
    'Authorization': 'token ghp_123456789',
}





class Github:
    def __init__(self):
        self.api_url = "https://api.github.com"
        self.token = "ghp_123456789"
        
    def getUser(self, username):
        self.username = username
        response = requests.get(self.api_url + "/users/" + username)
        return response.json()
        
    def getRepositories(self, username):
        response = requests.get(self.api_url + '/users/' + username + '/repos')
        return response.json() #python yapısında kullanabileceğimiz bir sözlük yapısına çeviriliyor, json.loads gibi

    def createRepository(self,rname):
        response = requests.post(self.api_url + "/user/repos?access_token=" + self.token, json={
            "name": rname,
            "description": "deneme123",
            "homepage": "https:/github.com",
            "private": False,
            "has_issues": True,
            "has_projects": True,
            "has_wiki": True
            }, headers = headers) 
        return response.json()



github = Github()






while True:
    secim  = input("1- Find User\n2- Get repositories\n3- Create Trepository\n4- Exit\nSeçim: ")
    
    if secim == "4":
        break
    else:
        if secim == "1":
            
            username = input("username: ")
            result = github.getUser(username)
            print(result)
            print("+".center(50, "*"))
            print(f'name: {result["name"]} public repos: {result["public_repos"]} followers: {result["followers"]} ')            
            print("+".center(50, "*"))
            
            
        elif secim == "2":
            username = input("username: ")
            result = github.getRepositories(username)
            for repo in result:
                print(repo["name"])
                
            
        elif secim == "3":
            rname = input("New Repository Name: ")
            result = github.createRepository(rname)
            print(result)
        else:
            print("Yanlış bir seçim yaptınız")


