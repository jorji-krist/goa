def validate_pin(pin):
    if len(pin) == 4 or len(pin) == 6:  
        if pin.isdigit():  
            return True
    return False

def divisors(integer):
    divisors_list = []
    for i in range(2, integer):
        if integer % i == 0:  
            divisors_list.append(i) 
    if len(divisors_list) == 0:
        return f"{integer} is prime"  
    return divisors_list