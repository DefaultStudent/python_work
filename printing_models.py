# first create a list include some designs will be print
unprinted_designs = ['iphone case', 'roboot pendant', 'dodecahedron']
completed_models = []

# print every designs till there are no design are not print
# move to the completed_models after print
while unprinted_designs:
    current_design = unprinted_designs.pop()

    #imitate print 3D models process accroding by design
    print ("Printing models: " + current_design)
    completed_models.append(current_design)

# show all printed models
print ("\nThe following models have been printed:")
for completed_model in completed_models:
    print (completed_model)