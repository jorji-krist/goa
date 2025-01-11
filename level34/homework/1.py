tuple = ("lorem1", "lorem2", "lorem3", "lorem4", "lorem5")
lorem1, lorem2, *rest = tuple
print(lorem1, lorem2)
print(rest)

print("--------------------------")

numbers = (2, 56, 99, 22, 15, 23, 66, 11, 134, 23, 66, 91, 22, 2, 23)
print(numbers.count(23))

print("--------------------------")

aura = (10, 25, 5, 80, 70, 20)
for biggest in aura:
    if biggest > 10:
        print(biggest)

print("--------------------------")

# list-სა და tuple-ს შორის განსხვავება არის ის რომ ჩვენ არ შეგვიძლია tuple-ს გამოყენების შემდეგ მოვახდინოთ რაიმე ცვლილება მასში მყოფ ცვლადებს შორის, მაგრამ list-ში ეს შესაძლებელია.

print("--------------------------")

#immutable და mutable ნიშნავს უცვლადს და ცვლადს. ჩვენ ამ ორ ტერმინს ვაკავშირებთ tuple და list-თან, tuple არის უცვლადი, ხოლო list არის ცვლადი. 