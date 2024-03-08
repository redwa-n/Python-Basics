mode_1 = {'color':'red', 'point': 5}
print(mode_1['color'])
print(mode_1['point'])

mode_1['border'] = 1
mode_1['tune'] = 'maan meri jaan'

mode_1['color'] = 'Yellow'
mode_1['speed'] = 'medium'

print(mode_1)

if mode_1['speed'] == 'slow':
    point_increment = 7
elif mode_1['speed'] == 'medium':
    point_increment = 8
else:
    point_increment = 9
    
    

mode_1['point'] = mode_1['point'] + point_increment

print(mode_1['point'])
print(mode_1)
