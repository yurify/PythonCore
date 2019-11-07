def zero_fuel(distance_to_pump, mpg, fuel_left):
    #Happy Coding! ;)
    if distance_to_pump/mpg > fuel_left:
        return False
    return True 