# 存储所点披萨的信息
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }

# 概述所点披萨信息
print ("Your order a " + pizza['crust'] + "-crust pizza with"
                                          " the following toppings:")

for topping in pizza ['toppings']:
    print ("\t" + topping)