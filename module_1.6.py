from sys import stdout
#Словарь
my_dict = {"El": 1974, "Max": 1975, "Dustin": 1975, "Mike": 1976, "Will": 1974, "Lucas": 1975}
print(f"Characters:\n{my_dict}")
print(f'Max birth year:\n{my_dict["Max"]}')
print(f'Jims birth year:\n{my_dict.get("Jim","This character not found")}')
my_dict["Jim"] = 1947
my_dict["Joyce"] = 1956
my_dict.pop("Will")
print("Will gone")
print(my_dict)

#Множества
for i in range(101):
    if(i == 50):
        stdout.write("SET")
    stdout.write("-")
print()
my_set = {1, 2, 1, 2, 1, 2, True, False,"String", False,"string", 'String'}
print(my_set)
my_set.add(5)
my_set.add("False")
my_set.remove(1)
print(my_set)
