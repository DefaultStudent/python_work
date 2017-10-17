# @author : Vodka
# create at 2017/9/30

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles) 

del motorcycles[0]
print(motorcycles)

popped_motorcycle = motorcycles.pop(0)
print(motorcycles)
print(popped_motorcycle)
print("The last motorcycle I owned was a " + popped_motorcycle.title() + ".")

motorcycles.remove('ducati')
print(motorcycles)