from constants import  BASE_URL,APP_ACCESS_TOKEN
import requests
import urllib                   #library helping download images

def get_my_recent_liked_post():
    request_url = (BASE_URL + 'users/self/media/liked?access_token=%s') % (APP_ACCESS_TOKEN)
    #print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()

    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            image_name = "myLikedPost.jpg"
            image_url  = user_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print 'Your image has been downloaded named as %s' % (image_name)

        else:
            print 'Post does not exist!'
    else:
        print "Status code other than 200 received!"
