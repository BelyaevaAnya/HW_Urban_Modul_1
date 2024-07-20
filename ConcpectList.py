food = ['apple', 'banana', 'coconut']
print(food[0])
food[0] = 'peach'
print(food)
# Добавление элемента в конец списка
food.append(True)
print(food)
# Добавление элемента
food.extend(["string", 2])
food.extend(["string"])
print(food)
food.extend("string")
print(food)         # => ['peach', 'banana', 'coconut', True, 'string', 2, 'string', 's', 't', 'r', 'i', 'n', 'g']
food = ['apple', 'banana', 'coconut']
food.remove("apple")
print(food)
print("coconut" in food)
print("coconut" not in food)
print(food[0:3])
print(food[0:2:2])