from constants import BASE_URL,APP_ACCESS_TOKEN
import requests

def get_own_post_id():
    request_url = (BASE_URL + 'users/self/media/recent/?access_token=%s') % (APP_ACCESS_TOKEN)
    #print 'GET request url : %s' % (request_url)
    own_media = requests.get(request_url).json()

    if own_media['meta']['code'] == 200:
        if len(own_media['data']):
           # print own_media['data'][0]['id']   #my recent post_id
            return own_media['data'][0]['id']
        else:
            print 'Post does not exist!'
    else:
        print "Status code other than 200 received!"
