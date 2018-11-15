some_str = 'some text with value %s' % 'my_value'
print(some_str)
some_str = 'some text with values %d %s, %d : %s' % (42, 'stringa', 25, 'ddd')
print(some_str)


some_str = 'some text with value {}'.format('my_value')
some_str = 'some text with values {}, {},{},{}' 
formated = some_str.format('word', True, 42, 77.7)
print(formated)


select_obj_in_squad = """ 
SELECT * FROM obj_locations
WHERE obj_lat BETWEEN {:f} AND {:f}
AND obj_lon BETWEEN {:f} AND {:f};
"""