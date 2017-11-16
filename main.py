import requests

client_id = "a3e059563d7fd3372b49b37f00a00bcf"
iterations = 5


class SoundCloudUser:
    def __init__(self, username=None, id=None):
        if id != None:
            self.id = id
        else:
            self.username = username
            api = ("http://api.soundcloud.com/resolve?url=https://soundcloud.com/" + str(self.username) + "&client_id=" + client_id)
            r = requests.get(api)
            try:
                self.id = r.json()['id']
            except:
                print("Invalid Initial Username")
        
    def followerList(self):
        api = ("http://api.soundcloud.com/users/" + str(self.id) + "/followings?client_id=" + client_id)
        r =  requests.get(api)
        try:
            collection = r.json()['collection']
            return collection
        except:
            print("Invalid Response")
            
    def printData(self):
        api = ("http://api.soundcloud.com/users/" + str(self.id) + "?client_id=" + client_id)
        r = requests.get(api)    
        try:
            username = str(r.json()['username'])
            userId = str(r.json()['id'])
            desc = str(r.json()['description']).replace('\n', " ")
            follow_count = str(r.json()['followers_count'])
            url = str("https://soundcloud.com/" + str(r.json()['permalink']))
            
            print(username + " :: " + userId + " :: " + desc + " :: " + follow_count + " :: " + url)
        except:
            print("Invalid Response")
            

#main
user = SoundCloudUser("alex_shortt", None)
list = user.followerList()

for x in range(0, iterations):
    for val in list:
        follow_user = SoundCloudUser(None, val['id'])
        follow_user.printData()
    user = SoundCloudUser(None, list[0]['id'])
    list = user.followerList()