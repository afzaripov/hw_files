from pprint import pprint

def main():
    cook_book = get_cook_book()
    shop_list = get_shop_list_by_dishes(cook_book, ['Фахитос', 'Омлет'], 2)
    pprint(shop_list)


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


def get_shop_list_by_dishes(cook_book : dict, dishes : list, person_count : int):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
           for ingredient in  cook_book[dish]:
                name = ingredient["ingredient_name"]
                measure = ingredient["measure"]
                quantity = int(ingredient["quantity"]) * person_count
            
                if name in shop_list:
                    shop_list[name]["quantity"] += quantity
                else:
                    shop_list[name] = {"measure": measure, "quantity": quantity} 

    return shop_list


if __name__ == "__main__":
    main()
