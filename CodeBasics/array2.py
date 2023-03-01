heroes = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']


# 1. Length of the list
def length_of_list():
    return len(heroes)


# 2. Add 'black panther' at the end of this list
def add_black_panther_to_end():
    heroes.append('black panther')
    return heroes


# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
def add_black_panther():
    heroes.remove('black panther')
    heroes.insert(3, 'black panther')
    return heroes


# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
def remove_thor_hulk():
    heroes[1] = heroes[2] = 'doctor strange'
    heroes[1:3] = ['doctor strange']
    return heroes


# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
def sort_heroes():
    heroes.sort()
    return heroes


print('length_of_list', length_of_list())
print('add_black_panther_to_end', add_black_panther_to_end())
print('add_black_panther', add_black_panther())
print('remove_thor_hulk', remove_thor_hulk())
print('sort_heroes', sort_heroes())
