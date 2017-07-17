import requests
from constants import BASE_URL, APP_ACCESS_TOKEN

#self_info() fun starts
def self_info():
    requests_url = (BASE_URL + 'users/self/?access_token=%s') % (APP_ACCESS_TOKEN)
    # print 'GET Request url : %s' % (requests_url)
    user_info =requests.get(requests_url).json()
    #print user_info                               #just for checking

    if user_info['meta']['code']== 200:
        if len(user_info['data']):
            print 'username                       : %s' %(user_info['data']['username'])
            print 'No. of followers               : %s' %(user_info['data']['counts']['followed_by'])
            print 'No. of people you are following: %s' %(user_info['data']['counts']['follows'])
            print 'No. of posts                   : %s' % (user_info['data']['counts']['media'])
        else:
            print 'User does not exist.'

    else:
        print 'Status code other than 200 received'

#self_info() fun ends.