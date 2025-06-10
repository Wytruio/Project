def main():
    bookings = []
    users = {}
    history = []
    
    options = [
        {"id": 1, "type": "Отель", "name": "Гранд Отель", "price": 5000, "available": True},
        {"id": 2, "type": "Апартаменты", "name": "Уютные апартаменты", "price": 3500, "available": True},
        {"id": 3, "type": "Хостел", "name": "Веселый хостел", "price": 1000, "available": False},
    ]
    
    def find_best_option(user_budget, prefer_type=None):
        nonlocal options
        available_options = [opt for opt in options if opt["available"] and opt["price"] <= user_budget]
        
        if prefer_type:
            available_options = [opt for opt in available_options if opt["type"] == prefer_type]
        
        if not available_options:
            return None
        
        available_options.sort(key=lambda x: x["price"])
        return available_options[0]

    while True:
        print("\n=== Система бронирования ===")
        print("1. Просмотреть доступные варианты")
        print("2. Забронировать")
        print("3. Найти лучший вариант по бюджету")
        print("4. Просмотреть историю запросов")
        print("5. Выйти")
        
        choice = input("Выберите действие: ")
        history.append(f"Выбран пункт меню: {choice}")
        
        if choice == "1":
            print("\nДоступные варианты:")
            for opt in options:
                status = "доступен" if opt["available"] else "не доступен"
                print(f"{opt['id']}. {opt['type']} '{opt['name']}' - {opt['price']} руб. ({status})")
            
        elif choice == "2":
            name = input("Введите ваше имя: ")
            opt_id = int(input("Введите ID варианта для бронирования: "))
            
            selected = next((opt for opt in options if opt["id"] == opt_id), None)
            
            if selected and selected["available"]:
                bookings.append({
                    "user": name,
                    "option_id": opt_id,
                    "option_name": selected["name"],
                    "price": selected["price"]
                })
                selected["available"] = False
                users[name] = users.get(name, []) + [opt_id]
                print(f"Успешно забронировано: {selected['name']} за {selected['price']} руб.")
            else:
                print("Выбранный вариант недоступен или не существует")
                
        elif choice == "3":
            print("\nПодбор лучшего варианта по вашему бюджету")
            name = input("Введите ваше имя: ")
            budget = int(input("Введите ваш бюджет: "))
            prefer_type = input("Введите предпочтительный тип (отель/апартаменты/хостел) или оставьте пустым: ")
            
            best = find_best_option(budget, prefer_type if prefer_type else None)
            
            if best:
                print(f"Рекомендуем: {best['type']} '{best['name']}' за {best['price']} руб.")
                history.append(f"Для пользователя {name} подобран вариант: {best['name']}")
            else:
                print("К сожалению, нет доступных вариантов по вашему бюджету")
                history.append(f"Для пользователя {name} не найдено вариантов по бюджету {budget}")
                
        elif choice == "4":
            print("\nИстория ваших запросов:")
            for i, record in enumerate(history, 1):
                print(f"{i}. {record}")
                
        elif choice == "5":
            print("Выход из системы...")
            break
            
        else:
            print("Неверный ввод, попробуйте еще раз")

if __name__ == "__main__":
    main()