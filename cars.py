cars = ['bmw', 'audi', 'toyota', 'subaru']
"""
sort funtion sort the list of items in alphabetical order
and we can never revert to 
the original order
"""
cars.sort()
print(cars)

"""
reverse=true
function to enable reversing items in reverse alphabetical
order
"""
cars.sort(reverse=True)
print(cars)

"""
sorted():enables you to sort
items temporarily
"""
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

#function to print the list in reversal order
cars.reverse()
print(cars)