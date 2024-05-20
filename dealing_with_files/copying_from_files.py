"""
Start with a list of names in friends.txt
Get user input of three names
If user input name matches list of friend, write to nearby_friends.txt
"""

friends_txt = r"C:\Development\my_python_bible\dealing_with_files\friends.txt"
friends_nearby_txt = r"C:\Development\my_python_bible\dealing_with_files\friends_nearby.txt"


my_friends = open(friends_txt, 'r')
friends_content = my_friends.read().splitlines()
friends_content_set = set(friends_content)
my_friends.close()


friends_nearby_input = input('Entre three friends seperated by commas (no spaces please):').split(',')
friends_nearby_set = set(friends_nearby_input)


friends_intersection = friends_nearby_set.intersection(friends_content_set)


my_file_writing = open(friends_nearby_txt, 'w') 
for friend in friends_intersection:
    my_file_writing.write(f"{friend}\n")
my_file_writing.close()

