alien_o = {'color' : 'green', 'points' : 5}

print (alien_o)

alien_o['x_position'] = 0
alien_o['y_position'] = 25
print (alien_o)

# change the value of dictionary
print ("The alien color is " + alien_o['color'] + ".")
alien_o['color'] = 'yellow'
print ("The alien is now " + alien_o['color'] + ".")

# move the alien to the right side
# accroding the speed to decide how far the alien move

alien_i = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print ("Original x_position: " + str(alien_i['x_position']))

if alien_i['speed'] == 'slow':
    x_increment = 1
elif alien_i['speed'] == 'medium':
    x_increment = 2
else:
    # the speed of this alien must fast
    x_increment = 3

# the new position equals the old position add the increment
alien_i['x_position'] = alien_i['x_position'] + x_increment
print ("New x_position: " + str(alien_i['x_position']))