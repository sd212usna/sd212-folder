# THIS IS A TESTER PROGRAM
# You can modify it as you like, but it will not be submitted.

from weight import Weight

apple = Weight(150, 'g')
grape = Weight(0.2, 'oz')

def print_weights(name, grams, ounces):
    print(f"{name} weighs {round(grams,2)} grams, or {round(ounces,2)} ounces")

print_weights("Apple", apple.g, apple.oz)
print_weights("Grape", grape.g, grape.oz)

# take a bite of the apple
# this should affect the weight of the grams AND the ounces!
apple.g = 100

print_weights("Bitten apple", apple.g, apple.oz)
print_weights("Original grape", grape.g, grape.oz)
