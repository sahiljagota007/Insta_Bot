from constants import BASE_URL,APP_ACCESS_TOKEN
import requests

def get_user_id(insta_username):

    request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') %(insta_username, APP_ACCESS_TOKEN)
                                                  #searching friend
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            #print user_info['data'][0]['id']     #just to check
            return user_info['data'][0]['id']
        else:
            return None
    else:
        print 'Status code other than 200 received!'
        exit()