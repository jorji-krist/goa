def count_by(x, n):
    result = []
    i = 1
    while i <= n:
        result.append(x * i)
        i += 1
    return result

def get_planet_name(planet_id):
    if planet_id == 1:
        return "Mercury"
    elif planet_id == 2:
        return "Venus"
    elif planet_id == 3:
        return "Earth"
    elif planet_id == 4:
        return "Mars"
    elif planet_id == 5:
        return "Jupiter"
    elif planet_id == 6:
        return "Uranus"
    elif planet_id == 7:
        return "Neptune"
    else:
        return "error"
    
def human_years_cat_years_dog_years(human_years):
    if human_years == 1:
        cat_years = 15
        dog_years = 15
    elif human_years == 2:
        cat_years = 15 + 9
        dog_years = 15 + 9
    else:
        cat_years = 24 + (human_years - 2) * 4  # 24 is 15 + 9
        dog_years = 24 + (human_years - 2) * 5  # 24 is 15 + 9
    
    return [human_years, cat_years, dog_years]

def twice_as_old(dad_years_old, son_years_old):
    age_diff = dad_years_old - son_years_old
    double_son = son_years_old * 2
    
    double = abs(dad_years_old - double_son)
    
    return double