import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
print(names)
length_of_string = len(names)
random_index = random.randint(0,length_of_string - 1)
# print(random_index)
buy_meal = names[random_index]
print(f"{buy_meal} is going to buy the meal today!")
