from pprint import pprint

def main():
    cook_book = get_cook_book()
    pprint(cook_book)


def get_cook_book():
    cook_book = {}
    with open("recipes.txt", encoding="utf-8") as file:
        data = [str_.strip() for str_ in file.readlines()]
        
        i = 0
        while i < len(data):
            #  Пустая строка
            if data[i] == "":
                i += 1
                continue
            # Название блюда
            dish_name = data[i]
            i+=1

            # Кол-во ингредиентов
            ingredients_counter = int(data[i])
            i += 1
            
            # Список со словарями ингредиентов и их параметрами
            ingredients = []
            for _ in range(ingredients_counter):
                ingredients_info = data[i].split("|")
                ingredients.append({"ingredient_name" : ingredients_info[0], "quantity" : ingredients_info[1], "measure" : ingredients_info[2]})
                i += 1
            
            cook_book[dish_name] = ingredients
            
    return cook_book





if __name__ == "__main__":
    main()
