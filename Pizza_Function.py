#A pepperoni and veggie pizza


def pepare_and_cook():
    print('Make pizza dough')
    print('Spread tomato sauce')
    print('Spread Cheese')
    print('Add additional toppings')
    print('Slide it in oven')

def pepperoni_pizza(ingredient):
    pepare_and_cook()
    pepperoni_pizza = 'A {} pizza'.format(ingredient)
    return pepperoni_pizza

def veggie_pizza(*ingredients):
    pepare_and_cook()
    veggie_pizza = 'a veggie pizza {} ingredients'.format(len(ingredients))
    return veggie_pizza
        
# make pepperoni pizza
print(pepperoni_pizza('pepperoni'))

# make a veggie pizza
print(veggie_pizza('onion','pepper','olive','mushroom','tomato'))
