fruits = []

print("please enter your 4 faviroute fruit ")
for i in range(4):
    favfruit = input(f"Fruit {i} ") 
    fruits.append(favfruit)

    print(fruits)

    for fruit in fruits:
        print(f"my fav fruits is{fruit} ")  