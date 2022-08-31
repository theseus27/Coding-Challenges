#Given a range that each light can cover and an array of house locations, find the minimum number of lights needed to illuminate the whole street. If it can't be done, return -1. A light will light up the street from [i-radius, i+radius].

def lights(radius, houses):
    lights = 0
    while houses:
        lights += 1
        position = houses[0] + radius
        for i in reversed(houses):
            if i >= position-radius and i <= position+radius:
                houses.remove(i)
    return lights

print(lights(3, [-5, 1, 2, 6, 8, 9]))   #Should be 3
print(lights(3, [-5, 1, 3, 6, 8, 9]))   #Should be 2