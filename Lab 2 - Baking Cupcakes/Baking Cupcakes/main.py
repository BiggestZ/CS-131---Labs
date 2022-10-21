# Zahir Choudhry
# Lab #2 B - Baking Cupcakes
# 9 / 16 / 2021

""" CUPCAKES
Consider the following recipe for making 12 cupcakes:
Ingredients
For the cupcakes:
1 1/2 cups all-purpose flour
1 cup granulated sugar
1 1/2 teaspoons baking powder
1/2 teaspoon table salt
1/2 cup unsalted butter (1 stick), room temperature
1/2 cup sour cream
1 large egg, room temperature
2 large egg yolks, room temperature
1 1/2 teaspoons vanilla extract 
"""

""" VANILLA FROSTING
Additionally, for the vanilla buttercream frosting:
1 cup (8 ounces) unsalted butter, at room temperature
2 1/2 cups powdered sugar
1 tablespoon (3 teaspoons) vanilla extract
"""

""" COST OF ITEMS
5 lb (20 cups) bag of flour costs $3.09
5 lb (10 cups) bag of granulated sugar costs $2.98
1 lb (2 cups) box of butter costs $2.50
8 oz (1 cup) tub of sour cream costs $1.29
A dozen (12) eggs cost $2.68
2 lb (5 1/2 cup) bag of powdered sugar costs $1.18
2 fluid oz (12 teaspoons) bottle of vanilla extract costs $4.12
"""

#pluralize for recipes and cupcakes
def pluralize(amount, singular, plural): 
    if amount == 1:
        return singular
    else:
        return plural

# Round up for # of cupcakes needed
def ceil(number): 
    from math import ceil as math_ceil
    return math_ceil(number)

#Use to get $ Value
def two_decimal_places(number): 
    """
        >>> print(two_decimal_places(3))
        3.00

        >>> print(two_decimal_places(3.14159))
        3.14

        >>> print(two_decimal_places(3.516))
        3.52
    """
    return '{:.2f}'.format(number)



def cup_cakes(ppl):
    # Find the number of ppl that will be gettng cupcakes, 1 per person. ceil will round up
    a = ceil(ppl/12)

    #Print # of batches
    print("You need to make: " + str(a) + pluralize(a, " batch ", " batches ") + "of cupcakes\n\n")

    #Shopping List
    print("Shopping List for Vanilla Cupcakes:")
    for i in range(35):
        print("-", end="")
    print()

    #Ingredient Quantity Calculations
    flour_bags = ceil((1.5 * a)/20) # Cups
    sugar = ceil((1 * a)/10) # Cups
    bake_pow = ceil((1.5 * a)) # TeaSpoons / 
    salt = ceil((1.5 * a)) # TeaSpoons  /
    butter = ceil((1.5 * a)/2) # Cups
    sour_cream = ceil((0.5 * a)/ 1) # Cups
    egg_yolk = ceil((3 * a) / 12) # Eggs, will account for both yolks and whites
    vanilla = ceil((4.5 * a)/ 12) # TeaSpoons
    pow_sugar = ceil((2.5 * a) / 5.5)

    #Ingredient Price Calculations (Exclude Baking Power, and Salt)
    
    fb_price = float(two_decimal_places(flour_bags * 3.09))
    
    sug_price = float(two_decimal_places(sugar * 2.98))
    
    b_price = float(two_decimal_places(butter * 2.50))
    
    sc_price = float(two_decimal_places(sour_cream * 1.29))
    
    egg_price = float(two_decimal_places(egg_yolk * 2.68))
    
    v_price = float(two_decimal_places(vanilla * 4.12))
    
    pow_sug_price = float(two_decimal_places(pow_sugar * 1.18))
    
    total_price = float(two_decimal_places(fb_price + sug_price + b_price + sc_price + egg_price + v_price + pow_sug_price))
    
    
    #print values
    print(str(flour_bags) + pluralize(flour_bags, " bag", " bags") +" of flour")
    print(str(sugar) + pluralize(sugar, " bag", " bags") + " of granulated sugar")
    #print(str(bake_pow) + pluralize(bake_pow, " teaspoon", "teaspoons") + " of baking powder")
    #print(str(salt) + pluralize(salt, " teaspoon"," teaspoons") + "of salt")
    print(str(butter) + pluralize(butter, " box", " boxes") + " of butter")
    print(str(sour_cream) + pluralize(sour_cream, " tub", " tubs") + " of sour cream")
    print(str(egg_yolk) + pluralize(egg_yolk, " dozen", " dozens") + " eggs")
    print(str(pow_sugar) + pluralize(pow_sugar, " bag", " bags") + " of powdered sugar")
    print(str(vanilla) + pluralize(vanilla, " bottle", " bottles") + " of vanilla extract")
    #Print total cost
    print("Total expected cost of ingredients: $"+ str(total_price))
    #End

ppl = int(input("How many people do you need to serve?"))

cup_cakes(ppl)