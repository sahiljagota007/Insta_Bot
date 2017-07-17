from get_users_id import get_user_id
from constants import BASE_URL,APP_ACCESS_TOKEN
import requests
import urllib

comment_list = []
post_id_list = []

def most_commented_users_post(username) :
    user_id = get_user_id(username)
    request_url = (BASE_URL + "users/%s/media/recent/?access_token=%s" % (user_id, APP_ACCESS_TOKEN))
    #print("Get request url: " + request_url)
    user_info = requests.get(request_url).json()
    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            for temp in range(0,len(user_info['data'])) :
                post_id = user_info['data'][temp]['id']
                post_id_list.append(post_id)
                comment_count = user_info['data'][temp]['comments']['count']
                comment_list.append(comment_count)
            maximum = max(comment_list)
            print("No of comments for the post: %d"%(maximum))
            index = comment_list.index(maximum)
            post_index = post_id_list[index]
            print("Most commmented post-id: %s"%(post_index))
            image_name = 'userspost'+str(post_index)+'.jpg'
            image_url = user_info['data'][index]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)       #-----saving the user's latest post-----#
            print("Your image has been successfully saved..")
        else:
            print("No info exist")
    else:
        print("Incorrect code..")