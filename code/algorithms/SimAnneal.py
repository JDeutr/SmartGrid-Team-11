from code.classes import house, battery
from code.algorithms import randomise

def simulated_annealing(batteries, houses):
    total_price = 0
    
    for battery in batteries:
        randomise.randomise_layout(battery, houses)
        battery.update_price(9)
        total_price += battery.price
    print(f"Starting price: {total_price}") 

    for i in 100:
        rand1 = randrange(5)
        rand2 = randrange(5)

        rand_house = random.choice(batteries[rand1])
        
        batteries[rand1].remove(rand_house)
        batteries[rand2].append(rand_house)

        for battery in batteries:
            total_price = 0
            
            battery.update_price(9)
            total_price += battery.price

        print(f"After {i} iterations the toeal price is {total_price}")


    