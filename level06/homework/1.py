birth_year = int(input("შეიყვანეთ თქვენი დაბადების წელი: "))
current_year = 2024
age = current_year - birth_year
print(f"თქვენ ხართ {age} წლის.")

a = float(input("შეიყვანეთ ოთკუთხედის სიგრძე: "))
b = float(input("შეიყვანეთ ოთკუთხედის სიგანე: "))
c = a * b
d = 2 * (a + b)
print(f"ოთკუთხედის ფართობია: {c}, პერიმეტრია: {d}")

distance_km = float(input("შეიყვანეთ მანძილი სახლიდან სკოლამდე კილომეტრებში: "))
distance_m = distance_km * 1000
distance_cm = distance_m * 100
distance_mm = distance_cm * 10
print(f"მანძილი: {distance_m} მეტრი, {distance_cm} სანტიმეტრი, {distance_mm} მილიმეტრი.")

number = int(input("შეიყვანეთ ორნიშნა რიცხვი: "))
tens = number // 10
units = number % 10 
sum_digits = tens + units
print(f"თქვენი რიცხვის ციფრების ჯამია: {sum_digits}")