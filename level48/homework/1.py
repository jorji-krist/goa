def simple_multiplication(number):
    if number % 2 == 0:
        return number * 8
    else:
        return number * 9
    def invert(lst):
        return [-i for i in lst]
    def invert(lst):
        i = 0
        inv = []
        while i < len(lst):
            inv.append(lst[i] * -1)
            i += 1
        return inv
def fake_bin(x):
    result = ""
    for i in x:
        if int(i) < 5:
            result += '0'
        else:
            result += '1'
    return result

def string_to_array(s):
    if s == "":
        return [""] 
    result = s.split()
    return result

def rps(p1, p2):
    wins = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }
    
    if p1 == p2:
        return "Draw!"
    if wins[p1] == p2:
        return "Player 1 won!"
    else:
        return "Player 2 won!"

def greet(name, owner):
    if name == owner:
        return 'Hello boss'
    else:
        return 'Hello guest'

def monkey_count(n):
    list = []
    for i in range(1,n+1):
        list.append(i)
    return list

def human_years_cat_years_dog_years(human_years):
    if human_years == 1:
        cat_years = 15
        dog_years = 15
    elif human_years == 2:
        cat_years = 15 + 9
        dog_years = 15 + 9
    else:
        cat_years = 24 + (human_years - 2) * 4
        dog_years = 24 + (human_years - 2) * 5 
    
    return [human_years, cat_years, dog_years]