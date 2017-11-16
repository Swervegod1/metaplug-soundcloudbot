#import libraries
import urllib
import soundcloud
import requests
from bs4 import BeautifulSoup

#quote_page = 'https://soundcloud.com/regardscoupables'
#page = urllib.urlopen(quote_page)
#soup = BeautifulSoup(page, 'html.parser')
#print(soup)
#name_box = soup.find('div', attrs={'class' : 'truncatedUserDescription__content'})
#name = name_box.text.strip() #strip() removes starting and trailing tags
#print(name)

client_id = "a3e059563d7fd3372b49b37f00a00bcf"
#client = soundcloud.Client(client_id)

class SoundCloudUser:
    def __init__(self, id):
        self.id = id
        
    def followerList(self):
        api = ("http://api.soundcloud.com/users/" + str(self.id) + "/followings?client_id=" + client_id)
        r =  requests.get(api)
        try:
            collection = r.json()['collection']
            for val in collection:
                print(val['id'])
        except:
            print("Invalid Response")
            
    def getData(self):
        api = ("http://api.soundcloud.com/users/" + str(self.id) + "?client_id=" + client_id)
        r = requests.get(api)    
        try:
            username = r.json()['username']
            userId = r.json()['id']
            desc = r.json()['description']
            follow_count = r.json()['followers_count']
            url = "https://soundcloud.com/" + str(r.json()['permalink'])
            
            print("Username: " + str(username))
            print("User ID: " + str(userId))
            print("Description: " + str(desc))
            print("Followers: " + str(follow_count))
            print("Url: " + str(url))
        except:
            print("Invalid Response")
            

#main
user = SoundCloudUser(1433)
user.followerList()