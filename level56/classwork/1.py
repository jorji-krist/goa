def nugzar_chubinidze(sadgerdzelo, limit):
    if sadgerdzelo > limit:
        return "ნუგზარი აღარ დალიო მეტი!"
    return "მოდი ახლა მართლა, დამილოცნიე!"

def yuri_gagarini(heart, pulse):
    heart = int(input("enter your heard pulse:"))
    pulse = int(input("enter your pulse"))

    if heart == pulse:
        return True
    return False

def captainjack():
    ship_prices = [150, 200, 250, 300, 350]
    coin = int(input("Enter your coins: "))
    ship = int(input("Choose a ship (1-5): "))

    if ship == 1:
        if coin >= ship_prices[0]:
            return "გაყიდულია"
    elif ship == 2:
        if coin >= ship_prices[1]:
            return "გაყიდულია"
    elif ship == 3:
        if coin >= ship_prices[2]:
            return "გაყიდულია"
    elif ship == 4:
        if coin >= ship_prices[3]:
            return "გაყიდულია"
    elif ship == 5:
        if coin >= ship_prices[4]:
            return "გაყიდულია"
    
    return "ეკიპაჟი აჯანყდება"
print(captainjack())

def apples():
    list = ["პანტა", "პანტა", "გორული"]
    list = list(set(apples_list))
    return list

print(apples())

def solve(s):
    upp = 0
    low = 0
    for i in s:
        if i.isupper():
            upp += 1
        elif i.islower():
            low += 1   
    if upp > lower:
        return s.upper()  
    else:
        return s.lower()