from constants import BASE_URL,APP_ACCESS_TOKEN
import requests
import urllib

def get_own_post():
    request_url = (BASE_URL + 'users/self/media/recent/?access_token=%s') % (APP_ACCESS_TOKEN)
                                                # getting post_id(same usrl like get_own_post_id)
                                                # or i can call get_own_post_id function also.
    own_media = requests.get(request_url).json()

    if own_media['meta']['code'] == 200:
        if len(own_media['data']):
            #print own_media['data'][0]['id']                          # extract post ID
            #print own_media['data'][0]['comments']['counts']          #for comments
            #return own_media['data'][0]['id']

            #image_name = own_media['data'][0]['id'] + '.jpeg'

            image_name = 'mypic.jpeg'       #image name can be my choice
            image_url  = own_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print 'Your image has been downloaded!'

        else:
            print 'Post does not exist!'
    else:
        print "Status code other than 200 received!"