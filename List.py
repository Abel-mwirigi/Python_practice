bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
bicycles[0] = 'Crek'

#append function to add new elements at the end of the list
bicycles.append('Noah')
print(bicycles)

#function to delete elements cant be accessed after that
del bicycles[0]
print(bicycles)

#function to delete elements at the end of the list but can still be accessed
popped_bicycle = bicycles.pop()
print(bicycles)
print(popped_bicycle)

#you can still choose the index of the element to delete
first_owned = bicycles.pop(0)
print(bicycles)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

bicycles_toAdd = ['Yamaha', 'Ducati', 'Suzuki', 'Honda']
bicycles.extend(bicycles_toAdd)

#to delete the element
bicycles.remove('Ducati')
print(bicycles)