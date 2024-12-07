label door_fix_game_css:
    $ choice_menu_type = "scroll"
    menu:
        "Выберите CSS для стилизации двери:"
        
        # Верный
        '.door {{\n\ \ width: 100px;\n\ \ height: 200px;\n\ \ background-image: url("door-closed.png");\n\ \ background-size: cover;\n\ \ transform-origin: left;\n\ \ transition: transform 0.5s ease, background-image 0.5s ease;\n}':
            ba "Превосходно! Теперь это действительно похоже на дверь. Всё выглядит как надо!"
            sp "Да, согласен. Код не только функционален, но и аккуратен. Молодец, Эмрах!"
            $ css_state.set_completed()
        
        # Верный, но стилистика нарушена
        '.door {{\n\ \ width: 100px;\n\ \ height: 200px;\n\ \ background: url("door-closed.png") center/contain;\n\ \ transform-origin: left;\n\ \ transition: none;\n\ \ border: 5px dotted red\n}':
            ba "Ну, сработало, дверь выглядит как надо. Отлично, идём дальше!"
            sp "Стоп-стоп. Вместо 'background-color' тут написали просто 'background'. Работает, но это не совсем точно."
            ba "Работает же, а ты хочешь идеала? Решай, Эмрах, оставляем так или исправляем."
            call door_fix_game_css
        
        # Похожий на верный
        '.door {{\n\ \ width: 100px;\n\ \ height: 200px;\n\ \ background: url("door-closed.png") repeat;\n\ \ transform-origin: center;\n\ \ transition: transform 0.5s ease-in-out;\n\ \ border: none;\n}':
            ba "Эй, высоты у двери нет! Теперь это просто коричневый прямоугольник. Попробуй ещё раз."
            call door_fix_game_css
    $ choice_menu_type = ""
    return