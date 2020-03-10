
import urllib, json
from math import sin, cos, sqrt, atan2, radians
import unittest

# convert json to python object
json_users = urllib.urlopen('https://jsonplaceholder.typicode.com/users')
json_posts = urllib.urlopen('https://jsonplaceholder.typicode.com/posts')
data_users = json.loads(json_users.read())
data_posts = json.loads(json_posts.read())

# convert users to dictionary
users_dict = {}
for user in data_users:
   id_num = user['id']
   users_dict[id_num] = user

# merge users dictionary with posts
for post in data_posts:
    user_id = post['userId']
    post['user'] = users_dict[user_id]
# print(json.dumps(data_posts, indent=4, sort_keys=True))

# count number of posts posted by user
posts_counter = {}
for post in data_posts:
   if 'userId' in post:
       posts_counter[post['user']['username']] = posts_counter.get(post['user']['username'], 0) + 1

# print list "user_name napisal(a) count postow"
count_list = []
for key, value in posts_counter.items():
    count_list.append(str(key) + ' napisal(a) ' + str(value) + ' postow')

# check if post title is unique
duplicates = {}
for post in data_posts:
    if 'title' in post:
        duplicates[post['title']] = duplicates.get(post['title'], 0) + 1

duplicates_list = []
for key, value in duplicates.items():
    if value > 1:
        duplicates_list.append(str(key))

# count distance
def count_distance(lat1, lng1, lat2, lng2):
    R = 6373.0
    lat1 = radians(lat1)
    lng1 = radians(lng1)
    lat2 = radians(lat2)
    lng2 = radians(lng2)
    dlat = lat2 - lat1
    dlng = lng2 - lng1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlng / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return int(distance)


# Test all tasks
class Test(unittest.TestCase):
    
    def test_posts_counter(self):
        self.assertDictEqual(posts_counter, {u'Maxime_Nienow': 10, u'Kamren': 10, u'Leopoldo_Corkery': 10, u'Samantha': 10, u'Karianne': 10, u'Delphine': 10, u'Moriah.Stanton': 10, u'Elwyn.Skiles': 10, u'Bret': 10, u'Antonette': 10})

    def test_count_list(self):
        self.assertListEqual(count_list, ['Maxime_Nienow napisal(a) 10 postow', 'Kamren napisal(a) 10 postow', 'Leopoldo_Corkery napisal(a) 10 postow', 'Samantha napisal(a) 10 postow', 'Karianne napisal(a) 10 postow', 'Delphine napisal(a) 10 postow', 'Moriah.Stanton napisal(a) 10 postow', 'Elwyn.Skiles napisal(a) 10 postow', 'Bret napisal(a) 10 postow', 'Antonette napisal(a) 10 postow'])

    def test_duplicates_list(self):
        self.assertListEqual(duplicates_list, [])

    def test_distance(self):
        self.assertEqual(count_distance(50.06143, 19.93658, 52.22977, 21.01178), 252) # Krakow - Warszawa
        self.assertEqual(count_distance(50.06143, 19.93658, -33.86785, 151.20732), 15701) # Krakow - Sydney

if __name__ == '__main__':
    unittest.main()
